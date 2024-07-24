efficient-learning and inference: https://github.com/horseee/Awesome-Efficient-LLM

# Background

key benchmarks:

- Time To First Token(TTFT)
- Token Generation Rate
- 

# More

https://github.com/DefTruth/Awesome-LLM-Inference

# Speculative Decoding

# KV Cache Optimization

MHA: Multi Head Attention

GQA: Group Query Attention

MQA: Multi Query Attention

MLA:  Multi-head Latent Attention: it use LoRA like thought

MLKV: Multi-Layer Key Value (https://arxiv.org/html/2406.09297v2)

reference:

https://spaces.ac.cn/archives/10091  (strongly recommend)

# Attention Optimization

Paged Attention

Flash Attention


sparse attention (speedup in prefilling stage):

https://github.com/microsoft/MInference   


# Batch Inference Strategy

# Multi-Iteration Inference Strategy

Based on prefix k-v cache reusing

# Quantization

**That depends**, not all low-precision computation are faster than higher ones, it usually happens in that situation: reduce GPU numbers by reducing memory usage

If it happens in one single GPU, FP16 usually inference quickly than BF16
