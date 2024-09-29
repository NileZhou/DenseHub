

设置容器开机自启动:
docker update --restart=always <容器ID>

# Redis

docker安装redis方法：
1.用命令来查看可用版本： docker search redis 
2.拉取官方的最新版本的镜像：docker pull redis:latest
3.查看镜像：docker images
4.运行 redis 容器：docker run -itd --name redis-test -p 6379:6379 redis

如果是腾讯的轻量级服务器，要使用可视化工具远程连接的话，记得去腾讯控制台放行6379端口

给redis设置密码：
先用命令 docker ps 查看容器id
1.进入redis的容器 [docker](https://so.csdn.net/so/search?q=docker&spm=1001.2101.3001.7020) exec -it 容器ID bash
2.进入redis目录 cd /usr/local/bin
3.运行命令：redis-cli
4.查看现有的redis密码：config get requirepass
5.设置redis密码config set requirepass 123456（123456为你要设置的密码）  (注意这个其实是在内存中的，所以重启容器后会丢失，需要再次设置一遍)


# RabitMQ

docker pull rabbitmq:management
docker run -p 5672:5672 -p 15672:15672 --name rabbitmq -d rabbitmq:management
访问localhost:15672，初始账号密码为guest  guest

添加用户后，记得授权给vhost