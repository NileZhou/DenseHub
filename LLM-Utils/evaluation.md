# convenient eval frameworks

1. lm-evaluation-harness

 https://github.com/EleutherAI/lm-evaluation-harness

```shell
lm_eval --model vllm \
    --model_args pretrained={model_name},tensor_parallel_size={GPUs_per_model},dtype=auto,gpu_memory_utilization=0.8,data_parallel_size={model_replicas} \
    --tasks lambada_openai \
    --batch_size auto
```

