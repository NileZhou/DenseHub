# VMware安装与破解
vmware 安装包: 
见百度网盘vmware workstation 16 full

vmware 破解码:
```shell
VMware Workstation Pro 16.x Serials

YA7RA-F6Y46-H889Z-LZMXZ-WF8UA
ZV7HR-4YX17-M80EP-JDMQG-PF0RF
UC3XK-8DD1J-089NP-MYPXT-QGU80
GV100-84W16-M85JP-WXZ7E-ZP2R6
YF5X2-8MW91-4888Y-DNWGC-W68TF
AY1XK-0NG5P-0855Y-K6ZXG-YK0T4

VMware Workstation Player 16.x Serials

FC3D0-FTFE5-H81WQ-RNWZX-PV894
AU3TA-8VFDP-08DUZ-VMM7X-YK8GF
ZF3XK-22F5K-M88AQ-ZMWQV-QCRGA
FF718-6JDEK-M8DRQ-FNWEX-QG2X4
ZA3DA-43Z9J-089TQ-36N5V-NLHEF
YY19A-6TX94-H88KQ-4NNXG-XAUF6
```


# 三种网络模式

![image.png](../../../../_imgs/3_network_mode.png)

## NAT
Network Address translation
所有的虚拟机构成一个局域网，这个局域网的网关(网络的出口)是宿主机，所以上网时和宿主机用的是同样的网络标识

![](https://cdn.nlark.com/yuque/0/2022/png/22348649/1641377138583-1d8733fa-6445-4217-8c79-2e9adbc98adc.png#clientId=uefce15da-fd31-4&from=paste&id=u9f69c365&originHeight=370&originWidth=588&originalType=url&ratio=1&rotation=0&showTitle=false&status=done&style=none&taskId=ud97438b5-11cb-40e6-a17f-809eeab2591&title=)


## Bridge
虚拟机和宿主机不是主从关系，上网使用宿主机通道，有自己的网络标识
![](https://cdn.nlark.com/yuque/0/2022/png/22348649/1641377110006-0119be6e-e0eb-429f-a47a-12c47650cfb5.png#clientId=uefce15da-fd31-4&from=paste&id=u4f3b60c9&originHeight=281&originWidth=561&originalType=url&ratio=1&rotation=0&showTitle=false&status=done&style=none&taskId=u9abf2719-f8a3-475d-b5fc-522aa707594&title=)


## Host-only

![](https://cdn.nlark.com/yuque/0/2022/png/22348649/1641377123838-47ef76c1-0818-4763-a726-41386d9d6525.png#clientId=uefce15da-fd31-4&from=paste&id=ue59e29df&originHeight=261&originWidth=566&originalType=url&ratio=1&rotation=0&showTitle=false&status=done&style=none&taskId=u696c311e-ca58-4a7f-8b06-0e73ccc9e22&title=)

# NAT模式设置静态ip

前提: 先关闭虚拟机

## 修改网络模式为NAT

点击虚拟机 -> 右键 -> 设置
![image.png](https://cdn.nlark.com/yuque/0/2022/png/22348649/1641619015770-7efc4587-c5f7-4fd3-aa44-c1cd6ac0b7b4.png#clientId=u4e6fde5a-61bd-4&from=paste&height=303&id=u095d9f50&originHeight=605&originWidth=1090&originalType=binary&ratio=1&rotation=0&showTitle=false&size=56514&status=done&style=none&taskId=ua94a1884-3c6b-4c64-9ae0-d60bd222b43&title=&width=545)
修改网络适配器为NAT模式或自定义中的NAT模式

![image.png](https://cdn.nlark.com/yuque/0/2022/png/22348649/1641619103922-3c47363c-8f05-4745-b5c2-dc50a1276300.png#clientId=u4e6fde5a-61bd-4&from=paste&height=331&id=uf876f8f5&originHeight=662&originWidth=861&originalType=binary&ratio=1&rotation=0&showTitle=false&size=40151&status=done&style=none&taskId=u431345cb-7a35-490b-9b64-a7532487dd7&title=&width=430.5)

## 创建虚拟网络

打开虚拟网络编辑器，进行虚拟子网创建
![image.png](https://cdn.nlark.com/yuque/0/2022/png/22348649/1641619169937-89fea88b-53aa-4809-b53d-63e6db599f24.png#clientId=u4e6fde5a-61bd-4&from=paste&height=303&id=u6b4ca74e&originHeight=605&originWidth=1095&originalType=binary&ratio=1&rotation=0&showTitle=false&size=64857&status=done&style=none&taskId=u2a1b4334-7471-4e2b-8eb7-ce36d43e489&title=&width=547.5)
点击VMnet8，点击【更改设置】，取消【使用本地DHCP服务器IP地址】前面的勾
![image.png](https://cdn.nlark.com/yuque/0/2022/png/22348649/1641619229137-7e0d5397-b8ba-417a-a5fc-4e12ab1f0c59.png#clientId=u4e6fde5a-61bd-4&from=paste&height=350&id=u392e171d&originHeight=700&originWidth=713&originalType=binary&ratio=1&rotation=0&showTitle=false&size=42204&status=done&style=none&taskId=u507b93ef-9307-4f10-ba27-cfc6b305608&title=&width=356.5)
再分配IP地址
![image.png](https://cdn.nlark.com/yuque/0/2022/png/22348649/1641619342163-7aa3e24c-2f54-457d-a55a-52c601377aa8.png#clientId=u4e6fde5a-61bd-4&from=paste&height=334&id=u0d90f98a&originHeight=667&originWidth=708&originalType=binary&ratio=1&rotation=0&showTitle=false&size=37229&status=done&style=none&taskId=ub9edb0ee-6c86-4453-8358-f19ab7bcdf5&title=&width=354)
这里的子网IP最后是 ".0" 结尾，代表分配了一个网段，结合子网掩码进行计算。
子网网段尽量和主机的IP网段不同
记住这个子网IP网段(192.168.80.0)和子网掩码(255.255.255.0)，待会会用到

再点击【NAT设置】
![image.png](https://cdn.nlark.com/yuque/0/2022/png/22348649/1641619482372-b0b50dc8-611a-479b-9193-e70fead627c3.png#clientId=u4e6fde5a-61bd-4&from=paste&height=328&id=u423dedf4&originHeight=655&originWidth=707&originalType=binary&ratio=1&rotation=0&showTitle=false&size=36362&status=done&style=none&taskId=u03de3189-b7c8-42e6-80bd-40e6a2fb4f3&title=&width=353.5)
设置网关，这个网关必须在刚才创建的子网下，但不能和待会要设置的虚拟机IP地址相同
![image.png](https://cdn.nlark.com/yuque/0/2022/png/22348649/1641619548401-33b7187f-c95d-4a14-8ba8-6bda73a76a76.png#clientId=u4e6fde5a-61bd-4&from=paste&height=324&id=u340313c0&originHeight=647&originWidth=572&originalType=binary&ratio=1&rotation=0&showTitle=false&size=23987&status=done&style=none&taskId=u009f3c1a-6de2-489e-9c01-7163bcc82da&title=&width=286)
然后一路点击确定

## 修改虚拟机中CentOS的网络配置
打开虚拟机CentOS，去修改网络配置文件:
```shell
cd /etc/sysconfig/network-scripts # 进入配置目录
sudo vi ifcfg-eno16777736  # 系统不一样，网卡名称也不一样
```
修改如下字段:
```shell
BOOTPROTO=static
ONBOOT=yes
IPADDR=192.168.80.12  #需要和设置的IP段统一，这里192.168.80.12在192.168.80.0(掩码255.255.255.0)的网段下
NETMASK=255.255.255.0  # 照着刚才设置的填
GATEWAY=192.168.80.2  # 需要和vmware虚拟网卡设置的网关一致，不能和IPADDR相同
DNS1=192.168.100.1  # 通过ipconfig(win10)查看宿主机的DNS，否则会导致能ping通外部IP，不通外部域名
```
注意; 这里的DNS如何查看:
在宿主机(win10上):
![image.png](https://cdn.nlark.com/yuque/0/2022/png/22348649/1641620101629-1862f2e4-13c9-4ca2-8a6f-d46318f5255a.png#clientId=u4e6fde5a-61bd-4&from=paste&height=318&id=u3a5e155e&originHeight=636&originWidth=1002&originalType=binary&ratio=1&rotation=0&showTitle=false&size=80314&status=done&style=none&taskId=u2105e930-3a90-4f17-80a2-f56fd6b251f&title=&width=501)
因为我现在连的是WIFI，所以查看无线局域网WLAN的配置，可以看到默认网关，那么这就是我们要找的DNS
如果是连接的有线网，应该去找以太网适配器 以太网中的DNS地址

配置文件更改后，重启网络:
```shell
sudo systemctl restart network
```
## 测试
测试下是否大功告成:
用sudo reboot重启，再ifconfig查看是否为设置好的IP地址
ping www.baidu.com，看是否能ping通

# 解决: NAT下Host ping不通Guest
问题描述: Guest能ping Host与Internet主机，Host ping 不通 Guest

更改VMnet8网卡设置
右键网络  ->   点击【打开"网络"和Internet设置】 -> 点击【更改适配器选项】
![image.png](https://cdn.nlark.com/yuque/0/2022/png/22348649/1641621773483-edbf74ea-cf5a-4411-9206-2bdaba07d961.png#clientId=u4e6fde5a-61bd-4&from=paste&height=538&id=u2afb759e&originHeight=1075&originWidth=1205&originalType=binary&ratio=1&rotation=0&showTitle=false&size=124957&status=done&style=none&taskId=uc07d65a3-f684-4f9d-92e5-f3d5a09619d&title=&width=602.5)
点击VMnet8，再点击【属性】
![image.png](https://cdn.nlark.com/yuque/0/2022/png/22348649/1641621884590-abc68ff3-145f-45cd-8dc8-21811b3a8637.png#clientId=u4e6fde5a-61bd-4&from=paste&height=301&id=u729f1a6e&originHeight=601&originWidth=1402&originalType=binary&ratio=1&rotation=0&showTitle=false&size=75663&status=done&style=none&taskId=ud5a2fcf6-3adc-4965-b424-e75e208a438&title=&width=701)
点击【Internet协议版本4】 -> 点击【属性】，在弹出窗口里点击【使用下面的IP地址】
填入IP地址与子网掩码:
在设置的虚拟机网段里(我的是192.168.80.0(255.255.255.0))，再新分配一个主机地址(注意不要和Guest的IP一样)，这里我随便分配了个192.168.80.10(255.255.255.0)

## ![image.png](https://cdn.nlark.com/yuque/0/2022/png/22348649/1641623783229-6878047c-a2d3-41c7-9149-1ed705056a4f.png#clientId=u4e6fde5a-61bd-4&from=paste&height=372&id=u3685d356&originHeight=744&originWidth=1111&originalType=binary&ratio=1&rotation=0&showTitle=false&size=235125&status=done&style=none&taskId=u86a1d299-10c9-4343-aacf-6c9398e1541&title=&width=555.5)
一路点击确定即可

运维结果验证:
在Host里Ping Guest的IP试试
