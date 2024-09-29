# 参考资料

[廖雪峰Git教程](https://www.liaoxuefeng.com/wiki/896043488029600)
[git flow](https://nvie.com/posts/a-successful-git-branching-model/)

# 代理设置

## 临时设置

只对http, https有效（每次都得输入账号密码）

这是当前用户范围的。修改完之后可以在 ~/.gitconfig 下看到
clone 加速:

```shell
# 设置命令
git config --global http.proxy socks5://127.0.0.1:<port>
git config --global https.proxy socks5://127.0.0.1:<port>

# 取消设置
git config --global --unset http.proxy
git config --global --unset https.proxy
```

## 长期设置

参考 [https://zhuanlan.zhihu.com/p/481574024](https://zhuanlan.zhihu.com/p/481574024)

编辑C:\Users\<用户名，这里我的是10331>\.ssh\config 文件如下:

```shell
# Windows用户，注意替换你的端口号和connect.exe的路径
# 这里127.0.0.1:10808 是本地代理服务器的端口和地址
ProxyCommand "C:\Tools\Git\mingw64\bin\connect.exe" -S 127.0.0.1:10808 -a none %h %p

# MacOS用户用下方这条命令，注意替换你的端口号
# ProxyCommand nc -v -x 127.0.0.1:51837 %h %p

Host github.com
  User git
  Port 22
  Hostname github.com
  # 注意修改路径为你的路径
  IdentityFile "C:\Users\10331\.ssh\id_rsa"
  TCPKeepAlive yes

Host ssh.github.com
  User git
  Port 443
  Hostname ssh.github.com
  # 注意修改路径为你的路径
  IdentityFile "C:\Users\10331\.ssh\id_rsa"
  TCPKeepAlive yes
```

然后测试连接:
ssh -T git@github.com

# 最重要的

1. 做完分支管理再切换回自己分支!!! 千万不要在公共分支上开发
2. 做危险操作（如git reset --hard ^HEAD或git checkout .）前，先copy代码与目录，以防不测
3. 每次提交检查下有哪些文件变动，别把自己debug时写的变动也提交上去

参考:
[https://tsejx.github.io/devops-guidebook/code/git/rebase/](https://tsejx.github.io/devops-guidebook/code/git/rebase/)

![git.png](https://cdn.nlark.com/yuque/0/2021/png/22348649/1639451976888-f95d5618-8662-4380-b870-c21b252b0a59.png#averageHue=%23f3f3f3&clientId=ub299ddfa-f281-4&from=drop&id=uaa82434a&originHeight=3162&originWidth=1759&originalType=binary&ratio=1&rotation=0&showTitle=false&size=1529000&status=done&style=none&taskId=u9a3503fa-68f6-40f1-9b4d-ee848fffa09&title=)

# 安装/覆盖之前的账号

先下载好windows 的git版本
生成ssh

```powershell
ssh-keygen -t rsa -C <邮箱名,需要和远程gitlab仓库邮箱一样>
```

把.ssh下的rsa.pub 上传到远程仓库去

本地设置全局变量:

```powershell
git config --global user.name <用户名，和远程一样>
git config --global user.email <邮箱, 和远程一样>
```

# 给分支设置新上游

需求: 我在Github上把别人的项目A  fork 到了自己的空间，变为B，然后clone B到本地
        怎么才能在本地将A的更新同步到B，并拉取到本地呢?

1. 设置Upstream Repository
   进入本地仓库的根目录，然后使用以下命令：

   git remote add upstream [原项目A的仓库URL]

   eg: git remote add upstream git@github.com:thirdgerb/ghostiss.git
2. 获取上游仓库的更新

   git fetch upstream

   这个命令会拉取原始仓库A的所有更新到本地，但不会自动合并到你的工作目录或分支中。
3. 切换到你想要更新的分支
   假如这里想切换到主分支：

   git checkout master  # 或者 git checkout main，取决于你的主分支名称
4. 将更新合并到你的本地分支

   git merge upstream/<A项目的目标分支>
5. 推送更新到你的GitHub仓库（B）

   git push origin master  # 或者 git push origin main

# 分支暂存

如果在分支a做了修改，想切到其它分支，但又不想commit:
优雅的方式

```shell
# 暂存
git stash

# 切回分支a后:
git stash apply   # 会发现修改又回来了

```

不优雅的方式，参考: 软回滚

如果在a->b->c->d中的d上做了修改e->f，想把修改应用到a那里，变成a->e->f:
0: 把分支做个备份，以免发生不测

1. git stash把e->f暂存
2. git reset --hard <a那里>
3. git stash pop

# 分支创建

创建一个分支并切换到新分支:

```git
git checkout -b ${新分支名}
```

但是如果是切换到某个tag，而这个tag又没有相应的分支，git会提示当前处于一个“detached HEAD" 状态.
因为 tag 相当于是一个快照，是不能更改它的代码的。
如果要在 tag 代码的基础上做修改，你需要新建一个分支：

```shell
git checkout -b <新分支名> <tag名>
```

创建一个分支并留在当前分支:

```git
git branch ${新分支名}
```

# 分支查看

## 查看所有

```git
git branch -a
```

## 查看本地的所有

```git
git branch
```

## 查看远程的所有

```git
git branch -r
```

## 查看分支差异

```shell
git diff ${branch1} ${branch2} --stat   // 显示出所有有差异的文件列表
```

# 分支合并

在本地分支workflow上提交后，想合到测试分支上进行测试:

1 先在本地分支workflow提交，然后：
2 切换到develop分支    git checkout develop_2.9.0
3 拉取新的更新  git pull
4 合并    git merge  workflow
5 推送(不用commit了)    git push

merge时遇到冲突 解决
解决完冲突后，git commit一下
然后esc :wq
git push

# 分支回滚

[参考](https://zhuanlan.zhihu.com/p/56843134)

![](https://cdn.nlark.com/yuque/0/2021/webp/22348649/1631697947084-fc5b9c83-e641-4ced-91f3-c6b014fe2486.webp#averageHue=%23e9f1cc&clientId=ua6786719-4130-4&from=paste&id=u86a3f89c&originHeight=359&originWidth=638&originalType=url&ratio=1&rotation=0&showTitle=false&status=done&style=none&taskId=u9a83970c-73b4-4665-ba42-aa8e51ecd8a&title=)

## 本地回滚

### 硬回滚

代码会发生变化

首先git log查看自己要回滚到哪个分支，再

```git
git reset --hard ${版本号}
```

### 软回滚

代码不会发生变化，只是会撤销commit

```shell
git reset --soft HEAD^
```

## 远程回滚

注意: 千万不要将别人的提交也回滚掉，一定要再三确认
现在只是将本地分支进行了回滚，要回滚远程分支，还需要:

```git
git push -f
```

这里必须使用-f 强制推送覆盖远程分支，否则无法推送到远程分支，因为本地版本更落后

# 分支重命名

## 本地重命名

```git
git branch -m <oldName> <newName>
```

## 远程分支重命名

```shell
git branch -m <oldName> <newName>
git push --delete origin <oldName>
git push origin <newName>
```

# 分支修改

## 本地修改并推送

```shell
# 先本地改了文件，然后:
git add .
# 再然后: 一定要记住，-m 后面跟的是 双引号 ！！！，如果是单引号它会认为是文件路径
git commit -m "message"
# 推送到main分支
git push origin main

# 注: 看本地git暂存区里的内容（即没提交过的修改）
git status
```

## 本地丢失修改

```git
git checkout . # 丢掉本地所有没有提交的修改，返回到原来的状态
```

## 本地commit信息修改

commit写错了，在还没有push上去之前:

```shell
git commit --amend
```

然后按Enter，用vim的方式去修改

# 分支删除

## 本地删除

# 参考资料

[廖雪峰Git教程](https://www.liaoxuefeng.com/wiki/896043488029600)
[git flow](https://nvie.com/posts/a-successful-git-branching-model/)

# 代理设置

## 临时设置

只对http, https有效（每次都得输入账号密码）

这是当前用户范围的。修改完之后可以在 ~/.gitconfig 下看到
clone 加速:

```shell
# 设置命令
git config --global http.proxy socks5://127.0.0.1:<port>
git config --global https.proxy socks5://127.0.0.1:<port>

# 取消设置
git config --global --unset http.proxy
git config --global --unset https.proxy
```

## 长期设置

参考 [https://zhuanlan.zhihu.com/p/481574024](https://zhuanlan.zhihu.com/p/481574024)

编辑C:\Users\<用户名，这里我的是10331>\.ssh\config 文件如下:

```shell
# Windows用户，注意替换你的端口号和connect.exe的路径
# 这里127.0.0.1:10808 是本地代理服务器的端口和地址
ProxyCommand "C:\Tools\Git\mingw64\bin\connect.exe" -S 127.0.0.1:10808 -a none %h %p

# MacOS用户用下方这条命令，注意替换你的端口号
# ProxyCommand nc -v -x 127.0.0.1:51837 %h %p

Host github.com
  User git
  Port 22
  Hostname github.com
  # 注意修改路径为你的路径
  IdentityFile "C:\Users\10331\.ssh\id_rsa"
  TCPKeepAlive yes

Host ssh.github.com
  User git
  Port 443
  Hostname ssh.github.com
  # 注意修改路径为你的路径
  IdentityFile "C:\Users\10331\.ssh\id_rsa"
  TCPKeepAlive yes
```

然后测试连接:
ssh -T git@github.com

# 最重要的

1. 做完分支管理再切换回自己分支!!! 千万不要在公共分支上开发
2. 做危险操作（如git reset --hard ^HEAD或git checkout .）前，先copy代码与目录，以防不测
3. 每次提交检查下有哪些文件变动，别把自己debug时写的变动也提交上去

参考:
[https://tsejx.github.io/devops-guidebook/code/git/rebase/](https://tsejx.github.io/devops-guidebook/code/git/rebase/)

![git.png](https://cdn.nlark.com/yuque/0/2021/png/22348649/1639451976888-f95d5618-8662-4380-b870-c21b252b0a59.png#averageHue=%23f3f3f3&clientId=ub299ddfa-f281-4&from=drop&id=uaa82434a&originHeight=3162&originWidth=1759&originalType=binary&ratio=1&rotation=0&showTitle=false&size=1529000&status=done&style=none&taskId=u9a3503fa-68f6-40f1-9b4d-ee848fffa09&title=)

# 安装/覆盖之前的账号

先下载好windows 的git版本
生成ssh

```powershell
ssh-keygen -t rsa -C <邮箱名,需要和远程gitlab仓库邮箱一样>
```

把.ssh下的rsa.pub 上传到远程仓库去

本地设置全局变量:

```powershell
git config --global user.name <用户名，和远程一样>
git config --global user.email <邮箱, 和远程一样>
```

# 分支暂存

如果在分支a做了修改，想切到其它分支，但又不想commit:
优雅的方式

```shell
# 暂存
git stash

# 切回分支a后:
git stash apply   # 会发现修改又回来了

```

不优雅的方式，参考: 软回滚

如果在a->b->c->d中的d上做了修改e->f，想把修改应用到a那里，变成a->e->f:
0: 把分支做个备份，以免发生不测

1. git stash把e->f暂存
2. git reset --hard <a那里>
3. git stash pop

# 分支创建

创建一个分支并切换到新分支:

```git
git checkout -b ${新分支名}
```

但是如果是切换到某个tag，而这个tag又没有相应的分支，git会提示当前处于一个“detached HEAD" 状态.
因为 tag 相当于是一个快照，是不能更改它的代码的。
如果要在 tag 代码的基础上做修改，你需要新建一个分支：

```shell
git checkout -b <新分支名> <tag名>
```

创建一个分支并留在当前分支:

```git
git branch ${新分支名}
```

# 分支查看

## 查看所有

```git
git branch -a
```

## 查看本地的所有

```git
git branch
```

## 查看远程的所有

```git
git branch -r
```

## 查看分支差异

```shell
git diff ${branch1} ${branch2} --stat   // 显示出所有有差异的文件列表
```

# 分支合并

在本地分支workflow上提交后，想合到测试分支上进行测试:

1 先在本地分支workflow提交，然后：
2 切换到develop分支    git checkout develop_2.9.0
3 拉取新的更新  git pull
4 合并    git merge  workflow
5 推送(不用commit了)    git push

merge时遇到冲突 解决
解决完冲突后，git commit一下
然后esc :wq
git push

# 分支回滚

[参考](https://zhuanlan.zhihu.com/p/56843134)

![](https://cdn.nlark.com/yuque/0/2021/webp/22348649/1631697947084-fc5b9c83-e641-4ced-91f3-c6b014fe2486.webp#averageHue=%23e9f1cc&clientId=ua6786719-4130-4&from=paste&id=u86a3f89c&originHeight=359&originWidth=638&originalType=url&ratio=1&rotation=0&showTitle=false&status=done&style=none&taskId=u9a83970c-73b4-4665-ba42-aa8e51ecd8a&title=)

## 本地回滚

### 硬回滚

代码会发生变化

首先git log查看自己要回滚到哪个分支，再

```git
git reset --hard ${版本号}
```

### 软回滚

代码不会发生变化，只是会撤销commit

```shell
git reset --soft HEAD^
```

## 远程回滚

注意: 千万不要将别人的提交也回滚掉，一定要再三确认
现在只是将本地分支进行了回滚，要回滚远程分支，还需要:

```git
git push -f
```

这里必须使用-f 强制推送覆盖远程分支，否则无法推送到远程分支，因为本地版本更落后

# 分支重命名

## 本地重命名

```git
git branch -m <oldName> <newName>
```

## 远程分支重命名

```shell
git branch -m <oldName> <newName>
git push --delete origin <oldName>
git push origin <newName>
```

# 分支修改

## 本地修改并推送

```shell
# 先本地改了文件，然后:
git add .
# 再然后: 一定要记住，-m 后面跟的是 双引号 ！！！，如果是单引号它会认为是文件路径
git commit -m "message"
# 推送到main分支
git push origin main

# 注: 看本地git暂存区里的内容（即没提交过的修改）
git status
```

## 本地丢失修改

```git
git checkout . # 丢掉本地所有没有提交的修改，返回到原来的状态
```

## 本地commit信息修改

commit写错了，在还没有push上去之前:

```shell
git commit --amend
```

然后按Enter，用vim的方式去修改

# 分支删除

## 本地删除

```git
git branch -d ${分支名}
# 或者 即使有未merge的东西也要删:
git branch -D ${分支名}
```

## 远程删除

```git
git push origin --delete ${分支名}
```

# Git rebase (危险)

## 合并多次提交记录

git rebase -i ${上一次master的hash串}
![2115cec9-aea1-448a-9e6e-ebfb0d964b36.png](https://cdn.nlark.com/yuque/0/2021/png/22348649/1634882993160-966f7e26-0127-4d8f-8f44-3683489bf862.png#averageHue=%2340403f&clientId=u557d6dd3-8872-4&from=drop&id=u29be444e&originHeight=722&originWidth=1126&originalType=binary&ratio=1&rotation=0&showTitle=false&size=124990&status=done&style=none&taskId=u4953fc68-61e1-45c9-86d5-6a64ff59ec2&title=)

解决完冲突后git commit，如果没冲突不用commit
git push -f

## 变基

如果发生错误，提示已经有一次错误提交:
git rebase --abort  丢弃以前错误的rebase

git rebase master
解决完冲突后
git rebase --continue
再提交:
git push -f

# Git原理

![image.png](https://cdn.nlark.com/yuque/0/2021/png/22348649/1631698970443-32f5571e-439b-4ce0-a181-bd99331889da.png#averageHue=%230d0d05&clientId=ua6786719-4130-4&from=paste&id=udee404a6&originHeight=340&originWidth=1172&originalType=url&ratio=1&rotation=0&showTitle=false&size=106758&status=done&style=none&taskId=ue211c748-43b2-445d-bdf3-9e94f9b8d37&title=)

三个区域:

```git
git branch -d ${分支名}
# 或者 即使有未merge的东西也要删:
git branch -D ${分支名}
```

## 远程删除

```git
git push origin --delete ${分支名}
```

# Git rebase (危险)

## 合并多次提交记录

git rebase -i ${上一次master的hash串}
![2115cec9-aea1-448a-9e6e-ebfb0d964b36.png](https://cdn.nlark.com/yuque/0/2021/png/22348649/1634882993160-966f7e26-0127-4d8f-8f44-3683489bf862.png#averageHue=%2340403f&clientId=u557d6dd3-8872-4&from=drop&id=u29be444e&originHeight=722&originWidth=1126&originalType=binary&ratio=1&rotation=0&showTitle=false&size=124990&status=done&style=none&taskId=u4953fc68-61e1-45c9-86d5-6a64ff59ec2&title=)

解决完冲突后git commit，如果没冲突不用commit
git push -f

## 变基

如果发生错误，提示已经有一次错误提交:
git rebase --abort  丢弃以前错误的rebase

git rebase master
解决完冲突后
git rebase --continue
再提交:
git push -f

# Git原理

![image.png](https://cdn.nlark.com/yuque/0/2021/png/22348649/1631698970443-32f5571e-439b-4ce0-a181-bd99331889da.png#averageHue=%230d0d05&clientId=ua6786719-4130-4&from=paste&id=udee404a6&originHeight=340&originWidth=1172&originalType=url&ratio=1&rotation=0&showTitle=false&size=106758&status=done&style=none&taskId=ue211c748-43b2-445d-bdf3-9e94f9b8d37&title=)

三个区域:
