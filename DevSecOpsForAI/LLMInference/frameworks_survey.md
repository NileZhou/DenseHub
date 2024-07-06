# General Common Sense

model precision choose

CPU: BFloat16

GPU: Float16

# Personal

ChatGPT-Like Desktop Client: LMStudio

# Personal & small team

Ollama

# vLLM

It claims that it can attach 14x - 24x throughput than huggingface/transformers, 2.2x - 2.5x than TGI(huggingface/TextGenerationInference)

applicable scenarios:

- process batched requests, especially high-batch requests

Core tech:

- Paged Attention (borrows from the classic solution of virtual memory and paging in operating system) to manage KV Cache
- continus batching
- quantization
- Optimized CUDA kernels
- tensor parallel
- 

Support Feature:

- Compatible with OpenAI API
- seamless integration with huggingface models



Advantage:

- easy to use
- support Nvidia CUDA / AMD ROCm / AWS Neuron / CPU



Disadvantages:

- single user request
- not optimized for quantized models (only support 2-3 types of quantized models)

problem: https://zhuanlan.zhihu.com/p/658780653

# exllamav2

applicable scenarios:

- single user, modern consumer-class GPUs (also support batch generation). You can get roughly 200 tokens per seconds on a single 4090 gpu for a 7b model.

additional:

- exl2 quantization: based on the same optimization method as GPTQ and supports 2, 3, 4, 5, 6 and 8-bit quantization, mixed with in a model.

# NVIDA/TensorRT-LLM

Former version: FasterTransformer


It use optimize-compiled LLM rather than origin LLM weight to inference, so faster than vLLM.



applicable senarios:

- 10 - 60 user requests, within GPU



Look also: https://github.com/NVIDIA/TensorRT: support vast range of different ml models, not only llms

Core tech:

- PagedAttention
- layer fusion: fusion multiple layers to a kernel (like multi-head attention)
- Matmul auto adjustment
- Low-precision inference
- Using MPI/NCCL to implement tensor parallelize

applicable scenatios:

- support vast range of different ml models, not only llms





# microsoft/DeepSpeed-MII (almost dead)

powerd by deepspeed

It claims that can attach 2-2.3x than vLLM

Core tech:

- Blocked KV Caching
- Continous Batching

* High Performance CUDA Kernels
* Dynamic SplitFuse
* DeepFusion for Transformers
* Multi-GPU Inference with Tensor-Slicing
* ZeRO-Inference for Resource Constrained Systems
* Compiler Optimizations

# fastllm

fastllm是一个基于量化技术的大模型推理加速工具，通过降低模型参数的精度，可以在保证模型性能的同时减少推理所需的计算资源和内存占用。以下是使用fastllm的基本步骤：

1. **安装fastllm库** ：从GitHub上克隆fastllm的仓库，并按照官方文档进行安装。
2. **加载预训练模型** ：使用fastllm提供的API加载你想要加速的LLM模型。
3. **模型量化** ：调用fastllm的量化函数对模型进行量化，选择合适的量化位数以达到最佳性能和速度的平衡。
4. **推理** ：使用量化后的模型进行推理，你将发现推理速度和内存占用都得到了优化。

# llama.cpp

llama.cpp是一个基于C++实现的大模型推理工具，通过优化底层计算和内存管理，可以在不牺牲模型性能的前提下提高推理速度。以下是使用llama.cpp的基本步骤：

1. **安装llama.cpp库** ：从GitHub上克隆llama.cpp的仓库，并按照官方文档进行安装。
2. **加载预训练模型** ：使用llama.cpp提供的API加载你想要加速的LLM模型。
3. **配置推理参数** ：根据实际需要配置推理过程中的参数，如批处理大小、并行度等。
4. **推理** ：使用llama.cpp进行推理，你将发现推理速度得到了显著提升，并且可以利用C++的灵活性进行更高级别的定制和优化。

# Other frameworks

- https://github.com/flexflow/FlexFlow   it claims that can attach 2x+ than TGI / FasterTransformer / vLLM
- https://github.com/PygmalionAI/aphrodite-engine
- SGLang

aphrodite

tests:

- https://www.bentoml.com/blog/benchmarking-llm-inference-backends
- https://www.inferless.com/learn/exploring-llms-speed-benchmarks-independent-analysis

# Ollama

Highlight:
