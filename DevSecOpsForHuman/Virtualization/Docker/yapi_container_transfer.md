
前提，已经有制作好的镜像文件，在\\Aventon_nas\it技术研发部\yapi所需数据  中进行下载

# 准备数据
将aventon-yapi-1.0.tar, aventon-yapi-mongo-1.0.tar 放到当前目录下
将db.zip 解压到 D:\volumes 下

执行命令:
```shell
docker load < aventon-yapi-1.0.tar
docker load < aventon-yapi-mongo-1.0.tar
docker network create --driver=bridge --subnet=172.19.0.0/16 --gateway=172.19.0.1 aventon-net
docker run -d --name aventon-yapi-mongo --restart unless-stopped -v "D:\\volumes\\db":/data/db --network aventon-net aventon-yapi-mongo:1.0
docker run -d --name yapi-web --restart unless-stopped -p 40001:3000 -e YAPI_CLOSE_REGISTER=false -e YAPI_DB_SERVERNAME=aventon-yapi-mongo -e YAPI_DB_PORT=27017 -e YAPI_DB_DATABASE=yapi -e YAPI_MAIL_ENABLE=false -e YAPI_LDAP_LOGIN_ENABLE=false -e YAPI_PLUGINS=[] --network aventon-net aventon-yapi:1.0
```

访问 http://localhost:40001 ，即可