HPC-X 依赖于 Mellanox OFED 驱动来与 InfiniBand 或 RoCE (RDMA over Converged Ethernet) 网络硬件进行高效通信。
如果您的节点间使用这类高速网络，请务必先安装或确保已正确安装并运行 OFED 驱动


所以**OFED驱动对IB来说至关重要**,不然机器间通信会退化到走TCP

# ubuntu22.04LTS

## 检查
```shell
# 1 检查有没有Mellanox ConnectX 网卡
apt install -y procps pciutils kmod
lspci | grep -i mellanox
# 如果有应该看到类似这样的输出
# 19:00.0 Infiniband controller: Mellanox Technologies MT2910 Family [ConnectX-7]
# 27:00.0 Ethernet controller: Mellanox Technologies MT2892 Family [ConnectX-6 Dx]
# 27:00.1 Ethernet controller: Mellanox Technologies MT2892 Family [ConnectX-6 Dx]
# 3b:00.0 Infiniband controller: Mellanox Technologies MT2910 Family [ConnectX-7]
# 4b:00.0 Infiniband controller: Mellanox Technologies MT2910 Family [ConnectX-7]
# 5c:00.0 Infiniband controller: Mellanox Technologies MT2910 Family [ConnectX-7]
# 9b:00.0 Infiniband controller: Mellanox Technologies MT2910 Family [ConnectX-7]
# bb:00.0 Infiniband controller: Mellanox Technologies MT2910 Family [ConnectX-7]
# ca:00.0 Infiniband controller: Mellanox Technologies MT2910 Family [ConnectX-7]
# da:00.0 Infiniband controller: Mellanox Technologies MT2910 Family [ConnectX-7]

# 2检查有没有RDMA设备
ibstat
# 如果有应该看到类似:
# CA 'mlx5_0'
#         CA type: MT4129
#         Number of ports: 1
#         Firmware version: 28.38.1900
#         Hardware version: 0
#         Node GUID: 0xa088c203000d58e8
#         System image GUID: 0xa088c203000d58e8
#         Port 1:
#                 State: Active
#                 Physical state: LinkUp
#                 Rate: 400
#                 Base lid: 49
#                 LMC: 0
#                 SM lid: 1
#                 Capability mask: 0xa751e848
#                 Port GUID: 0xa088c203000d58e8
#                 Link layer: InfiniBand
# CA 'mlx5_3'
#         CA type: MT4129
#         Number of ports: 1
#         Firmware version: 28.38.1900
#         Hardware version: 0
#         Node GUID: 0x946dae0300d776d0
#         System image GUID: 0x946dae0300d776d0
#         Port 1:
#                 State: Active
#                 Physical state: LinkUp
#                 Rate: 400
#                 Base lid: 42
#                 LMC: 0
#                 SM lid: 1
#                 Capability mask: 0xa751e848
#                 Port GUID: 0x946dae0300d776d0
#                 Link layer: InfiniBand
# CA 'mlx5_4'
#         CA type: MT4129
#         Number of ports: 1
#         Firmware version: 28.38.1900
#         Hardware version: 0
#         Node GUID: 0x946dae0300d77598
#         System image GUID: 0x946dae0300d77598
#         Port 1:
#                 State: Active
#                 Physical state: LinkUp
#                 Rate: 400
#                 Base lid: 35
#                 LMC: 0
#                 SM lid: 1
#                 Capability mask: 0xa751e848
#                 Port GUID: 0x946dae0300d77598
#                 Link layer: InfiniBand
# CA 'mlx5_5'
#         CA type: MT4129
#         Number of ports: 1
#         Firmware version: 28.38.1900
#         Hardware version: 0
#         Node GUID: 0xa088c203000d40c0
#         System image GUID: 0xa088c203000d40c0
#         Port 1:
#                 State: Active
#                 Physical state: LinkUp
#                 Rate: 400
#                 Base lid: 39
#                 LMC: 0
#                 SM lid: 1
#                 Capability mask: 0xa751e848
#                 Port GUID: 0xa088c203000d40c0
#                 Link layer: InfiniBand
# CA 'mlx5_6'
#         CA type: MT4129
#         Number of ports: 1
#         Firmware version: 28.38.1900
#         Hardware version: 0
#         Node GUID: 0xa088c203000d58e0
#         System image GUID: 0xa088c203000d58e0
#         Port 1:
#                 State: Active
#                 Physical state: LinkUp
#                 Rate: 400
#                 Base lid: 47
#                 LMC: 0
#                 SM lid: 1
#                 Capability mask: 0xa751e848
#                 Port GUID: 0xa088c203000d58e0
#                 Link layer: InfiniBand
# CA 'mlx5_7'
#         CA type: MT4129
#         Number of ports: 1
#         Firmware version: 28.38.1900
#         Hardware version: 0
#         Node GUID: 0xa088c203000d3740
#         System image GUID: 0xa088c203000d3740
#         Port 1:
#                 State: Active
#                 Physical state: LinkUp
#                 Rate: 400
#                 Base lid: 14
#                 LMC: 0
#                 SM lid: 1
#                 Capability mask: 0xa751e848
#                 Port GUID: 0xa088c203000d3740
#                 Link layer: InfiniBand
# CA 'mlx5_8'
#         CA type: MT4129
#         Number of ports: 1
#         Firmware version: 28.38.1900
#         Hardware version: 0
#         Node GUID: 0x946dae0300d776e0
#         System image GUID: 0x946dae0300d776e0
#         Port 1:
#                 State: Active
#                 Physical state: LinkUp
#                 Rate: 400
#                 Base lid: 48
#                 LMC: 0
#                 SM lid: 1
#                 Capability mask: 0xa751e848
#                 Port GUID: 0x946dae0300d776e0
#                 Link layer: InfiniBand
# CA 'mlx5_9'
#         CA type: MT4129
#         Number of ports: 1
#         Firmware version: 28.38.1900
#         Hardware version: 0
#         Node GUID: 0x946dae0300d77178
#         System image GUID: 0x946dae0300d77178
#         Port 1:
#                 State: Active
#                 Physical state: LinkUp
#                 Rate: 400
#                 Base lid: 24
#                 LMC: 0
#                 SM lid: 1
#                 Capability mask: 0xa751e848
#                 Port GUID: 0x946dae0300d77178
#                 Link layer: InfiniBand
# CA 'mlx5_bond_0'
#         CA type: MT4125
#         Number of ports: 1
#         Firmware version: 22.38.1900
#         Hardware version: 0
#         Node GUID: 0xb8cef60300cc2ba6
#         System image GUID: 0xb8cef60300cc2ba6
#         Port 1:
#                 State: Active
#                 Physical state: LinkUp
#                 Rate: 100
#                 Base lid: 0
#                 LMC: 0
#                 SM lid: 0
#                 Capability mask: 0x00010000
#                 Port GUID: 0x4c1b6cfffeb8d220
#                 Link layer: Ethernet


# 3 检查内核模块
lsmod | grep -E "mlx5_core|mlx5_ib|ib_core|ib_uverbs"
# 如果看到这些模块被列出：说明相应的内核驱动模块已经加载

# 4 检查网络接口
# 查看是否有 ibX 接口，或者你的 RoCE 以太网接口是否处于 UP 状态。
ifconfig -a
# 如果有ib，输出会包含如下(每张卡上一个)
# ib0: flags=4098<BROADCAST,MULTICAST>  mtu 4092
#         unspec 00-00-10-49-FE-80-00-00-00-00-00-00-00-00-00-00  txqueuelen 256  (UNSPEC)
#         RX packets 0  bytes 0 (0.0 B)
#         RX errors 0  dropped 0  overruns 0  frame 0
#         TX packets 0  bytes 0 (0.0 B)
#         TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
# ib1: flags=4098<BROADCAST,MULTICAST>  mtu 4092
#         unspec 00-00-10-49-FE-80-00-00-00-00-00-00-00-00-00-00  txqueuelen 256  (UNSPEC)
#         RX packets 0  bytes 0 (0.0 B)
#         RX errors 0  dropped 0  overruns 0  frame 0
#         TX packets 0  bytes 0 (0.0 B)
#         TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
# ib2: flags=4098<BROADCAST,MULTICAST>  mtu 4092
#         unspec 00-00-10-49-FE-80-00-00-00-00-00-00-00-00-00-00  txqueuelen 256  (UNSPEC)
#         RX packets 0  bytes 0 (0.0 B)
#         RX errors 0  dropped 0  overruns 0  frame 0
#         TX packets 0  bytes 0 (0.0 B)
#         TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
# ib3: flags=4098<BROADCAST,MULTICAST>  mtu 4092
#         unspec 00-00-10-49-FE-80-00-00-00-00-00-00-00-00-00-00  txqueuelen 256  (UNSPEC)
#         RX packets 0  bytes 0 (0.0 B)
#         RX errors 0  dropped 0  overruns 0  frame 0
#         TX packets 0  bytes 0 (0.0 B)
#         TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
# ib4: flags=4098<BROADCAST,MULTICAST>  mtu 4092
#         unspec 00-00-10-49-FE-80-00-00-00-00-00-00-00-00-00-00  txqueuelen 256  (UNSPEC)
#         RX packets 0  bytes 0 (0.0 B)
#         RX errors 0  dropped 0  overruns 0  frame 0
#         TX packets 0  bytes 0 (0.0 B)
#         TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
# ib5: flags=4098<BROADCAST,MULTICAST>  mtu 4092
#         unspec 00-00-10-49-FE-80-00-00-00-00-00-00-00-00-00-00  txqueuelen 256  (UNSPEC)
#         RX packets 0  bytes 0 (0.0 B)
#         RX errors 0  dropped 0  overruns 0  frame 0
#         TX packets 0  bytes 0 (0.0 B)
#         TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
# ib6: flags=4098<BROADCAST,MULTICAST>  mtu 4092
#         unspec 00-00-10-49-FE-80-00-00-00-00-00-00-00-00-00-00  txqueuelen 256  (UNSPEC)
#         RX packets 0  bytes 0 (0.0 B)
#         RX errors 0  dropped 0  overruns 0  frame 0
#         TX packets 0  bytes 0 (0.0 B)
#         TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
# ib7: flags=4098<BROADCAST,MULTICAST>  mtu 4092
#         unspec 00-00-10-49-FE-80-00-00-00-00-00-00-00-00-00-00  txqueuelen 256  (UNSPEC)
#         RX packets 0  bytes 0 (0.0 B)
#         RX errors 0  dropped 0  overruns 0  frame 0
#         TX packets 0  bytes 0 (0.0 B)
#         TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

# 5 检查/sys/class/infiniband 目录
ls /sys/class/infiniband/
# mlx5_0  mlx5_3  mlx5_4  mlx5_5  mlx5_6  mlx5_7  mlx5_8  mlx5_9  mlx5_bond_0
# 如果这个目录存在并且里面有内容（例如 mlx5_0, mlx5_1 等），这通常表明 InfiniBand 内核子系统已经识别了你的硬件

```


## ofed 驱动安装
若没有ofed驱动，得装
下载DOCA_OFED地址: https://developer.nvidia.com/doca-downloads?deployment_platform=Host-Server  (Deployment Package选DOCA-Host)
参考安装方法(在目标网页里选好安装包后会有)：
```
wget https://www.mellanox.com/downloads/DOCA/DOCA_v3.0.0/host/doca-host_3.0.0-058000-25.04-ubuntu2204_amd64.deb
sudo dpkg -i doca-host_3.0.0-058000-25.04-ubuntu2204_amd64.deb
sudo apt-get update

# 如果下面报错说依赖的mft版本过低，参考:  apt-get install mft=4.32.0-120
sudo apt-get -y install doca-ofed

# 检查
ofed_info
```

## hpcx安装

1. 在这找hpc-x版本
https://docs.nvidia.com/networking/software/accelerator-software/index.html
2. 进入对应版本的页面，点击Installing and Loading HPC-X，里面有具体安装方法，我的:
```shell
cd /opt/hpcx # 假如有这个目录，里面有下面这个包
tar -xvf hpcx-v2.21.2-gcc-doca_ofed-ubuntu22.04-cuda12-x86_64.tbz

# 临时生效 (当前终端)
source /opt/hpcx/hpcx-v2.21.2-gcc-doca_ofed-ubuntu22.04-cuda12-x86_64/hpcx-init.sh
hpcx_load  # 加载默认的 HPC-X 配置

# 或者，为了永久生效 (推荐)，将其添加到 .bashrc:
echo 'source /opt/hpcx/hpcx-v2.21.2-gcc-doca_ofed-ubuntu22.04-cuda12-x86_64/hpcx-init.sh' >> ~/.bashrc
echo 'hpcx_load' >> ~/.bashrc # 或者根据需要选择特定配置加载
source ~/.bashrc
```


