
# Virtual Box装Ubuntu
友情提示: 

1. 没有ssd别装虚拟机
2. 硬盘设为动态大小，别固定大小
## 安装步骤

1. create 虚拟机，设置硬盘大小
2. 配置iso

点击设置->storage
![image.png](https://cdn.nlark.com/yuque/0/2021/png/22348649/1632707294209-0165a871-6a50-4824-aa9c-fdddb115c1bb.png#clientId=uab59e6bc-36fa-4&from=paste&height=350&id=uf7587f01&originHeight=523&originWidth=665&originalType=binary&ratio=1&rotation=0&showTitle=false&size=40841&status=done&style=none&taskId=udec1d687-5749-44c7-b8aa-13111ca4c0d&title=&width=445.5)
点击右边的光盘，选择iso文件

3. 配置网络

因为我的虚拟机想使用Host的VPN，所以选择NAT，但是在这个模式之下，虚拟机可以访问主机，但是主机不能访问虚拟机

4. 启动，过程中有提示，选择启动盘

选择语言为中文，键盘布局为US:
![image.png](https://cdn.nlark.com/yuque/0/2021/png/22348649/1632708211599-140e638f-3572-4e02-aa80-fead805e4ee2.png#clientId=uab59e6bc-36fa-4&from=paste&height=462&id=u090479c5&originHeight=606&originWidth=795&originalType=binary&ratio=1&rotation=0&showTitle=false&size=75556&status=done&style=none&taskId=u8c28f74c-fca5-4b0f-ab8d-47781c9d4b1&title=&width=606.5)

最小安装:
![image.png](https://cdn.nlark.com/yuque/0/2021/png/22348649/1632708250687-8883fec5-17b1-4004-b193-f94a58c8a98c.png#clientId=uab59e6bc-36fa-4&from=paste&height=466&id=ue8779827&originHeight=606&originWidth=799&originalType=binary&ratio=1&rotation=0&showTitle=false&size=73852&status=done&style=none&taskId=ud659198b-b876-479a-a869-99504199946&title=&width=614.4886169433594)

## 进入系统

### 1 改root密码
```shell
sudo passwd root
```
把密码改了


### 2 换源

```shell
sudo vim /etc/apt/sources.list
```
改为下面的中科大源.
[https://mirrors.ustc.edu.cn/](https://mirrors.ustc.edu.cn/)   找到ubuntu右面的help链接:
```shell
# 默认注释了源码仓库，如有需要可自行取消注释
deb https://mirrors.ustc.edu.cn/ubuntu/ focal main restricted universe multiverse
# deb-src https://mirrors.ustc.edu.cn/ubuntu/ focal main restricted universe multiverse

deb https://mirrors.ustc.edu.cn/ubuntu/ focal-security main restricted universe multiverse
# deb-src https://mirrors.ustc.edu.cn/ubuntu/ focal-security main restricted universe multiverse

deb https://mirrors.ustc.edu.cn/ubuntu/ focal-updates main restricted universe multiverse
# deb-src https://mirrors.ustc.edu.cn/ubuntu/ focal-updates main restricted universe multiverse

deb https://mirrors.ustc.edu.cn/ubuntu/ focal-backports main restricted universe multiverse
# deb-src https://mirrors.ustc.edu.cn/ubuntu/ focal-backports main restricted universe multiverse

# 预发布软件源，不建议启用
# deb https://mirrors.ustc.edu.cn/ubuntu/ focal-proposed main restricted universe multiverse
# deb-src https://mirrors.ustc.edu.cn/ubuntu/ focal-proposed main restricted universe multiverse
```


### 3 增强功能
```shell
sudo apt-get update
sudo apt-get install virtualbox-guest-dkms
```

### 3 设置共享文件夹


host为win10，在virtualbox上的ubuntu设置共享文件夹 

![image.png](https://cdn.nlark.com/yuque/0/2021/png/22348649/1632712882769-3df6490e-980f-4d08-9860-bdbd99e3b583.png#clientId=u3086d9bb-f24f-4&from=paste&height=483&id=u403aec85&originHeight=545&originWidth=812&originalType=binary&ratio=1&rotation=0&showTitle=false&size=65414&status=done&style=none&taskId=ub6bc4f92-6593-499c-b219-87f75a54de3&title=&width=718.9943237304688)


![](https://cdn.nlark.com/yuque/0/2021/png/22348649/1632712016179-7e2dda4c-337c-4e66-8f85-80d127667e1a.png#clientId=u3086d9bb-f24f-4&from=paste&id=ua3102e06&originHeight=590&originWidth=962&originalType=url&ratio=1&rotation=0&showTitle=false&status=done&style=none&taskId=u49f75501-0a81-46bb-9b6e-c3e5cc2464f&title=)
这么设置好，发现/media/data存在，但是无法进入和访问，只能用root用户访问和sudo查看文件,很不方便,这是因为我们没有权限。执行sudo adduser <user_name> vboxsf，这样把用户添加到vboxsf组,然后就有权限了。
