# basic concepts

- rank: 全局进程号且全局唯一，从0开始，如果一个GPU上分配一个进程的话，rank0指0卡上的进程
- local_rank: 在单个node上进程的相对序号,从0开始,local_rank在node之间相互独立,全局不唯一，node里唯一
- node: 节点(容器/物理节点)，一个node上通常有多个GPU
    - node_rank: 标识第几台node
    - nnodes: 节点数量
    - nproc_per_node: 每个节点上的进程数
    - ngprus_per_node: 每个节点上可用的GPU卡数
- world_size: 全局进程总个数，即在一个分布式任务中rank的数量
- Group: 进程组，一个分布式任务对应了一个进程组。只有用户需要创立多个进程组时才会用到group来管理，默认情况下只有一个group


# Distributed Train

## DDP

4 main steps:
1. 初始化进程组: dist.init_process_group
```python
torch.distributed.init_process_group(
    backend,  # 通常GPU采用NCCL, CPU采用GLOO
    init_method=None, # 可以是TCP连接 / File共享文件系统 / ENV环境变量三种方式
    world_size=-1, 
    rank=-1, 
    store=None,
    ...)
```

2. 设置分布式采样器: DistributedSampler

```python
torch.utils.data.distributed.DistributedSampler(
    dataset,
    num_replicas=None,  # 把数据集分成多少份，默认是当前dist的world_size
    rank=None, # 当前进程的id，默认dist的rank
    shuffle=True, 
    seed=0, 
    drop_last=False)
```

3. 使用DistributedDataParallel封装模型

```python
torch.cuda.set_device(local_rank)
model = Model().cuda()
model = DistributedDataParallel(model, device_ids=[local_rank])
```

4. 使用torchrun 或者 mp.spawn 启动分布式训练

# Reference

- https://pytorch.org/tutorials/beginner/dist_overview.html
