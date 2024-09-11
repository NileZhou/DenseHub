- [notes](#notes)

# notes

- Container
  Abstract -> beanDefinition
  Type[Abstract] -> type of bean
  Provider -> bean selector when inject (qualifier + factory method)
- Thought

It's like smart function,
LLM可以在当前会话完成的思考且产生的行为,尽量都用代码,太复杂就包传统函数即可
LLM自认为无法在当前会话完成的思考, 且需要AI作为单元驱动(否则还是应该调Tool或Library), 就应该创建Thought
复用Thought, 实质上是在复用智能函数
Thought 作为 BaseModel 类, 可以任意定义参数, 里面也可以加自然语言. 返回的是自然语言或者变量类消息

- Difference between thought and agent
  The implementation of thought and agent are very similar. But an agent should be in it's own process, while there are lots of thought in a process.
- MultiTask
  The orchestration mechanism of smart funcitons, like multi-thread mechanism to run functions
- MindSet
  MindSet就是一个智能函数的集合, 或者说, 智能类
  和传统类不太一样的是,这个类是可以不断给自己加智能函数的,或者说持续学习的
- Relation between moss module and thought
  moss module 对于 thought 而言还是应该作为一个配置项.
  比如一个简单的 ToolAgent, 可以切换 moss module path 来切换功能.
  有两个核心的考虑:

  1. 不要轻易让 Thought 感知到自身的存在,   Moss 是它看到的世界,  Thought 是我们眼里的它,  只有 meta thought 可以修改 thought. 否则不知道会发生什么.
  2. thought 不和 moss 耦合,  这样避免说创建一个 thought 实例 (调整了一些包和类库)  就得重新建一个文件
     比如说 一万个 thoughts 或者 agents,  背后可能只有几十个文件.  而没必要创建一万个

life cycle:

- compiler
  - compile: generate the target module object firstly (_compile method), then
  - 



session -> process -> task

一个process下有个root task，然后哦其它task都是父子关系的进程树









# workflow 深水区

1. debug问题, 动态代码->静态代码，人类可介入
2. 每个节点idempotent 幂等的问题





# Paper thought:

1. Module即容器，共享进程内context

2. Ioc

解决的问题都是: Agent写出来，且运行的代码要影响自己框架的代码

moss is a shell, ghost 就算是一个OS的进程管理



全异步好处: 

1. 并行计算
2. 增加交互体验
3. 主动推送

