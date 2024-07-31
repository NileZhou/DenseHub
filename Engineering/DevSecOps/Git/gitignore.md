

如果之前已经上传过.idea 文件夹，则需要先在本地
git rm -r --cached .idea  
然后在.gitignore文件中加入 ".idea"
再git add, commit, push一条龙

才能在远端把.idea文件夹删除掉

# 模板

## Intellij

```shell
#.gitignore for java
*.class
test/output/
test/test/
test/stable/
logs/
output/

# Package Files #
*.jar
*.war
*.ear
**/target/

# logs
/stacktrace.log
/test/reports
/logs
*.log
*.log.*

## .gitignore for intellij
*.iml
*.ipr
*.iws
.idea/

## .gitignore for eclipse
*.pydevproject
.project
.metadata
bin/**
tmp/**
tmp/**/*
*.tmp
*.bak
*.swp
*~.nib
local.properties
.classpath
.settings/
.loadpath

## MacOS
.DS_Store
pom.xml.versionsBackup
.deploy/
output
```