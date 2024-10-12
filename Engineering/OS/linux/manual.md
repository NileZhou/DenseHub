[TOC]



# 基础操作手册

Linux下各种解决问题的命令、工具  很值得一学:

[https://linuxtools-rst.readthedocs.io/zh_CN/latest/tool/gdb.html](https://linuxtools-rst.readthedocs.io/zh_CN/latest/tool/gdb.html)

Linux下开发常用命令:

[https://www.yanbinghu.com/2018/09/26/61877.html](https://www.yanbinghu.com/2018/09/26/61877.html)

# 文件/IO管理

UNIX的哲学: 一切皆文件

## 目录结构FHS

**Filesystem Hierarchy Standard (FHS)** : 文件系统结构层次，是一种描述UNIX操作系统布局的参考，由Linux基金会维护，目前版本是2015年发布的3.0

| **目录**                                                     | **描述**                                                     |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| /                                                            | 根目录                                                       |
| /bin                                                         | 一些必要的二进制程序，必须是单用户模式下可用的，包含可用来修复系统的命令如cat, ls, cp等 |
| /boot                                                        | bootloader文件，也叫启动引导程序，如                         |
| [kernels](https://en.wikipedia.org/wiki/Kernel_(operating_system)), [initrd](https://en.wikipedia.org/wiki/Initrd) |                                                              |
| /dev                                                         | 设备文件，如磁盘等设备                                       |
| /etc                                                         | 放全局范围的配置文件，全称为"Editable Text Configuration" 或 "Extended Tool Chest"。 |

此外还可能有
• /etc/opt: 存在/opt中的插件包的配置
• /etc/sgml: 处理SGML的程序的配置
• /etc/X11: X Window System, version 11的配置
• /etc/xml: 处理XML程序的配置 |
| /home | 用户个人目录，包含用户保存的文件、用户个人设置等 |
| /lib<qual>:

/lib
/lib64 (可能有) | /bin和/sbin的二进制程序所使用到的库文件 |
| /media | 可移除的媒体设备(如CD-ROMS)的挂载点 |
| /mnt | 临时被挂载的文件系统 |
| /opt | 存放插件类应用软件(optional可选应用包，一般是直接提供二进制程序的非开源包) |
| /proc | 虚拟文件系统，以文件的形式提供了进程和内核的信息。Linux中对应procfs挂载点，其中内容通常是被系统运行中自动生成的。系统版本信息在/proc/version |
| /root | root用户的家目录 |
| /run | 从最近一次启动开始记录的，运行时不断变化的数据，如当前登录用户，运行中的后台进程，pid，socket文件 |
| /sbin | 非常关键且必要的系统可执行文件(system binaries)，如fsck、init、route |
| /srv | 网站相关的数据(site-specific data)，如web服务器的数据、脚本、FTP服务器传输过来的数据，版本控制系统的版本库(repository) |
| /sys | 包含设备、驱动、一些kernel特性相关的信息 |
| /tmp | 临时文件目录，类似地有/var/tmp，通常系统重启就没有了，且大小受到严格限制 |
| /usr | Unix Software Resource，绝大多数的程序和应用工具(多用户共享的、只读的)都是放在这里的，结构和/比较相似，本地数据的第二级(按顺序的第二种选择) |
| /usr/bin | 所有用户共享的、非必须的二进制命令程序(单用户模式用不到) |
| /usr/include | 放置include头文件 |
| /usr/lib<qual> | /usr/bin和/usr/sbin的程序用到的库文件 |
| /usr/local | 本地数据的第三级(按顺序的第三种选择)，特定于主机的，往往有其它子目录如bin, lib, share |
| /usr/sbin | 非必要的系统二进制程序(如多样的网络服务的后台程序) |
| /usr/share | 和计算机架构无关的共享资源文件 |
| /usr/src | 源码，如kernel的源码 |
| /var | 可变文件: 系统运行中内容不断变化(variable)的文件，如日志、临时email文件 |
| /var/cache | 应用的缓存数据，用来加速应用的耗时I/O与计算的，就算被删除也不会真的丢数据 |
| /var/lib | 持久化状态，应用程序的持久化数据如数据库、包管理系统（如/var/lib/dpkg）的元信息等 |
| /var/lock | 锁文件，给设备或多个应用都能访问的资源进行加锁，命名一般以LCK....开头 |
| /var/log | 存日志文件，常用: /var/log/kernel、/var/log/cron、/var/log/boot.log等 |
| /var/email | 邮箱，有些发行版把邮件存到/var/spool/mail |
| /var/opt | 存在/opt中的插件程序产生的变化的数据 |
| /var/run | 运行时的变化数据，包含了从开机开始的系统信息 |
| /var/tmp | 开机->重启，系统运行时产生的临时文件 |

## 查看/找文件内容

| 命令 | 说明                                                         |
| ---- | ------------------------------------------------------------ |
| cat  | 一次性将文件内容输出到terminal，可将多个文件连接起来显示，常与重定向符配合使用，适用于文件内容少的情况 |
| more | 可显示文件内容超过一屏的内容，可翻页     空格显示下一页，按b显示上一页 |
| less | 可显示文件内容超过一屏的内容，可翻页，跳转，查找    空格显示下一页，按b显示上一页 |
| head | 查看文件内容的头部几行      head -n 5 file   # 查看file中头5行 |
| tail | 查看文件内容的尾部几行      head -n 5 file   # 查看file中尾5行 |
| grep | 查找文件内容中匹配表达式的某些行                             |

sheet:

```
# 单文件

# grep
cat file | grep '要匹配的字符串'-A 5     # 显示文件file里字符串出现的那行及其后5行
cat file | grep '要匹配的字符串'-B 5     # 显示文件file里字符串出现的那行及其前5行
cat file | grep '要匹配的字符串' -C 5    # 显示文件file里字符串出现的那行及其周围5行
cat file | grep '模式串' -c             # 输出在文件中匹配成功了几行 -c 即为 --count

# 多文件

# -n 代表输出这个字符串在哪个文件的哪一行
# -r 代表递归搜索目标目录(可以是相对路径也可以是绝对路径)
# --color代表将匹配到的字符串进行
grep -nr "这里写正则表达式" <目标目录> --color

# 在/home/xiaoju/logs文件夹下先【排除, -v】带blocConsumer的文件，再在文件里查找带目标串的行
grep 目标字符串 -n $(ls /home/xiaoju/logs/ | grep -v blocConsumer)

# 只列出哪些文件包含这个模式串
grep -lr  <模式串>  <目标目录>

# 查看某个文件存不存在，文本文件的话直接打开:
open -e <file_path>
```

## IO重定向

| 命令                                        | 说明                                         |
| ------------------------------------------- | -------------------------------------------- |
| ${cmd} > file                               |                                              |
| ${cmd} >> file                              |                                              |
| ${cmd} < file                               | 将命令的输出重定向到file                     |
| 将命令的输出以追加的方式重定向到file        |                                              |
| 将命令的输入重定向到file                    |                                              |
| n > file                                    |                                              |
| n >> file                                   | 将文件描述符为n的文件重定向到file            |
| 将文件描述符为n的文件以追加方式重定向到file |                                              |
| n >& m                                      |                                              |
| n < & m                                     | 将输出文件m和n合并                           |
| 将输入文件m和n合并                          |                                              |
| << tag                                      | 将开始标记tag和结束标记tag之间的内容作为输出 |

# 注: man手册

| Section/章节 | 说明                   |
| ------------ | ---------------------- |
| 1            | 一般命令               |
| 2            | 系统调用               |
| 3            | 库函数                 |
| 4            | 特殊文件和驱动程序     |
| 5            | 文件格式约定           |
| 6            | 游戏和屏保             |
| 7            | 杂项                   |
| 8            | 系统管理命令和守护进程 |

# 权限管理

递归更改某个目录的权限:

```
chmod -R 775 <目标目录>
```

# 服务

# 服务管理

![https://cdn.nlark.com/yuque/0/2022/png/22348649/1648644905211-98454f89-3810-40b9-a09f-fa364de8d74b.png](https://cdn.nlark.com/yuque/0/2022/png/22348649/1648644905211-98454f89-3810-40b9-a09f-fa364de8d74b.png)

## systemctl

- systemctl status <服务> : 查看服务状态
- systemctl start <服务> : 启动某个服务
- systemctl stop <服务>: 停止某个服务
- systemctl enable <服务> : 设置某个服务开机自启
- systemctl disable <服务> : 移除某个服务开机自启
- systemctl restart <服务>: 重启某个服务

Systemctl: 一个systemd工具，主要负责控制systemd系统和服务管理器。

Systemd: 一个系统管理守护进程、工具和库的集合，用于取代System V初始进程。Systemd的功能是用于集中管理和配置类UNIX系统。在Linux生态系统中，Systemd被部署到了大多数的标准Linux发行版中，只有为数不多的几个发行版尚未部署。Systemd通常是所有其它守护进程的父进程，但并非总是如此。

## journalctl

journalctl -u sshd.service    # 查看ssh的日志(system)

systemd提供了自己的日志系统（logging system），称为 journal

## 过时的命令

init: init始终是第一个进程（其进程编号始终为1）。

内核会在过去曾使用过init的几个地方查找它，它的正确位置（对Linux系统来说）是/sbin/init。如果内核找不到init，它就会试着运行/bin/sh，如果运行失败，系统的启动也会失败

service: 在[Centos7](https://so.csdn.net/so/search?q=Centos7&spm=1001.2101.3001.7020).0之后，linux系统不再使用service命令进行服务管理，转而使用systemctl

# cron表达式

cron在Unix系统上是一个很基础的定时任务工具

定时任务，日志在/var/log/cron        [参考](https://www.jianshu.com/p/1e3b4bb75044)

cron表达式格式:

{秒} {分} {时} {日} {月} {星期} {年 (可为空) }        所以看到cron表达式先看它有6个域还是7个域

| **域** | **是否必需** | **取值范围**                                                 | **特殊字符**  |
| ------ | ------------ | ------------------------------------------------------------ | ------------- |
| 秒     | 是           | [0, 59]                                                      | * , - /       |
| 分钟   | 是           | [0, 59]                                                      | * , - /       |
| 小时   | 是           | [0, 23]                                                      | * , - /       |
| 日期   | 是           | [1, 31]                                                      | * , - / ? L W |
| 月份   | 是           | [1, 12]或[JAN, DEC]                                          | * , - /       |
| 星期   | 是           | [1, 7]或[MON, SUN]。若您使用[1, 7]表达方式，**1**代表星期一，**7**代表星期日。 | * , - / ? L # |
| 年     | 否           | [当前年份，2099]                                             | * , - /       |

特殊字符:

Cron表达式中的每个域都支持一定数量的特殊字符，每个特殊字符有其特殊含义。

| **特殊字符** | **含义**                                     | **示例**                                                     |
| ------------ | -------------------------------------------- | ------------------------------------------------------------ |
| *****        | 所有可能值                                   | 在月域中，*****表示每个月；在星期域中，*****表示星期的每一天。 |
| **,**        | 列出枚举值                                   | 在分钟域中，**5,20**表示分别在5分钟和20分钟触发一次。        |
| **-**        | 范围                                         | 在分钟域中，**5-20**表示从5分钟到20分钟之间每隔一分钟触发一次。 |
| **/**        | 指定数值的增量                               | 在分钟域中，**3/20**表示从第3分钟开始，每20分钟。            |
| **?**        | 不指定值，仅日期和星期域支持该字符           | 当日期或星期域其中之一被指定了值以后，为避免冲突，需要将另一个域的值设为 **?** |
| **L**        | 表示最后一天(Last)，仅日期和星期域支持该字符 |                                                              |

**注: 指定L字符时，避免指定列表或范围，否则会导致逻辑问题**
 | • 在日期域中，**L**表示某个月的最后一天。在星期域中，**L**表示一个星期的最后一天，也就是星期日（**SUN**）。
• 如果在**L**前有具体的内容，例如，在星期域中的**6L**表示这个月的最后一个星期六 |
| **W** | 工作日(weekday)，在离指定日期的最近的有效工作日触发事件。**W**字符寻找最近有效工作日时不会跨过当前月份，连用字符**LW**时表示为指定月份的最后一个工作日 | 在日期域中**5W**，如果5日是星期六，则将在最近的工作日星期五，即4日触发。如果5日是星期天，则将在最近的工作日星期一，即6日触发；如果5日在星期一到星期五中的一天，则就在5日触发。 |
| **#** | 确定每个月第几个星期几，仅星期域支持 | 在星期域中，**4#2**表示某月的第二个星期四。 |

踩过的坑:   **注意'*'和某个具体数如'0'的区别** !    比如:

```
# 每天执行一次，执行时间为00:00:00
0 0 0 1/1 * ? *

# 每秒执行一次
* * * 1/1 * ? *
```

crontab使用：

```
crontab -e # 编辑定时任务，选择vim编辑一个文件

# 注意以下都是脚本的全路径
# * * * * * 依次是分钟／小时／日／月／星期 执行命令
# 30 8,10-15/2,22 * * * /usr/local/bin/python3 /test/hello.py 这代表每天 8:30 10到15点每两小时的30 22:30执行任务，用“，”表示和，“-”表示至，“／”表示每隔
# 表示每2分钟执行一次hello.py，注意不能是python xxx，要用 /usr/bin/python (which python查看) <pythonfile>
*/2 * * * *  /usr/bin/python3 /test/hello.py
```

wq保存即可

其它命令:

```
tail -f /var/log/cron 追踪查看crontab日志 -f后可添加行数 如 tail -f -n 20 /var/log/cron
```

# SSH

# 

![https://cdn.nlark.com/yuque/0/2022/png/22348649/1648387442853-cee9745d-cf74-4ca0-b463-8c72c57e5b94.png](https://cdn.nlark.com/yuque/0/2022/png/22348649/1648387442853-cee9745d-cf74-4ca0-b463-8c72c57e5b94.png)

## SSH保持长时间连接

情形：ssh连接老是自己会断，一段时间不理它就会失去响应

解决：在/etc/ssh/ssh_config文件里加两个参数

```
#保持连接
TCPKeepAlive yes
#每过5分钟发一个数据包到服务器表示“我还活着”
ServerAliveInterval 300
```

# 进程管理

## pstree 打印进程树

```
pstree
```

## strace 追踪系统调用

strace是一个Linux下的工作在用户态的工具，可以用来监控进程与Linux内核之间的交互，包括系统调用，信号传递，进程状态的改变

```
# 先拿到pid，然后查看syscall是否合理:
strace -p <master pid> -f

# 如果服务甚至启动不了，那么这样做:
strace -f python server.py 或者 strace -f start.sh
```

strace基本是个万金油，比如unixsocket的场景下，tcpdump抓不到，strace就可以。

# 服务管理

# systemctl

systemctl 是 Linux 的 systemd 系统和service manager的一部分。对于使用 systemd 的 Linux 发行版，如 Ubuntu，CentOS 和 Debian，它提供了一种标准的服务管理方式（包括自定义脚本）

可以把一个脚本或程序作为服务管理起来、enable, disable, stop, start, restart等，甚至开机自启

```
# 创建一个 systemd 服务文件：
# systemd 服务文件是一个配置文件，告诉 systemd 如何管理服务。
# 需要在 /etc/systemd/system 目录中为脚本创建一个新的服务文件。
# 此文件应以 .service 结尾
$ sudo nano /etc/systemd/system/<serviceName>.service

# 编写服务文件：在服务文件中，为脚本定义一个新的服务。这可能是这样的：
# [Unit]
# Description=我的自定义脚本

# [Service]
# ExecStart=/path/to/my_script.sh

# [Install]
# WantedBy=multi-user.target

在 [Unit] 部分，可以提供服务的描述。
在 [Service] 部分，使用 ExecStart 来指定脚本的路径。
[Install] 部分告诉 systemd 何时应启动该服务，multi-user.target 是一个常见的选择，它将在系统启动到多用户运行级别时启动该服务

# 重新加载 systemd 管理器配置：创建服务文件后，您需要重新加载 systemd 配置，
$ systemctl daemon-reload

# 然后就可以使用systemctl start stop enable status等命令了
```

注意：确保脚本文件（/path/to/my_script.sh）具有可执行的正确权限。可以使用 chmod u+x /path/to/my_script.sh 命令使其可执行。

删除一个服务的操作 (比如我把clash删掉了):

```
systemctl stop [servicename]
systemctl disable [servicename]
rm /etc/systemd/system/[servicename]
rm /etc/systemd/system/[servicename] # and symlinks that might be related
rm /usr/lib/systemd/system/[servicename]
rm /usr/lib/systemd/system/[servicename] # and symlinks that might be related
systemctl daemon-reload
systemctl reset-failed
```

# 内存管理

# free

```
free -h
```

# 磁盘管理

## df

打印出各个文件系统及对应的磁盘占用、挂载点的信息

```
df
df -i    # 打印出来inodes的使用情况，如果Linux文件系统中小文件特别多则会导致inode不够用
df -aT   # 列出一些隐藏系统的磁盘
df -h    # 以human能看得懂的形式(自动选择单位)进行输出，而默认的输出大小都是以KB为单位的
```

## du

可以看各个文件夹的空间占用情况

可以看到，**Linux中最小的文件大小是4KB**，不够的会填充，不允许过小的文件存在

```
du        # 列出当前目录下所有文件夹的容量
du -h     # 带上合适的单位
du -ah    # 列出所有的并带单位
du -sh    # 列出当前文件夹的占用空间大小
du -sh /* # 查看根目录下各文件夹大小,  -s代表看目录总大小而不是看每个文件的大小

# 最佳实践: 查看某个目录下各个一级文件/目录的大小
du -h --max-depth=1 ./
```

## fdisk

用于磁盘分区

```
fdisk -l                      # 查看当前系统挂载的所有磁盘
fdisk <某个磁盘如/dev/sdb>     # 进入某个磁盘并可以进行分区、查看分区表等操作
```

## 挂载本地盘

下面是挂载一个本地盘

```
# 先查看有哪些磁盘
fdisk -l

# 格式化目标磁盘，注意这里的/dev/sdb1后面有数字
mkfs.ext4 /dev/sdb1

# 分区
fdisk /dev/sdb

# 挂载
blkid  # 确认/dev/sdb的UUID

vim /etc/fstab

# 详细参考 https://wiki.debian.org/fstab
UUID=<UUID> <挂载点> ext4 rw 0 0
```

注意，要把挂载点的权限改一下，否则干啥都得要sudo:

```
chown -R <用户> <挂载点>
chgrp -R <用户组> <挂载点>
```

# 控制台

CTRL + A: 移动到命令首

CTRL + E: 移动到命令尾

CTRL + C: 强制终止前台程序的执行，发送SIGINT给前台进程组种所有进程

CTRL + Z: 挂起(suspend)前台进程，发送 SIGTSTP 信号给前台进程组中的所有进程。

jobs: 查看在后台运行的任务

fg: 在前台恢复被挂起的进程: fg <任务号>

bg: 在后台恢复被挂起的进程: bg <任务号> 

其实，控制字符都是可以通过stty命令更改的，可在终端中输入命令"stty -a"查看终端配置:

```
stty -a
```

& : 加到一个命令的最后，可以让它在后台执行

shift + insert: 粘贴，相当于windows下的Ctrl V

# terminal与explorer转换

从terminal打开file explorer:

```
$ nautilus <path>

# 如果是gnome桌面，也可以用
$ gio open <path>
```

常用: gio open .

# Trouble Shooting

## 查看当前操作系统版本和版本号

```go
# 查看发行版
cat /etc/issue

# 查看内核版本
cat /proc/version
```

## 查看文件夹的sha1sum值

```
# 查看某文件的
sha1sum <文件名>

# 查看当前文件夹 ($PWD)
find . -type f \( -exec sha1sum "$PWD"/{} \; \) | awk '{print $1}' | sort | sha1sum
```

## 任务管理器

linux下没有任务管理器，当我们要看cpu资源、io等占用靠前的进程怎么办呢?

```
# 查看cpu, 内存:
# 先
htop
# 再
htop -p <进程号>

# 查看各磁盘的读写速度情况
# 如果没有 iostat 命令，那么使用 yum install sysstat 进行安装
iostat -x 1 10

# 查看各进程的读写情况
iotop -oP
# 或者  展示I/O统计，每秒更新一次
pidstat -d 1
```

## telnet连接

常用来测试目标软件是否正常工作

telnet有个好处，比如远程连接redis，必须得装个redis-cli客户端在本地，然而用telnet也可以

```
telnet 192.168.160.104 6379   # 连接
auth "1qaz2wsx"   # 认证
SELECT 5   # 进入5数据库
keys STAT_APP_SALE_STEAM_RANK_*   # 查询
keys STAT_APP_ONLINE_STEAM_RANK_*   # 查询
quit  # 退出
```

连上就可以执行一些简单的redis命令了

类似地，使用telnet可以执行dubbo、tomcat、server，只要目标软件实现了telnet server就行

# Linux底层原理 代码分析

先要把/etc/apt/sources.list 里弄好src links

```
sudo cp /etc/apt/sources.list /etc/apt/sources.list~
sudo sed -Ei 's/^# deb-src /deb-src /' /etc/apt/sources.list
sudo apt-get update
```

然后直接下载源码到当前目录下.

```
sudo apt-get source <包名>
```

# 查看被kill掉的进程

```
dmesg | grep -i kill | grep pid
```

更纤细的， 查看为什么进程被kill，以及写个小脚本来实时监控:

[http://knoxxs.github.io/programming/linux/ops/2015/08/31/linux-find-out-how-the-process-got-killed/](http://knoxxs.github.io/programming/linux/ops/2015/08/31/linux-find-out-how-the-process-got-killed/)

# 压缩/解压

## 打包与解包 : tar

打包，不压缩：

```
tar cvf <FileName>.tar <DirName>
```

解包:

```
tar xvf <FileName>.tar
```

## 压缩与解压缩

**zip**

```
zip FileName.zip DirName
unzip FileName.zip
压缩一个目录使用 -r 参数，-r 递归。例：
zip -r FileName.zip DirName
```

**rar**

```
rar a FileName.rar DirName
rar x FileName.rar
```



# Software Package Management



## Debian/Ubuntu

```shell
# search installed package
apt list --installed | grep <pkg_name>
# or
dpkg --get-selections | grep <pkg_name>

# show detailed information about a package
apt show <pkg_name>

# remove package
## --purge will remove any configuration files associated with the package
sudo apt remove --purge <pkg_name>


```



# 编解码

```
# base64 解码
echo 'asdasda=' | base64 --decode
```

# 网络

## curl

模拟http post 调用，比如要以json方式注册用户邮箱:

```
curl http://<ip>:<port>/<path> -X POST -H "content-type: application/json" -d '{"mail":"12345678@gmail.com"}' -i
```

## nslookup

查询DNS的记录，查看域名解析是否正常

直接查询A记录：

```
nslookup <域名> [dns-server]
```

如果没指定dns-server就会用系统默认的DNS服务器

查询其它记录:

```
nslookup -qt=<type> <域名> [dns-server]
```

其中，type可以是以下这些类型：

A 地址记录

AAAA 地址记录

AFSDB Andrew文件系统数据库服务器记录

ATMA ATM地址记录

CNAME 别名记录

HINFO 硬件配置记录，包括CPU、操作系统信息

ISDN 域名对应的ISDN号码

MB 存放指定邮箱的服务器

MG 邮件组记录

MINFO 邮件组和邮箱的信息记录

MR 改名的邮箱记录

MX 邮件服务器记录

NS 名字服务器记录

PTR 反向记录

RP 负责人记录

RT 路由穿透记录

SRV TCP服务器信息记录

TXT 域名对应的文本信息

X25 域名对应的X.25地址记录

查询更具体的信息:

```yaml
nslookup -d [其他参数] <域名> [dns-server]
```

加上-d还可以查域名的缓存

## route

查看/操作IP 路由表

常用命令搭配 (详细可以看man 里的 EXAMPLES):

```
route -n # 不解析名字，以IP的方式显示

route -ee # 显示详细信息

# 添加一条路由(发往192.168.62这个网段的全部要经过网关192.168.1.1)
route add -net 192.168.62.0 netmask 255.255.255.0 gw 192.168.1.1
# 删除路由 (不用写网关)
route del -net 192.168.122.0 netmask 255.255.255.0

//添加到主机的路由
# route add –host 192.168.168.110 dev eth0  # dev在这其实可以省略
# route add –host 192.168.168.119 gw 192.168.168.1

//添加默认网关
# route add default gw ${IP}
```

## ebpf

这个技术博客讲的非常的好

[https://www.netronome.com/technology/ebpf/](https://www.netronome.com/technology/ebpf/)

## netstat

查看一个服务的端口和进程号:

比如要查看一个叫spp_xxx 的服务的进程号和端口:

```
$ netstat -lnp | grep spp
tcp  0   0   10.10.145.26:9866    0.0.0.0:*   LISTEN  26778/./spp_frame_p
```

## scp

网络传输文件

```
# 从本地服务器将文件上传到远程服务器
$ scp <file_path> <username>@<ip>:<remote_addr>
# 上传目录
$ scp -r <folder_path> <username>@<ip>:<remote_addr>

# 下载文件到本地
$ scp <username>@<ip>:<remote_addr> <local_addr>
# 下载目录到本地
$ scp -r <username>@<ip>:<remote_addr> <local_addr>
```



# 权限管理

# 文件搜索

# 帮助

# 用户管理

创建用户:

```
adduser <用户名>  # 创建用户且创建它的家目录
```

但他还没root权限，需要进行权限管理

改变一个文件的用户和组:

```
sudo chown <新所有者>:<新用户组> <文件名或目录>
```



# 关机重启

```
#查看ip
ifconfig
#查看进程
jps
#开启docker
sudo systemctl start docker
#查看文件
vi broker.conf #按i进入编辑模式，按Esc推出编辑模式，:wq进行保存退出
#后面加&，使Linux命令在后台运行，可以继续执行其它命令
sudo docker-compose up &
```

# shell 编程

首先要知道自己使用的是哪个shell:

```bash
$ echo $SHELL # 显示当前登录会话使用的shell的完整路径
$ echo $0 # 当前终端窗口正在运行的shell

# 查看与当前终端会话相关的进程来找出您正在使用的shell
$ ps -p $$ # $$代表当前shell进程的进程ID 
```

在线shell编程环境:

[https://www.tutorialspoint.com/execute_bash_online.php](https://www.tutorialspoint.com/execute_bash_online.php)