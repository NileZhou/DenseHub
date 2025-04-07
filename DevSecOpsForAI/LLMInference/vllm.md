# troubleshooting

VLLM_USE_MODELSCOPE=True  
这个命令参数要不得，会导致报错:  
FileNotFoundError: [Errno 2] No such file or directory: '/tmp/tmplnor8nqj/gauge_mostrecent_400327.db'  
导致启动不了

# check support models
https://docs.vllm.ai/en/latest/models/supported_models.html

# Run with docker on Nvidia GPU

1. First, set docker runtime to nvidia

reference: [installing-with-apt](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#installing-with-apt)

```
# Configure the production repository:
$ curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
  && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
    sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
    sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list

$ sed -i -e '/experimental/ s/^#//g' /etc/apt/sources.list.d/nvidia-container-toolkit.list

$ sudo apt-get update

$ sudo apt-get install -y nvidia-container-toolkit

```

2. set docker configuration

```json
{
  "runtimes": {
    "nvidia": {
      "path": "nvidia-container-runtime",
      "runtimeArgs": []
    }
  },
  "default-runtime": "nvidia"
}

```

3. restart docker

sudo systemctl restart docker

4. test run vllm using docker

docker run --runtime nvidia --gpus all
    -v ~/.cache/huggingface:/root/.cache/huggingface
    -p 8000:8000
    --ipc=host
    --entrypoint python3
    vllm/vllm-openai:latest
    /usr/local/lib/python3.10/dist-packages/vllm/entrypoints/openai/api_server.py
    --api-key token-abc123
    --gpu-memory-utilization 0.8
    --max-model-len 8192
    --served-model-name llama3.1-8B
    --tensor-parallel-size 4
    --model /root/.cache/huggingface/hub/models--hugging-quants--Meta-Llama-3.1-8B-Instruct-GPTQ-INT4/snapshots/ba3eae7a24afbe0fb490020523cd099b69703f65



测试:

```
$ curl http://localhost:8000/v1/chat/completions -H "Content-Type: application/json"     -H "Authorization: Bearer token-abc123"     -d '{
            "model": "llama3.1-8B",
            "messages": [{"role": "user", "content": "Why is the sky blue?"}]
        }'

```


多并发测试:

```
import time
import os
import json
import requests
from transformers import PreTrainedTokenizerFast
from concurrent.futures import ThreadPoolExecutor, as_completed

os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")

def load_tokenizer(tokenizer_path):
    return PreTrainedTokenizerFast(tokenizer_file=tokenizer_path)

def send_request(text, url, headers, data):
    # 发送请求并记录时间
    start_time = time.time()
    response = requests.post(url, headers=headers, data=json.dumps(data))
    end_time = time.time()
    duration = end_time - start_time

    # 解析响应以获取输出tokens数
    response_data = response.json()
    output_tokens = response_data['usage']['completion_tokens']

    return output_tokens, duration, response_data

def perform_concurrent_requests(num_requests, text, tokenizer, url, headers, data):
    # 准备执行多线程
    with ThreadPoolExecutor(max_workers=num_requests) as executor:
        futures = [executor.submit(send_request, text, url, headers, data) for _ in range(num_requests)]
    
        total_tokens = 0
        total_duration = 0
        responses = []
    
        for future in as_completed(futures):
            output_tokens, duration, response_data = future.result()
            total_tokens += output_tokens
            total_duration += duration
            responses.append(response_data)
    
        # 计算平均每秒输出token数
        if total_duration > 0:
            tokens_per_second = total_tokens / total_duration
        else:
            tokens_per_second = 0
    
        return tokens_per_second, total_tokens, total_duration, responses

# 路径到你的tokenizer.json
tokenizer_path = "/home/llm/.cache/huggingface/hub/models--hugging-quants--Meta-Llama-3.1-8B-Instruct-GPTQ-INT4/snapshots/ba3eae7a24afbe0fb490020523cd099b69703f65/tokenizer.json"
tokenizer = load_tokenizer(tokenizer_path)

# API details
url = "http://localhost:8000/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer token-abc123"
}
data = {
    "model": "llama3.1-8B",
    "messages": [{"role": "user", "content": "Why is the sky blue?"}]
}

# 设置并发数和文本
num_requests = 16  # 并发数
text = "Why is the sky blue?"

tokens_per_second, total_tokens, total_duration, responses = perform_concurrent_requests(num_requests, text, tokenizer, url, headers, data)

print(f"Total Output Tokens: {total_tokens}")
print(f"Total Duration for all requests: {total_duration:.2f} seconds.")
print(f"Average Output Tokens per second: {tokens_per_second:.2f}")

```



```text
usage: api_server.py [-h] [--host HOST] [--port PORT]
                     [--uvicorn-log-level {debug,info,warning,error,critical,trace}]
                     [--allow-credentials] [--allowed-origins ALLOWED_ORIGINS]
                     [--allowed-methods ALLOWED_METHODS]
                     [--allowed-headers ALLOWED_HEADERS] [--api-key API_KEY]
                     [--lora-modules LORA_MODULES [LORA_MODULES ...]]
                     [--prompt-adapters PROMPT_ADAPTERS [PROMPT_ADAPTERS ...]]
                     [--chat-template CHAT_TEMPLATE]
                     [--response-role RESPONSE_ROLE]
                     [--ssl-keyfile SSL_KEYFILE] [--ssl-certfile SSL_CERTFILE]
                     [--ssl-ca-certs SSL_CA_CERTS]
                     [--ssl-cert-reqs SSL_CERT_REQS] [--root-path ROOT_PATH]
                     [--middleware MIDDLEWARE] [--model MODEL]
                     [--tokenizer TOKENIZER] [--skip-tokenizer-init]
                     [--revision REVISION] [--code-revision CODE_REVISION]
                     [--tokenizer-revision TOKENIZER_REVISION]
                     [--tokenizer-mode {auto,slow}] [--trust-remote-code]
                     [--download-dir DOWNLOAD_DIR]
                     [--load-format {auto,pt,safetensors,npcache,dummy,tensorizer,bitsandbytes}]
                     [--dtype {auto,half,float16,bfloat16,float,float32}]
                     [--kv-cache-dtype {auto,fp8,fp8_e5m2,fp8_e4m3}]
                     [--quantization-param-path QUANTIZATION_PARAM_PATH]
                     [--max-model-len MAX_MODEL_LEN]
                     [--guided-decoding-backend {outlines,lm-format-enforcer}]
                     [--distributed-executor-backend {ray,mp}]
                     [--worker-use-ray]
                     [--pipeline-parallel-size PIPELINE_PARALLEL_SIZE]
                     [--tensor-parallel-size TENSOR_PARALLEL_SIZE]
                     [--max-parallel-loading-workers MAX_PARALLEL_LOADING_WORKERS]
                     [--ray-workers-use-nsight] [--block-size {8,16,32}]
                     [--enable-prefix-caching] [--disable-sliding-window]
                     [--use-v2-block-manager]
                     [--num-lookahead-slots NUM_LOOKAHEAD_SLOTS] [--seed SEED]
                     [--swap-space SWAP_SPACE]
                     [--cpu-offload-gb CPU_OFFLOAD_GB]
                     [--gpu-memory-utilization GPU_MEMORY_UTILIZATION]
                     [--num-gpu-blocks-override NUM_GPU_BLOCKS_OVERRIDE]
                     [--max-num-batched-tokens MAX_NUM_BATCHED_TOKENS]
                     [--max-num-seqs MAX_NUM_SEQS]
                     [--max-logprobs MAX_LOGPROBS] [--disable-log-stats]
                     [--quantization {aqlm,awq,deepspeedfp,fp8,fbgemm_fp8,marlin,gptq_marlin_24,gptq_marlin,awq_marlin,gptq,squeezellm,compressed-tensors,bitsandbytes,None}]
                     [--rope-scaling ROPE_SCALING] [--rope-theta ROPE_THETA]
                     [--enforce-eager]
                     [--max-context-len-to-capture MAX_CONTEXT_LEN_TO_CAPTURE]
                     [--max-seq-len-to-capture MAX_SEQ_LEN_TO_CAPTURE]
                     [--disable-custom-all-reduce]
                     [--tokenizer-pool-size TOKENIZER_POOL_SIZE]
                     [--tokenizer-pool-type TOKENIZER_POOL_TYPE]
                     [--tokenizer-pool-extra-config TOKENIZER_POOL_EXTRA_CONFIG]
                     [--enable-lora] [--max-loras MAX_LORAS]
                     [--max-lora-rank MAX_LORA_RANK]
                     [--lora-extra-vocab-size LORA_EXTRA_VOCAB_SIZE]
                     [--lora-dtype {auto,float16,bfloat16,float32}]
                     [--long-lora-scaling-factors LONG_LORA_SCALING_FACTORS]
                     [--max-cpu-loras MAX_CPU_LORAS] [--fully-sharded-loras]
                     [--enable-prompt-adapter]
                     [--max-prompt-adapters MAX_PROMPT_ADAPTERS]
                     [--max-prompt-adapter-token MAX_PROMPT_ADAPTER_TOKEN]
                     [--device {auto,cuda,neuron,cpu,openvino,tpu,xpu}]
                     [--scheduler-delay-factor SCHEDULER_DELAY_FACTOR]
                     [--enable-chunked-prefill [ENABLE_CHUNKED_PREFILL]]
                     [--speculative-model SPECULATIVE_MODEL]
                     [--num-speculative-tokens NUM_SPECULATIVE_TOKENS]
                     [--speculative-draft-tensor-parallel-size SPECULATIVE_DRAFT_TENSOR_PARALLEL_SIZE]
                     [--speculative-max-model-len SPECULATIVE_MAX_MODEL_LEN]
                     [--speculative-disable-by-batch-size SPECULATIVE_DISABLE_BY_BATCH_SIZE]
                     [--ngram-prompt-lookup-max NGRAM_PROMPT_LOOKUP_MAX]
                     [--ngram-prompt-lookup-min NGRAM_PROMPT_LOOKUP_MIN]
                     [--spec-decoding-acceptance-method {rejection_sampler,typical_acceptance_sampler}]
                     [--typical-acceptance-sampler-posterior-threshold TYPICAL_ACCEPTANCE_SAMPLER_POSTERIOR_THRESHOLD]
                     [--typical-acceptance-sampler-posterior-alpha TYPICAL_ACCEPTANCE_SAMPLER_POSTERIOR_ALPHA]
                     [--disable-logprobs-during-spec-decoding DISABLE_LOGPROBS_DURING_SPEC_DECODING]
                     [--model-loader-extra-config MODEL_LOADER_EXTRA_CONFIG]
                     [--ignore-patterns IGNORE_PATTERNS]
                     [--preemption-mode PREEMPTION_MODE]
                     [--served-model-name SERVED_MODEL_NAME [SERVED_MODEL_NAME ...]]
                     [--qlora-adapter-name-or-path QLORA_ADAPTER_NAME_OR_PATH]
                     [--otlp-traces-endpoint OTLP_TRACES_ENDPOINT]
                     [--engine-use-ray] [--disable-log-requests]
                     [--max-log-len MAX_LOG_LEN]
```


# usual run shell commands

```shell
CUDA_VISIBLE_DEVICES=0,3,4,6 \
    vllm serve /njfs/train-nlp/zhouyi9/base_models/Qwen/Qwen2___5-VL-32B-Instruct \
    --mm-processor-kwargs '{"max_pixels":1806336, "min_pixels":401408}' \
    --tensor-parallel-size 4 \
    --dtype bfloat16 \
    --port 9999 \
    --host 0.0.0.0 \
    --gpu_memory_utilization 0.6 \
    --max-model-len 16384 \
    --served_model_name qwenvl
```