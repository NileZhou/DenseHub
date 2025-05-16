# CPU程序

首先htop查看哪些进程在占用大量资源
然后：
strace -c -f -p <pid>
几秒后ctrl-c，收集并统计下这几秒的系统调用

如果是python进程，直接生成火焰图:
py-spy record -o profile.svg --pid <PID>
