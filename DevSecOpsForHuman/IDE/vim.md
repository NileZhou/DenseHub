常用快捷键:

ESC模式下:
- w: 快速向右移动，每次一个单词
- b: 快速向左移动，每次一个单词
- $: 快速移动到行尾
- 0: 快速移动到行首


# 中文不显示问题

vim ~/.vimrc,输入以下:
```shell
set encoding=utf-8      " Vim 内部编码
set fileencodings=utf-8,gbk,gb18030,big5 " 自动识别文件编码列表
set termencoding=utf-8  " 终端编码
set ambiwidth=double    " 处理全角符号（如中文引号
```