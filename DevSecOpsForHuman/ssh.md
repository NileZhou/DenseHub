# 设置SSH免密登录

典型需求:
我想在自己的MacBook Pro里直接ssh vllm-server，就能连接到远程Ubuntu 22.04服务器里

## 远程服务器所需工作

**1. 首先确保远程服务器SSH服务可用**

- 普通 Ubuntu（带 systemd）
```bash
sudo apt update
sudo apt install openssh-server -y
```

- 容器或无 systemd 环境
```bash
sudo apt update
sudo apt install openssh-server -y
sudo mkdir -p /var/run/sshd
# -D 表示不守护进程，直接在前台运行，容器中可用 & 放后台
sudo /usr/sbin/sshd -D &
```

检查 SSH 是否可用
```bash
ps aux | grep sshd
netstat -tlnp | grep 22  # 默认22，或用自己的自定义端口
```

防火墙设置(选用)
```bash
sudo ufw allow 19422/tcp   # 如果我们没使用22，使用的是非标准端口
sudo ufw enable            # 如果 ufw 没启用
```


**2. 配置sshd_config**
编辑SSH配置文件：
apt install -y vim
vim /etc/ssh/sshd_config

关键设置：
```ini
Port 19422                  # 使用你需要的端口
PermitRootLogin yes         # 允许root登录（生产环境建议禁用）
PubkeyAuthentication yes    # 启用公钥认证
PasswordAuthentication yes  # 禁临时启用以便初次上传公钥
```


**3.重启SSH服务**
```bash
# 若有systemd服务
sudo systemctl restart ssh

# 容器中/无systemd服务
sudo pkill sshd          # 先杀掉老的 sshd
sudo /usr/sbin/sshd -D & # 后台启动新的 sshd
```


## 本地所需工作

**1.在本地生成SSH密钥对**
```bash
ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa_vllm
```
- 按提示操作（可设置密码或直接回车跳过）
- 生成两个文件：`id_rsa_vllm`(私钥)和`id_rsa_vllm.pub`(公钥)

**2. 复制公钥到远程服务器**
```bash
# 在本地查看公钥内容
cat ~/.ssh/id_rsa_vllm.pub

# 登录远程服务器（使用其他方式）
mkdir -p ~/.ssh
echo "粘贴你的公钥内容" >> ~/.ssh/authorized_keys
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
```

或者
```bash
ssh-copy-id -i ~/.ssh/id_rsa_vllm.pub -p 19422 root@10.1.126.13 # 如果远程暴露出的端口是19422
```

**3. 配置本地SSH config文件 (~/.ssh/config)**

示例配置：
```
Host vllm-server
    HostName 10.1.126.13  # 替换为你的服务器IP
    User root             # 替换为你的用户名
    Port 19422            # 替换为你的端口
    IdentityFile ~/.ssh/id_rsa_vllm
    ServerAliveInterval 60
    ServerAliveCountMax 10
```

**4. 测试连接**
```bash
ssh vllm-server
```
