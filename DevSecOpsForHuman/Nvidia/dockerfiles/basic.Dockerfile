FROM m.daocloud.io/docker.io/nvidia/cuda:12.4.1-cudnn-devel-ubuntu22.04

# 在此Dockerfile同目录下新建一个resources目录，resources目录下分别为cuda相关文件和hpcx相关文件
# ├── cuda
# │   ├── cuda_12.4.1_550.54.15_linux.run
# │   └── cudnn-local-repo-ubuntu2204-9.10.0_1.0-1_amd64.deb
# └── hpcx
#     ├── doca-host_3.0.0-058000-25.04-ubuntu2204_amd64.deb
#     ├── hpcx-v2.21.2-gcc-doca_ofed-ubuntu22.04-cuda12-x86_64
#     └── hpcx-v2.21.2-gcc-doca_ofed-ubuntu22.04-cuda12-x86_64.tbz

# 设置代理（仅在构建阶段有效，注意变为自己的代理ip）
ENV http_proxy=http://10.136.0.191:10890 \
    https_proxy=http://10.136.0.191:10890


# 设置非交互式环境（跳过所有提示）
ENV DEBIAN_FRONTEND=noninteractive

# 预先配置时区（中国上海为例）
RUN ln -fs /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    apt update && \
    apt install -y tzdata && \
    dpkg-reconfigure --frontend noninteractive tzdata

# resources里为doca-ofed(doca-host版)和hpcx
# 如果目标容器构建镜像的过程中，/opt/hpcx 目录不存在，Docker 的 COPY 指令会自动创建该目录。如果路径中包含多级不存在的目录，它们也都会被一并创建。
COPY resources/hpcx/* /opt/hpcx/

# 命令太长，由于网络抖动，可能会因为网络问题失败，这时可将长命令拆分
# 第1行: 安装python3.12
# 第2-3行: 设置python3.12为默认python
# 第4行: 安装编译工具
# 第5-6行: 安装Python 开发依赖
# 第7行: 安装debug和监控工具以及基础工具
RUN apt update && apt install software-properties-common -y && add-apt-repository ppa:deadsnakes/ppa -y && apt update && apt install python3.12 -y && \
    update-alternatives --install /usr/bin/python python /usr/bin/python3.12 1 && \
    update-alternatives --config python && \
    apt install -y build-essential cmake ninja-build git curl wget && \
    apt install -y python3.12-dev python3.12-venv && python -m ensurepip --upgrade && \
    python -m pip install --upgrade pip setuptools wheel && \
    apt install -y jq iputils-ping htop net-tools rsync

# 因为source命令是bash特有的 
SHELL ["/bin/bash", "-c"]

# 1-2行装doca-ofed  3-5行装hpcx
RUN cd /opt/hpcx && dpkg -i doca-host_3.0.0-058000-25.04-ubuntu2204_amd64.deb && \
    apt-get update && apt-get install mft=4.32.0-120 && apt-get -y install doca-ofed && \
    tar -xvf hpcx-v2.21.2-gcc-doca_ofed-ubuntu22.04-cuda12-x86_64.tbz && \
    echo 'source /opt/hpcx/hpcx-v2.21.2-gcc-doca_ofed-ubuntu22.04-cuda12-x86_64/hpcx-init.sh' >> ~/.bashrc && \
    echo 'hpcx_load' >> ~/.bashrc && source ~/.bashrc && \
    rm -rf /opt/hpcx/doca-host_3.0.0-058000-25.04-ubuntu2204_amd64.deb && \
    rm -rf /opt/hpcx/hpcx-v2.21.2-gcc-doca_ofed-ubuntu2204-cuda12-x86_64.tbz && \
    rm -rf /var/lib/apt/lists/* && apt-get clean

# COPY resources/cuda/* /opt/cuda/，不要用COPY, 一用COPY必然镜像大小爆炸
# 1-2行: cuda （wget https://developer.download.nvidia.com/compute/cuda/12.4.1/local_installers/cuda_12.4.1_550.54.15_linux.run）
# 3-4行: cudnn （wget https://developer.download.nvidia.com/compute/cudnn/9.10.0/local_installers/cudnn-local-repo-ubuntu2204-9.10.0_1.0-1_amd64.deb）
# 5行: 清理
RUN rm -rf /usr/local/cuda* && \
    mkdir -p /opt/cuda && cd /opt/cuda && http_proxy= https_proxy= wget https://developer.download.nvidia.com/compute/cuda/12.4.1/local_installers/cuda_12.4.1_550.54.15_linux.run && \
    http_proxy= https_proxy= wget https://developer.download.nvidia.com/compute/cudnn/9.10.0/local_installers/cudnn-local-repo-ubuntu2204-9.10.0_1.0-1_amd64.deb && \
    sh /opt/cuda/cuda_12.4.1_550.54.15_linux.run --silent --toolkit --override && \
    dpkg -i /opt/cuda/cudnn-local-repo-ubuntu2204-9.10.0_1.0-1_amd64.deb && cp /var/cudnn-local-repo-ubuntu2204-9.10.0/cudnn-*-keyring.gpg /usr/share/keyrings/ && \
    apt-get update && apt-get -y install cudnn-cuda-12 && \
    rm -rf /var/lib/apt/lists/* && apt-get clean && rm -rf /opt/cuda


ENV http_proxy= \
    https_proxy=

    