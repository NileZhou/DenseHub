# Conda

## 安装miniconda

*参考：下载:https://www.anaconda.com/docs/getting-started/miniconda/install#quickstart-install-instructions*

mkdir -p /data0/users/x/env

**下载 Miniconda 安装脚本**
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /data0/users/x/env/miniconda.sh

**安装到指定目录（注意 -p 参数指定路径）**
一定要将 -p 的路径安装到持久化路径，不然如果在容器里，一重启就没了
bash /data0/users/x/env/miniconda.sh -b -u -p /data0/users/x/env/miniconda3

**激活 conda**
source /data0/users/x/env/miniconda3/bin/activate

**初始化 conda（这会将 conda 添加到你的 shell 配置中）**
/data0/users/x/env/miniconda3/bin/conda init --all


## 创建env环境

conda create -n <name> python=3.12


## conda activate后默认python不变问题

1. find conda related directory
conda env list

2. cd to the directory

cd <directory>/conda-meta/

3. vim state file
vim state

4. add path
正常的state文件内容:
```json
{"env_vars": {"PATH":"/data0/users/software/cuda-12.4/bin:/data0/users/software/20240312_conda/miniconda/envs/internvl/bin:/data0/users/software/20240312_conda/miniconda/condabin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/data0/users/software/20240312_conda/miniconda/envs/internvl/lib","LD_LIBRARY_PATH":"/data0/users/software/cuda-12.4/lib64:/data0/users/software/20240312_conda/miniconda/envs/internvl/lib"}}
```

