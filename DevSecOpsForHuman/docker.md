配置daemon.json文件
在配置文件 /etc/docker/daemon.json 中加入：

{
"registry-mirrors":["https://docker.nju.edu.cn/"]
}
一些可用的镜像源:

https://dockerpull.com
https://docker.1panel.live
https://dockerproxy.cn
https://docker.hpcloud.cloud
然后执行:
sudo systemctl daemon-reload
sudo systemctl restart docker


docker pull太慢:
替换下载命令
将 gcr.io 替换为 gcr.nju.edu.cn

将 k8s.gcr.io 替换为 gcr.nju.edu.cn/google-containers

将 ghcr.io 替换为 ghcr.nju.edu.cn

将 nvcr.io 替换为 ngc.nju.edu.cn

将 quay.io 替换为 quay.nju.edu.cn


# 