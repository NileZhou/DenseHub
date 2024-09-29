# 问题解决

## 每次push都弹出登录框

![image.png](https://cdn.nlark.com/yuque/0/2022/png/22348649/1647783880372-e897a2b8-e59e-4e41-8223-3e9553a7c935.png#averageHue=%23fcfcfc&clientId=u4c904c60-e355-4&errorMessage=unknown%20error&from=paste&height=314&id=u9e1b99a8&originHeight=413&originWidth=409&originalType=url&ratio=1&rotation=0&showTitle=false&size=24767&status=error&style=none&taskId=u85317a3f-c2f4-408f-94be-b0e4c58ce05&title=&width=311)
这是因为copy respository 的时候走的是https协议而不是ssh key走的ssh协议
[参考](https://zhuanlan.zhihu.com/p/339964630)



## push被拒绝

### 1 命令不对

报错如下:

```shell
To git@github.com:myrepo.git
 ! [rejected]        development -> development (non-fast-forward)
error: failed to push some refs to 'git@github.com:myrepo.git'
To prevent you from losing history, non-fast-forward updates were rejected
Merge the remote changes (e.g. 'git pull') before pushing again.  See the
'Note about fast-forwards' section of 'git push --help' for details.
```

解决:

```
$ git pull origin main
$ git push origin main
```

注意github上主分支名为main而不是master

### 2 邮箱隐私设置

报错:

```shell
remote: error: GH007: Your push would publish a private email address.
remote: You can make your email public or disable this protection by visiting:
remote: http://github.com/settings/emails
To github.com:NileZhou/AlgorithmsRecords.git
 ! [remote rejected] main -> main (push declined due to email privacy restrictions)
error: failed to push some refs to 'github.com:NileZhou/AlgorithmsRecords.git'
```

解决:

1. 先点击settings，再点击Access下的Emails:

![image.png](https://cdn.nlark.com/yuque/0/2022/png/22348649/1647785157139-29ef00bd-daf1-4c06-83c2-7bc7f441ff12.png#averageHue=%23c4c2bf&clientId=ud2ac5d4e-986c-4&errorMessage=unknown%20error&from=paste&height=454&id=uf704afaa&originHeight=809&originWidth=429&originalType=binary&ratio=1&rotation=0&showTitle=false&size=44782&status=error&style=none&taskId=u082de861-73d3-4425-af3c-23adbf38302&title=&width=241)

2. 取消勾

![image.png](https://cdn.nlark.com/yuque/0/2022/png/22348649/1647785234091-bc38425b-ade1-4fc3-b97c-59deab5b66bb.png#averageHue=%23c4c1be&clientId=ud2ac5d4e-986c-4&errorMessage=unknown%20error&from=paste&height=268&id=u4454b1e8&originHeight=648&originWidth=1441&originalType=binary&ratio=1&rotation=0&showTitle=false&size=104193&status=error&style=none&taskId=ueb433be3-29c5-432f-82fe-1bca3e24e32&title=&width=597)

### 3 error: GH013: Repository rule violations found for xxx

GITHUB PUSH PROTECTION

看具体的Protection rule，一般情况下是push的内容中包含了secret, token等东西

## pull 报connection reset

报错如下:

```shell
Connection reset by 140.82.114.4 port 22
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
```

有可能是网络问题，校园网换自己的热点就好了

或者是ssh 密钥问题，重新生成密钥
