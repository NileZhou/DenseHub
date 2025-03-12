# 使用方法
```shell
import ipdb
# ... other code
ipdb.set_trace() # 执行到这行会自动进入ipdb
```

# control flow
| command | desc | eg |
|--|--|--|
| n (next line) | step over to next line(not step in) | n |
| s (next line) | step into function to execute next line | s |
| c (continue)  | keep run to next breakpoint | c |
| r (return)    | execute until current function return | r |
| until <lineno> | execute until to the line number | until 90 |
| j <lineno>    | jump to specific line number (be careful) | 
| q (quit)      | quit and kill program | q |

# breakpoint
| command | desc | eg |
|--|--|--|
| b | 查看所有断点 | b |
| b (break) [location] | 设置断点 | b 10 (第10行)<br>b my_function (函数入口) |
| tbreak [location] | 临时断点（命中后自动删除） | tbreak 20 |
| cl (clear) [bpnumber] | 清除断点 | cl 1 (清除断点1) |
| disable [bpnumber] | 禁用断点 | disable 1 |
| enable [bpnumber] | 启用断点 | enable 1 |
| ignore [bpnumber] [count] | 忽略断点次数 | ignore 1 5 (忽略断点1前5次触发) |
| condition [bpnumber] [expr] | 条件断点 | condition 1 x > 5 (当x>5时触发断点1) |


# stack

| command | desc | eg |
|--|--|--|
| w (where) | print whole stack trace | w |
| u (up) | go to the outerside frame | u |
| d (down) | go to the inside frame | d |

# show

| command | desc | eg |
|--|--|--|
|l (list) | show code around current position | l |
|l <start_line>,<end_line>  | show code from <start_line> to <end_line> | p 50, 150 |
| p (print) | print value of variable | p x |
| pp locals() | 漂亮打印当前所有局部变量，包含入参的值 | pp locals() |

