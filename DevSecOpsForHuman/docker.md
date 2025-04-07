# run docker




# docker file

## commit container to image

不要直接commit，那样镜像会非常大


先清理:

```shell
apt-get clean
rm -rf /var/lib/apt/lists/*
rm -rf ~/.cache/pip
conda clean --all -y
rm -rf /tmp/* /var/tmp/*
```

宿主机执行:

*将容器导出为扁平化tar包（会丢失历史层）这样得到的image只会有一层*   
<del>docker export <container-id> | docker import - <my_compact_image></del>

```shell

# 重打tag
docker tag <my_compact_image> <new_img_name:version>
```

# Dockerfile
打镜像:
```shell
docker build --network-host -f <docker_file_path> -t <image-name>:<tag> .
```
后边的点代表打镜像时用到的上下文地址

# Network
使用宿主机网络:
--name nginx代表给容器取个名字
```shell
docker run --name nginx --net host <镜像名>
```


# mirror management

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



# speed up docker pull


docker pull太慢:
替换下载命令
将 gcr.io 替换为 gcr.nju.edu.cn

将 k8s.gcr.io 替换为 gcr.nju.edu.cn/google-containers

将 ghcr.io 替换为 ghcr.nju.edu.cn

将 nvcr.io 替换为 ngc.nju.edu.cn

将 quay.io 替换为 quay.nju.edu.cn

# Win10安装
先安装WSL：  
1. 软件商店搜索ubuntu20.04LTS，获取，安装   
2. 开启hyperV   
3. 安装docker-desktop   

一切正常的话就可以在cmd和powershell里用docker命令了


# 关联远程仓库
docker login <远程仓库域名> -u <用户名> -p <密码>  


# command cheetsheet


```shell
# push image
## 1. 先打tag
docker tag <原镜像名>:<原tag> <远程仓库域名>/<仓库名>/<新镜像名>:<新tag>
## 2. push
docker push <远程仓库域名>/<仓库名>/<新镜像名>:<新tag>


# start container from image
## 注意后面不能加 /bin/bash，否则容器跑不起来，会变成Exited(0)状态
docker run -it -p <本地端口>:<容器端口> <镜像name:tag> 

# container 管理
docker stop Name或者ID  
docker start Name或者ID  
docker kill Name或者ID  
docker restart name或者ID
# 删除container (也可以直接docker rm -f <name或ID>)
## docker rm不能直接删除运行中的容器，可是使用-f, --force参数，表示强制删除，即直接向容器中的主进程发送SIGKILL信号，一般不推荐这么做，建议先使用docker stop停止容器，然后再使用docker rm删除容器，给容器留出一些时间进行清理等工作
## 1. 先stop
docker stop <name或id>
## 2. 删除
docker rm <name或id>

# image 管理
docker rmi <镜像1的ID> <镜像2的ID>

# 文件复制
## 在windows下: docker默认的用户路径是/c/Users/windows的登录用户名，所以在docker下可以直接访问windows用户桌面上文件。注意一定要先 cd 到 ~/Desktop 目录，直接 docker cp ~/Desktop/upload.txt myCentos:/usr/local会报错：GetFileAttributesEx C:\c: The system cannot find the file specified.
## host -> container
docker cp <宿主机文件路径> <容器ID>:<容器里路径>
## container -> host
docker cp <容器ID>:<容器里路径> <宿主机文件路径>
```

docker run -it -p <本地端口>:<容器端口> <镜像name:tag>
注意不能加 /bin/bash，否则容器跑不起来，会变成Exited(0)状态
原理:
Dockerfile文件中有两个关键字CMD和ENTRYPOINT。其中CMD的值是可以被覆盖的。举个栗子：
```yaml
FROM python
CMD ["/home/hello.sh","Hello World"]   
ENTRYPOINT ["/home/hello.sh","xiaoming"]
```
如果在docker run后增加了/bin/bash，执行的CMD就变成了/bin/bash。一般镜像文件中两种关键字选用其中之一就可以了，但也可以同时使用。同时使用的时候，CMD中的值会被当作ENTRYPOINT的参数。所以，ENTRYPOINT的内容就变成["/home/hello.sh","/bin/bash"]。那么镜像内置的执行命令就无法正确执行了，于是容器就Exited了


# 终止容器中的process
CTRL+C是不行的

CTRL+P, CTRL+Q可以

然后docker run -it <容器ID> /bin/bash 进去
