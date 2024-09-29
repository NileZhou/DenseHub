# 容器

unshare 和 nsenter 都是来自包 util-linux 的命令, 依靠它们可用于操控 Linux 的进程 namemspace, 以实现对特定系统对象或资源的隔离,

# 安装

## Win10

先安装WSL： wsl --update
再安装docker-desktop 这个软件，选择使用wsl运行

一切正常的话就可以在cmd和powershell里用docker命令了

## CentOS 7

[参考](https://docs.docker.com/engine/install/centos/)

```shell
sudo yum install -y yum-utils
sudo yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo
sudo yum install docker-ce docker-ce-cli containerd.ios
sudo systemctl start docker
# test
sudo docker run hello-world
```

注: 安装docker-compose:

1. 把https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)

下载到/usr/local/bin/docker-compose

2. 加执行权限

```shell
sudo chmod +x /usr/local/bin/docker-compose
```

3. 软链接

```shell
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
```

测试:

```shell
sudo docker-compose --version
```

# 与远程仓库协同

## 关联远程仓库

这里关联的是远程私有仓库harbor

```shell
docker login <远程仓库域名> -u <用户名> -p <密码>
```

## push镜像

先得打tag

```shell
docker tag <原镜像名>:<原tag> <远程仓库域名>/<仓库名>/<新镜像名>:<新tag>
```

push:

```shell
docker push <远程仓库域名>/<仓库名>/<新镜像名>:<新tag>
```

**注意，推上Harbor的镜像默认是私有的，需要登陆页面更改成公有**


# Using registry-mirrors

If you can't pull images from dockerhub.com, eg: You are in China.  You will need this


vim /etc/docker/daemon.json:

```json
{
    "registry-mirrors": ["<custom registry domain or ip>"]
}
```

domain recommendation list (in China):
- https://dockerpull.com
- https://docker.1panel.live
- https://dockerproxy.cn
- https://docker.hpcloud.cloud


check if the replace is successful:
```shell
docker info
```



# 执行镜像(启动容器)

```shell
docker run -it -p <本地端口>:<容器端口> <镜像name:tag>
```

注意后面不能加 /bin/bash，否则容器跑不起来，会变成Exited(0)状态
原理:
Dockerfile文件中有两个关键字**CMD**和**ENTRYPOINT**。其中CMD的值是可以被覆盖的。举个栗子：

```dockerfile
FROM python
CMD ["/home/hello.sh","Hello World"]   
ENTRYPOINT ["/home/hello.sh","xiaoming"]
```

如果在docker run后增加了/bin/bash，执行的CMD就变成了/bin/bash。一般镜像文件中两种关键字选用其中之一就可以了，但也可以同时使用。同时使用的时候，CMD中的值会被当作ENTRYPOINT的参数。所以，ENTRYPOINT的内容就变成["/home/hello.sh","/bin/bash"]。那么镜像内置的执行命令就无法正确执行了，于是容器就Exited了

# 容器暂停，启动，杀死，重启

```shell
docker stop Name或者ID  
docker start Name或者ID  
docker kill Name或者ID  
docker restart name或者ID
```

## 终止容器中的进程

CTRL+C是不行的

CTRL+P, CTRL+Q可以

然后docker run -it <容器ID> /bin/bash 进去

# 删除

先停止:

```shell
docker stop <容器ID>
```

删除容器:

```shell
docker rm <容器ID>
```

docker rm不能直接删除运行中的容器，可是使用-f, --force参数，表示强制删除，即直接向容器中的主进程发送SIGKILL信号，一般不推荐这么做，建议先使用docker stop停止容器，然后再使用docker rm删除容器，给容器留出一些时间进行清理等工作

删除所有停止的容器:

```shell
docker container prune
```

删除镜像:

```shell
docker rmi <镜像1的ID 1> <镜像2的ID>
```

# 文件复制

从宿主机到容器:

```shell
docker cp <宿主机文件路径> <容器ID>:<容器里路径>
```

从容器到宿主机:

```shell
docker cp <容器ID>:<容器里路径> <宿主机文件路径>
```

在windows下:
docker默认的用户路径是/c/Users/windows的登录用户名，所以在docker下可以直接访问windows用户桌面上文件。注意一定要先 cd 到 ~/Desktop 目录，直接 docker cp ~/Desktop/upload.txt myCentos:/usr/local
会报错：GetFileAttributesEx C:\c: The system cannot find the file specified.

# 容器迁移到另一主机

常有的需求，怎么将当前已运行的容器（包含一系列运行时的端口映射等迁移到另一主机）

```shell
# 1. 先把当前运行时的容器打成镜像
docker commit <container_id> <新镜像名>

# 2. 导出镜像为tar文件 （如果在win10下，这个文件会出现在命令行所在文件夹下）
docker save <新镜像名> > mynewimage.tar

# 3. 传输此文件，可通过FTP或SCP进行传输

# 4. 加载镜像
docker load < mynewimage.tar

# 5. 运行镜像 (注意端口映射等信息全没了)
docker run -d --name mynewcontainer mynewimage
```

# Dockerfile

语法参考: [https://www.runoob.com/docker/docker-dockerfile.html](https://www.runoob.com/docker/docker-dockerfile.html)

打镜像:

```shell
docker build --network-host -f <docker_file_path> -t <image-name>:<tag> .
```

后边的点代表打镜像时用到的上下文地址

运行命令:
**RUN**：用于执行后面跟着的命令行命令。有以下俩种格式：

```shell
# shell 格式：
RUN <命令行命令>
# <命令行命令> 等同于，在终端操作的 shell 命令。


# exec 格式：
RUN ["可执行文件", "参数1", "参数2"]
# 例如：
# RUN ["./test.php", "dev", "offline"] 等价于 RUN ./test.php dev offline

```

# 网络

使用宿主机网络:
--name nginx代表给容器取个名字

```shell
docker run --name nginx --net host <镜像名>
```
