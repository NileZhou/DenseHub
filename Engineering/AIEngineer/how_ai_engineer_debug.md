# Local Debug

## Current file

launch.json:   

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Debug Current File",
            "type": "debugpy",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "justMyCode": false,
            "cwd": "${fileDirname}",
            "env": {
                "PATH": "/root/miniconda3/envs/verl/bin:$PATH", // python环境PATH 
                "CONDA_PREFIX": "/root/miniconda3/envs/verl",   // python环境conda prefix
                "CONDA_DEFAULT_ENV": "verl"                     // python环境conda env name
            }
        }
    ]
}

```


## Current module




# Remote Debug

要确认与远程机器ip: port连通


## Remote file


launch.json:   

```json
{
    "name": "Python: Attach to Remote (Train)",
    "type": "debugpy",
    "request": "attach",
    "connect": {
        "host": "10.194.07.24", // remote ip
        "port": 5678            // remote port
    },
    "pathMappings": [
        {
            "localRoot": "${workspaceFolder}",
            "remoteRoot": "/path/project_path" // 项目根地址
        }
    ],
    "justMyCode": false
}
```

依次执行:   
```shell
# 在远程机器上: 
cd /path/project_path
# 0.0.0.0 代表来者不拒， oexps/base_models/gen.py代表从项目根地址出发到此文件的地址
python -m debugpy --listen 0.0.0.0:<remote port > --wait-for-client oexps/base_models/gen.py
python -m debugpy --listen 0.0.0.0:5678 --wait-for-client oexps/base_models/gen.py

# 在vscode中:
# 打开左上角 "Start Debugging"
# 在顶部的调试配置下拉菜单中，选择 Python: Attach to Remote (Train)
# debug，然后去attach到远程进程
```


## Remote torchrun


与remote file的debug方式类似，唯一不同：
启动脚本要这么写:
```shell
python -m debugpy --listen 0.0.0.0:<remote port> --wait-for-client \
    -m torch.distributed.run --standalone --nnodes=$TORCH_NNODES --nproc_per_node=$TORCH_NPROC_PER_NODE \
 src/train.py
```

然后在vscode里，"Start Debugging"后打断点即可


## Remote Ray

1. vscode里装插件: Ray Distributed Debugger
2. 在插件页面, 点击【Add cluster】, 输入目标机器的ip:port, port是ray程序的dashboard port，一般为8265
3. vscode插件里点击config，配置好项目目录（此地址一定要是可以启动目标ray程序代码，无报错的地址，可以先在terminal下进入该地址试试）
4. 启动的程序代码里，ray的env_vars里包含：
```shell
DEBUG: "1"
```
5. 启动的程序代码里，要打断点的地方，写个 breakpoint()
6. 启动程序代码，执行至breakpoint()处，左边的插件那会有反应，点击start debugging即可




