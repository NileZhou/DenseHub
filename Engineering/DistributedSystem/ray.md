```python
@ray.remote(num_gpus=0) # This orchestrator task itself doesn't need a GPU
def process_partition_on_actor_task(actor_handle, main_config: OmegaConf, partition_dataset_df: pd.DataFrame, partition_chat_list: list, worker_id: int):
    print(f"[Task for Worker {worker_id}] Starting to process data partition of size {len(partition_dataset_df)}")

    # Initialize tokenizer within the remote task
    # Each task needs its own tokenizer instance if it's doing the tokenization.
    local_model_path = copy_local_path_from_hdfs(main_config.model.path)
    tokenizer = hf_tokenizer(local_model_path) # Assuming hf_tokenizer is globally available or imported
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = 'left' # Typically left padding for generation

    # Construct worker-specific output path from main_config and worker_id
    base_output_path = main_config.data.output_path
    output_dir = os.path.dirname(base_output_path)
    base_filename = os.path.basename(base_output_path)
    name, ext = os.path.splitext(base_filename)
    # Ensure the worker file has a .jsonl extension
    worker_output_filename = f"{name}_worker_{worker_id}.jsonl"
    worker_output_path = os.path.join(output_dir, worker_output_filename)

    # Create directory for output file if it doesn't exist
    if output_dir and not os.path.exists(output_dir):
        # makedirs might not be available if not imported at top level. Let's assume it is or use os.makedirs.
        # For safety, let's use os.makedirs which is standard.
        os.makedirs(output_dir, exist_ok=True)

    if os.path.exists(worker_output_path):
        # Overwrite existing worker file if it exists, to ensure fresh run for this partition
        print(f"[Task for Worker {worker_id}] Output file {worker_output_path} exists. Will be overwritten.")
        try:
            os.remove(worker_output_path)
        except OSError as e:
            print(f"[Task for Worker {worker_id}] Error removing existing file {worker_output_path}: {e}. Proceeding to write.")

    config_batch_size = main_config.data.batch_size
    num_batches_in_partition = (len(partition_dataset_df) + config_batch_size - 1) // config_batch_size
    
    print(f"[Task for Worker {worker_id}] Processing {len(partition_dataset_df)} samples in {num_batches_in_partition} batches.")

    for batch_idx in tqdm(range(num_batches_in_partition), desc=f"Task for Worker {worker_id}", position=worker_id):
        batch_start_idx = batch_idx * config_batch_size
        batch_end_idx = (batch_idx + 1) * config_batch_size
        
        current_batch_chat_lst = partition_chat_list[batch_start_idx:batch_end_idx]
        current_batch_dataset_slice = partition_dataset_df.iloc[batch_start_idx:batch_end_idx]

        if not current_batch_chat_lst: # Should not happen if logic is correct
            continue

        inputs = tokenizer.apply_chat_template(current_batch_chat_lst,
                                             add_generation_prompt=True,
                                             padding=True, 
                                             truncation=True,
                                             max_length=main_config.rollout.prompt_length,
                                             return_tensors='pt',
                                             return_dict=True,
                                             tokenize=True)
        
        input_ids_tensor = inputs['input_ids']
        attention_mask_tensor = inputs['attention_mask']
        # Compute position_ids; ensure compute_position_id_with_mask is available
        position_ids_tensor = compute_position_id_with_mask(attention_mask_tensor)

        batch_dict_for_proto = {
            'input_ids': input_ids_tensor,
            'attention_mask': attention_mask_tensor,
            'position_ids': position_ids_tensor
        }
        
        data_proto_batch = DataProto.from_dict(batch_dict_for_proto)
        
        # Invoke generate_sequences on the dedicated actor for this partition
        # The actor handle (actor_handle) is specific to one GPU actor
        output_sequences_proto = ray.get(actor_handle.generate_sequences.remote(data_proto_batch))
        output_sequences_proto = output_sequences_proto.to('cpu') # Ensure data is on CPU for subsequent processing

        generated_ids = output_sequences_proto.batch['input_ids']
        
        actual_generated_ids_list = []
        for i in range(generated_ids.shape[0]):
            # Assuming generated_ids contains prompt + response, slice for response part
            # The original code used -config.rollout.response_length:
            actual_generated_ids_list.append(generated_ids[i, -main_config.rollout.response_length:])

        output_text_decoded = tokenizer.batch_decode(actual_generated_ids_list, skip_special_tokens=False)
        
        pad_token = tokenizer.pad_token if tokenizer.pad_token is not None else tokenizer.eos_token
        output_text_unpad = [text.replace(pad_token, '') for text in output_text_decoded]

        num_responses_per_prompt = main_config.rollout.n
        processed_batch_df = current_batch_dataset_slice.copy()

        if num_responses_per_prompt > 1:
            if len(output_text_unpad) == len(processed_batch_df) * num_responses_per_prompt:
                reshaped_responses = np.array(output_text_unpad).reshape(len(processed_batch_df), num_responses_per_prompt).tolist()
                processed_batch_df['responses'] = reshaped_responses
            else:
                print(f"[Task for Worker {worker_id}] Warning: Mismatch in expected number of responses for batch {batch_idx}. Got {len(output_text_unpad)}, expected {len(processed_batch_df) * num_responses_per_prompt}. Padding with empty lists.")
                responses_data = []
                current_resp_idx = 0
                for _ in range(len(processed_batch_df)):
                    end_resp_idx = current_resp_idx + num_responses_per_prompt
                    slice_to_append = output_text_unpad[current_resp_idx:end_resp_idx]
                    # Pad if slice is shorter than num_responses_per_prompt
                    slice_to_append.extend([''] * (num_responses_per_prompt - len(slice_to_append)))
                    responses_data.append(slice_to_append)
                    current_resp_idx = end_resp_idx
                processed_batch_df['responses'] = responses_data
        else:
            processed_batch_df['responses'] = output_text_unpad

        # Append the processed batch to the worker's JSONL file
        # Open in append mode. Create if not exists (handled by initial check/removal)
        with open(worker_output_path, 'a', encoding='utf-8') as f:
            processed_batch_df.to_json(f, orient='records', lines=True, force_ascii=False)
    
    print(f"[Task for Worker {worker_id}] Finished processing. Output written to {worker_output_path}")
    return worker_output_path

```