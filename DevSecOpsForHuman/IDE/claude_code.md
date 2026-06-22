

# install

## on ubuntu

curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo bash -
sudo apt-get install -y nodejs
node --version

npm install -g @anthropic-ai/claude-code
claude --version

# uninstall

npm uninstall -g @anthropic-ai/claude-code

root用户无法bypass permission，加一条设定即可:
IS_SANDBOX=1 claude --dangerously-skip-permissions 

# 常用命令

# Claude Code 20个最常用核心命令

| 命令 | 功能描述 |
|---|---|
| `/help` | 列出所有可用的命令及帮助信息 |
| `/init` | 在当前项目根目录生成 `CLAUDE.md` 模板文件 |
| `/clear` | 清空当前对话历史和上下文，开启全新会话（别名 `/reset`） |
| `/compact` | 压缩当前长对话并生成摘要，释放上下文 Token 空间 |
| `/btw` | 快速问个附加问题（Side question），不计入主对话上下文 |
| `/rewind` | 时光倒流（回滚），撤销代码或对话至之前的某个节点 |
| `/model` | 查看或切换当前会话正在使用的 AI 模型 |
| `/cost` | 显示当前会话消耗的 Token 数量及具体金额花费 |
| `/usage` | 查看你账户当前的调用额度限制和频率限制状态 |
| `/context` | 可视化当前加载了哪些上下文，以及 Token 花在哪些文件上 |
| `/memory` | 快速查看或编辑当前生效的 `CLAUDE.md` 记忆文件 |
| `/plan` | 进入规划模式，只分析和输出修改计划，不直接改代码 |
| `/diff` | 调出交互式界面，查看当前未提交（Uncommitted）的代码变更 |
| `/add-dir` | 将额外的文件夹目录加入到当前 Claude 的访问权限中 |
| `/permissions`| 查看或修改工具执行时的审批权限规则 |
| `/config` | 打开全局配置面板（修改主题、默认设置、编辑器模式等） |
| `/agents` | 管理子智能体（Sub-agents），可拆分并并行处理后台任务 |
| `/mcp` | 管理 MCP (Model Context Protocol) 服务器的连接与鉴权 |
| `/resume` | 恢复并继续之前的历史会话（别名 `/continue`） |
| `/exit` | 退出 Claude Code CLI 交互终端（别名 `/quit`） |

> **提示**：在对话中输入 `@` 符号，可直接搜索并引用具体的文件、目录或网页链接作为上下文。
> 