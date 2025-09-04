# Sync 同步

zotero支持的云盘列表：https://www.zotero.org/support/kb/webdav_services，坚果云（https://www.jianguoyun.com/s/pricing）也支持

云盘: https://app.koofr.net/  (免费10G)
1. koofr这里：注册账号，记下注册邮箱 M
2. koofr这里：点击自己头像，进入【Preferences】 -> 【Password】，找到下方的Generate new password，输入一个比如叫WebDAV_Zotero的，点击【Generate】，会生成一个密码，记下这个密码 PWD
3. 转到zotero那里, 进入【Settings】-> 【Sync】 ，看到【File Syncing】
4. 将sync方式从Zotero换为WebDAV (在Zotero点击下，下拉中看到WebDAV)
5. URL为https://  app.koofr.net/dav/Koofr   /zotero/，我们需要填的是app.koofr.net/dav/Koofr
6. username输入 M
7. Password输入 PWD
8. 点击verify server看看成功不，第一次可能zotero会提示在koofr创建名为zotero的app
9. 如果成功，回到zotero，右上角的sync符号，进行同步，然后在koofr那看到一个新的zotero文件夹开始接收上传同步的内容了

手机上：
1. settings -> Account，来到【File Syncing】的地方，把Zotero改为WebDAV
2. 填写app.koofr.net/dav/Koofr, M, PWD，一定要和电脑端一样


# 护眼模式

【Tools】->【Plugin】，安装这个插件: https://github.com/muisedestiny/zotero-style#readme

# 批量导出PDF

全选，然后批量导出

# 高级

群晖NAS 自搭网盘，适配WebDAV协议
https://zhuanlan.zhihu.com/p/529294294

