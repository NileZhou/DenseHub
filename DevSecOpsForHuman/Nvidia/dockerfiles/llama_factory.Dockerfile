FROM basic:0.1
# 这里的basic镜像见basic.Dockerfile，如果目标云平台已经有基础镜像(cuda-12.4.1-cudnn-ubuntu22.04)了，basic换成它的即可

# 设置非交互式环境（跳过所有提示）
ENV DEBIAN_FRONTEND=noninteractive http_proxy=http://10.136.0.191:10890 \
    https_proxy=http://10.136.0.191:10890

# 装pytorch的话，代理位置选在美国是最快的
# 其他 ray liger-kernel tensordict hydra-core tabulate, torchvision和torchaudio不要
RUN pip install --no-cache-dir torch==2.6.0 --index-url https://download.pytorch.org/whl/cu124 && \
    pip install --no-cache-dir vllm==0.8.4 flash_attn==2.7.4.post1 liger-kernel==0.5.9 && \
    pip install --no-cache-dir accelerate datasets==3.5.0 peft==0.15.1 trl==0.9.6 deepspeed==0.16.5 matplotlib wandb omegaconf ujson ijson && \
    pip cache purge && rm -rf /var/lib/apt/lists/* && apt-get clean && rm -rf /tmp/* /var/tmp/* /var/log/*

ENV http_proxy= \
https_proxy=