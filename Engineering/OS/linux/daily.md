防止机器OOM死机:
```shell
# 1.安装earlyoom,提前在内存压力高时杀掉占用大的进程(容器也是进程),安装完毕即自动启用
sudo apt install earlyoom
systemctl status earlyoom # 检查是否可用

# 2. 调整配置
# 配置文件在 /etc/default/earlyoom，可以调整阈值，比如：
# 默认是低于10%空闲内存或5%空闲swap就触发
EARLYOOM_ARGS="-m 10 -s 5 -r 60"
# 参数含义：
# -m: 最小可用内存百分比（低于就触发）
# -s: 最小可用 swap 百分比
# -r: 每秒最多打印一次日志

# 3. 改完后重启服务
sudo systemctl restart earlyoom
```

parquet文件 看第一行(只推荐这种方案，但是parquet文件过大的话真的看不了):
先 pip install parquet-inspector
pqi head -n 1 xxx.parquet | jq .
pqi head -n 1 


jsonl文件看第一行:
head -1 xxx.jsonl | jq .

排查inode数:
去到某个目录下，然后: du --inodes -d 1 | sort -nr  可显示此目录下的下一级文件数
df -ih

排查fd数量: cat /proc/sys/fs/file-nr


vscode修复：
rm -rf /root/.cursor-server/cli/servers/*


AI Infra问题:
如果容器一直起不来，检查下是不是自己的镜像有问题或镜像没推到远程


docker环境修复:
遇到nvidia-smi突然不能用的情况
docker restart xxx 即可


hfd下载
export HF_ENDPOINT=https://hf-mirror.com
参考: https://gist.github.com/padeoe/697678ab8e528b85a2a7bddafea1fa4f#file-hfd-sh


杀程序关联的所有进程
pgrep -f <name> | xargs kill -9


tmux
tmux kill-server

wandb
wandb login --host <自有wandb host name>


chatgpt
env http_proxy=http://127.0.0.1:7890 https_proxy=http://127.0.0.1:7890 open -a "/Applications/ChatGPT.app"


tmux下编辑失败
export TERM=xterm


截图
ocr: shift + command + 4  需要复制就加control
编辑/pin: shift + command + 2


gitlab
git clone 对应项目，然后cd 到项目里
git config --local user.name xxx
git config --local user.email xxxx-mail-address

即可
查看:
git config --global user.name
git config --global user.email

nohup
后台运行程序，ssh会话挂了还运行
nohup python -u gemini.py > output_gemini.log 2>&1  &
nohup python -u qvq.py > output_qvq.log 2>&1  &

- u: 无缓冲模式运行 Python，标准输出和标准错误立即写入日志文件
- nohup：忽略挂断信号
- >：重定向标准输出到 output.log
- 2 > &1: 将标准错误重定向到标准输出
- & 后台运行程序


jupyter lab
得上ssh隧道
在本地机器上: ssh -L 8888:localhost:8888 -p 22 root@10.136.0.191
输入密码连上开发机，然后
1. conda activate <对应env>
2. conda install ipykernel  (弄过就不弄了)
3. conda install jupyterlab (弄过就不弄了)
4. python -m ipykernel install --user --name <对应env> --display-name "Python <对应env>" (注册kernel，弄过就不弄了)
5. jupyter lab —allow-root
本地输入url即可访问
5. 打开一个notebook，右上角选择自己刚才注册的kernel

jupyter lab --allow-root


统计文件大小
du -BG --max-depth=1


rsync
--ignore-existing: 忽略已经存在的文件, 跳过已下载的文件

rsync对比scp，增加了断点续传、checksum校验等支持
上传大文件 (rsync)
rsync -av --partial --progress -e "ssh -p <远程端口>"  <本地目录或文件> <远程user>@<远程ip>:<远程文件夹地址>

下载大文件 (rsync)
rsync -av --partial --progress -e "ssh -p <远程端口>"  <远程user>@<远程ip>:<远程文件夹地址> <本地目录或文件>


rsync -av --partial --progress -e "ssh -p 22" root@10.136.0.191:

上传
scp -P <目标端口> -r <本地目录> root@10.133.169.31:<远程目录>

下载
scp -P <目标端口> -r root@10.133.169.31:<远程目录>  <本地目录>



conda
下载:https://www.anaconda.com/docs/getting-started/miniconda/install#quickstart-install-instructions
conda create -n <name> python=3.10


huggingface
下载大模型的时候用
pip install -U "huggingface_hub[cli]"
pip install hf_transfer 
huggingface-cli login
HF_HUB_ENABLE_HF_TRANSFER=1 huggingface-cli download <model-id>


pip
临时用官方repo，不用mirror:
pip install --index-url https://pypi.org/simple <包>

清华mirror:
pip install -i https://mirrors.aliyun.com/pypi/simple <包>

