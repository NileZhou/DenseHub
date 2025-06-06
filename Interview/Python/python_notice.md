**数据结构需注意**

```python
>>> from collections import defaultdict
>>> d = v
>>> d = defaultdict(list)
>>> d[1].extend('prompt')
>>> d[1]
['p', 'r', 'o', 'm', 'p', 't']
>>> d[2].append('prompt')  # 所以如果是字符串，一定要用append，不能用extend
>>> d[2]
['prompt']
```

**Python f-string填充零的正确使用方法：**

在Python中，当你使用f-strings来格式化数字，并希望数字以特定的长度显示，同时在前面补零时，你需要确保在指定的宽度前不要有空格。如果在冒号和数字宽度规范之间加入空格，它会被解释为对齐指令，而不是填充字符的一部分。以下是一个正确的示例：

错误的格式：

```
s = f'{79: 03}|'
print(s)  # 输出 " 79|"，数字前有一个空格而不是零

```

正确的格式：

```
s = f'{79:03}|'
print(s)  # 输出 "079|"，数字前正确地填充了零

```

使用这种格式，可以确保数字按预期格式填充零。