# 对比

无hpc-x (GB/s):
```text
Bandwidth between Node0 and Node1:
        Node1_GPU0  Node1_GPU1  Node1_GPU2  Node1_GPU3  Node1_GPU4  Node1_GPU5  Node1_GPU6  Node1_GPU7 
Node0_GPU0:   0.42   4.79   1.85   4.12   2.77   0.20   0.52   2.89
Node0_GPU1:   4.77   4.73   4.26   4.45   0.40   2.80   2.84   2.88
Node0_GPU2:   0.87   4.85   4.75   4.90   0.39   0.78   0.16   0.29
Node0_GPU3:   0.36   4.88   0.33   0.56   0.45   0.40   2.93   2.78
Node0_GPU4:   4.08   3.91   4.24   4.11   0.64   2.96   1.04   0.63
Node0_GPU5:   3.82   3.82   0.36   3.92   0.21   2.80   0.63   1.02
Node0_GPU6:   3.98   3.99   4.81   3.87   2.94   2.97   2.85   2.82
Node0_GPU7:   4.12   4.03   0.15   3.79   2.93   3.00   2.79   2.77
```


有doca_ofed + hpc-x  (GB/s):
```text
Bandwidth between Node0 and Node1:
        Node1_GPU0  Node1_GPU1  Node1_GPU2  Node1_GPU3  Node1_GPU4  Node1_GPU5  Node1_GPU6  Node1_GPU7 
Node0_GPU0:  31.23  33.13  31.51  32.65  27.52  26.09  26.28  28.13
Node0_GPU1:  32.46  32.32  33.32  33.38  26.76  27.32  27.59  28.62
Node0_GPU2:  32.73  33.41  32.59  31.71  27.01  25.79  26.78  28.22
Node0_GPU3:  32.94  33.93  32.95  32.49  26.85  28.33  27.96  27.27
Node0_GPU4:  27.26  26.26  26.73  27.80  33.03  33.93  32.97  32.31
Node0_GPU5:  27.37  28.41  27.65  26.80  33.56  32.77  32.85  31.61
Node0_GPU6:  28.34  28.94  28.96  27.55  33.45  32.88  34.41  34.30
Node0_GPU7:  26.76  26.71  27.56  25.86  32.26  32.73  32.63  32.37
```