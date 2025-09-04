
数据并行：

```python
import os
import time
import json
import pandas as pd
import torch
import torch.distributed as dist
from torch.nn.parallel import DistributedDataParallel as DDP
from transformers import AutoModelForCausalLM, AutoTokenizer
from tqdm import tqdm
import logging

# --- 日志配置 ---
def get_logger(rank):
    logger = logging.getLogger(f"ddp_infer_rank{rank}")
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter(f"%(asctime)s [%(levelname)s][rank={rank}] %(message)s")
    if not logger.handlers:
        logger.addHandler(logging.StreamHandler())
        if rank == 0:
            logger.addHandler(logging.FileHandler("/njfs/train-aitech/projects/y/exaone_testinference.log"))
    return logger

# --- 1. 设置和加载模型 ---
MODEL_NAME = "/njfs/train-aitech/projects/z/verl-rllm/exps/exps-group-math-baseline/models/EXAONE-4.0-1.2B"
DATASET_PATH = "/njfs/train-aitech/projects/x/projects/coderl/verl/oexps/data/livecodebench_start_2025-02-01.parquet"
OUTPUT_FILE = "/njfs/train-aitech/projects/y/exaone_test/inference_results_exaone1.2B_livecodebench_start_2025-02-01.jsonl"

OUTER_BATCH_SIZE = 16
NUM_GENERATIONS_PER_PROMPT = 4
EFFECTIVE_BATCH_SIZE = OUTER_BATCH_SIZE * NUM_GENERATIONS_PER_PROMPT
NUM_SAMPLES_TO_PROCESS = None

# --- DDP 初始化 ---
def setup_distributed():
    dist.init_process_group(backend="nccl")
    local_rank = int(os.environ["LOCAL_RANK"])
    torch.cuda.set_device(local_rank)
    return local_rank, dist.get_rank(), dist.get_world_size()

def main():
    local_rank, rank, world_size = setup_distributed()
    logger = get_logger(rank)
    logger.info(f"DDP initialized: rank={rank}, local_rank={local_rank}, world_size={world_size}")

    # 加载模型到本地GPU
    logger.info("Loading model and tokenizer...")
    try:
        model = AutoModelForCausalLM.from_pretrained(
            MODEL_NAME,
            torch_dtype=torch.bfloat16,
            device_map={"": local_rank},
            attn_implementation="flash_attention_2"
        ).cuda(local_rank)
        logger.info("Model loaded with Flash Attention 2.")
    except ImportError:
        logger.warning("Flash Attention 2 not available. Loading model with default attention.")
        model = AutoModelForCausalLM.from_pretrained(
            MODEL_NAME,
            torch_dtype=torch.bfloat16,
            device_map={"": local_rank}
        ).cuda(local_rank)
    model = DDP(model, device_ids=[local_rank])

    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    logger.info(f"Model is loaded on devices: {model.device_ids if hasattr(model, 'device_ids') else local_rank}")
    logger.info(f"Effective batch size for model.generate(): {EFFECTIVE_BATCH_SIZE}")

    # --- 2. 数据加载 ---
    logger.info(f"\nLoading dataset from {DATASET_PATH}...")
    try:
        df = pd.read_parquet(DATASET_PATH)
        if NUM_SAMPLES_TO_PROCESS is not None:
            df = df.head(NUM_SAMPLES_TO_PROCESS)
        logger.info(f"Dataset loaded. Processing {len(df)} samples.")
    except FileNotFoundError:
        logger.error(f"Error: Dataset file not found at {DATASET_PATH}")
        dist.destroy_process_group()
        return

    # --- 3. 按rank切分数据 ---
    df_split = df.iloc[rank::world_size].reset_index(drop=True)
    logger.info(f"Rank {rank} processing {len(df_split)} samples.")

    logger.info(f"\n--- Starting Large Batch 1-to-{NUM_GENERATIONS_PER_PROMPT} Generation ---")

    all_results = []
    total_process_start_time = time.time()
    total_generation_time = 0.0
    total_new_tokens_generated = 0

    for i in tqdm(range(0, len(df_split), OUTER_BATCH_SIZE), desc=f"Rank{rank} Batches"):
        batch_df = df_split.iloc[i:i+OUTER_BATCH_SIZE]
        mega_batch_prompts = []
        for prompt in batch_df['prompt'].tolist():
            mega_batch_prompts.extend([prompt] * NUM_GENERATIONS_PER_PROMPT)
        formatted_prompts = [
            tokenizer.apply_chat_template(
                [{"role": "user", "content": p}],
                tokenize=False,
                add_generation_prompt=True,
                enable_thinking=True
            ) for p in mega_batch_prompts
        ]
        tokenizer.padding_side = "left"
        inputs = tokenizer(
            formatted_prompts,
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=2048
        ).to(local_rank)
        generation_start_time = time.time()
        with torch.no_grad():
            outputs = model.module.generate(
                **inputs,
                max_new_tokens=30720,
                do_sample=True,
                temperature=0.8,
                top_p=0.95,
                pad_token_id=tokenizer.pad_token_id
            )
        generation_end_time = time.time()
        total_generation_time += (generation_end_time - generation_start_time)
        input_lengths = inputs['input_ids'].shape[1]
        generated_ids = outputs[:, input_lengths:]
        total_new_tokens_generated += generated_ids.numel()
        batch_answers = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)
        for j, row in enumerate(batch_df.iterrows()):
            original_data = row[1].to_dict()
            start_index = j * NUM_GENERATIONS_PER_PROMPT
            end_index = start_index + NUM_GENERATIONS_PER_PROMPT
            prompt_specific_answers = batch_answers[start_index:end_index]
            result_entry = original_data.copy()
            result_entry['generated_answers'] = prompt_specific_answers
            all_results.append(result_entry)

    total_process_end_time = time.time()
    total_process_time = total_process_end_time - total_process_start_time

    logger.info("\n--- Generation Finished ---")
    logger.info(f"Total processing time: {total_process_time:.2f} seconds")
    logger.info("\n--- Performance (Throughput) ---")
    if total_generation_time > 0:
        throughput = total_new_tokens_generated / total_generation_time
        logger.info(f"Total pure generation time: {total_generation_time:.2f} seconds")
        logger.info(f"Total new tokens generated: {total_new_tokens_generated}")
        logger.info(f"Outer Batch Size: {OUTER_BATCH_SIZE}")
        logger.info(f"Generations per Prompt (k): {NUM_GENERATIONS_PER_PROMPT}")
        logger.info(f"Effective Batch Size: {EFFECTIVE_BATCH_SIZE}")
        logger.info(f"Throughput: {throughput:.2f} tokens/second")
    else:
        logger.warning("Could not calculate throughput.")

    # --- 4. 收集所有进程的结果到主进程 ---
    # 先将每个进程的结果序列化
    import pickle
    result_bytes = pickle.dumps(all_results)
    result_size = torch.tensor([len(result_bytes)], dtype=torch.long, device=local_rank)
    sizes = [torch.zeros_like(result_size) for _ in range(world_size)]
    dist.all_gather(sizes, result_size)
    max_size = int(max([s.item() for s in sizes]))
    padded = result_bytes + b' ' * (max_size - len(result_bytes))
    gathered = [torch.empty(max_size, dtype=torch.uint8, device=local_rank) for _ in range(world_size)]
    dist.all_gather(gathered, torch.frombuffer(padded, dtype=torch.uint8).to(local_rank))

    # --- 5. 全局统计信息收集与输出 ---
    local_time = torch.tensor([total_generation_time], dtype=torch.float64, device=local_rank)
    local_tokens = torch.tensor([total_new_tokens_generated], dtype=torch.long, device=local_rank)
    all_times = [torch.zeros_like(local_time) for _ in range(world_size)]
    all_tokens = [torch.zeros_like(local_tokens) for _ in range(world_size)]
    dist.all_gather(all_times, local_time)
    dist.all_gather(all_tokens, local_tokens)

    if rank == 0:
        all_results_merged = []
        for i, (buf, sz) in enumerate(zip(gathered, sizes)):
            part = bytes(buf[:sz.item()])
            all_results_merged.extend(pickle.loads(part))
            logger.info(f"Collected {len(pickle.loads(part))} results from rank {i}.")
        logger.info(f"Total merged results from all ranks: {len(all_results_merged)}")
        # 全局统计输出
        max_time = float(torch.max(torch.stack(all_times)))
        total_tokens = int(torch.sum(torch.stack(all_tokens)))
        logger.info(f"[Global] Total pure generation time (max of all ranks): {max_time:.2f} seconds")
        logger.info(f"[Global] Total new tokens generated (all ranks): {total_tokens}")
        if max_time > 0:
            logger.info(f"[Global] Throughput (all ranks): {total_tokens / max_time:.2f} tokens/second")
        else:
            logger.warning("[Global] Could not calculate throughput.")
        try:
            with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
                for entry in all_results_merged:
                    f.write(json.dumps(entry, ensure_ascii=False) + '\n')
            logger.info(f"\nAll results from all ranks saved to '{OUTPUT_FILE}'.")
        except IOError as e:
            logger.error(f"Error writing to file {OUTPUT_FILE}: {e}")
        logger.info("All ranks finished. Unified result file generated.")
    dist.barrier()
    dist.destroy_process_group()

if __name__ == "__main__":
    main()


```