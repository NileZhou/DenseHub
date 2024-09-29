# 
# 监控指标

## 同比 vs 环比

- 同比: 相邻时间段的同一时刻进行对比，如2月3日 对比 3月3日的监控数据
- 环比: 相邻时间段进行对比，如2月3日对比2月2日的数据。英文有Month (on/over) Month (MoM), YoY, QoQ (季度对比)

同比看的是大的趋势变化，环比看的是小的变化

## p90 p99分位数
中位数就是p50分位数
上四分位数就是p75分位数
可推

# 各种发布策略

## 蓝绿部署

![image.png](https://cdn.nlark.com/yuque/0/2022/png/22348649/1647934337157-5682a07c-5268-4139-b9ef-f373594bf193.png#averageHue=%23f7f7f7&clientId=u28ccc812-e32f-4&from=paste&height=248&id=ucf554d9c&originHeight=496&originWidth=1018&originalType=binary&ratio=1&rotation=0&showTitle=false&size=26085&status=done&style=none&taskId=u6ac63f76-4c87-4da6-88b4-43bb10aa233&title=&width=509)
部署的时候，并不停止掉老版本，而是直接部署一套新版本，等新版本运行起来后，再将流量切换到新版本上。
但是蓝绿部署要求在升级过程中，同时运行两套程序，对硬件的要求就是日常所需的二倍

## 滚动发布
并不一下启动所有新版本，是先启动一台新版本，再停止一台老版本 --> 然后再启动一台新版本，再停止一台老版本，直到升级完成。如果日常需要10台服务器，那么升级过程中也就只需要11台就行了

缺点: 流量会直接流向启动起来的新版本，但是这时新版本不一定可用，难以判断问题是新版本还是老版本造成的


## 灰度发布 + A/B test
也叫金丝雀(canary)发布，起源: 矿井工人发现，金丝雀对瓦斯气体很敏感，矿工会在下井之前，先放一只金丝雀到井中，如果金丝雀不叫了，就代表瓦斯浓度高。

![image.png](https://cdn.nlark.com/yuque/0/2022/png/22348649/1647934635157-6e6f0508-56eb-409a-bf62-7cc50db54b70.png#averageHue=%23f8f8f8&clientId=u28ccc812-e32f-4&from=paste&height=248&id=u757dd331&originHeight=496&originWidth=1018&originalType=binary&ratio=1&rotation=0&showTitle=false&size=32947&status=done&style=none&taskId=u36d27197-0e86-400c-81f3-6798bc4b79d&title=&width=509)
其实就是滚动发布 + 流量控制

发布开始后，先启动一个新版本应用，但并不直接将流量切过来，而是OA对新版本进行线上测试，启动的这个新版本应用(金丝雀) 如果没有问题，那么可以将少量的用户流量导入到新版本上，然后再对新版本做运行状态观察，收集各种运行时数据。
此时对新旧版本做各种数据对比，就是所谓的A/B测试

当确认新版本运行良好后，再逐步将更多的流量导入到新版本上，在此期间，还可以不断地调整新旧两个版本的运行的服务器副本数量，以使得新版本能够承受越来越大的流量压力。直到将100%的流量都切换到新版本上，最后关闭剩下的老版本服务，完成灰度发布

其实灰度发布分为前端、客户端、服务端，[参考](https://baijiahao.baidu.com/s?id=1692367749356717047&wfr=spider&for=pc)
# 
# 应用运维体系建设
应用运维体系建设，这是运维的基础。正确运维建设思路：从标准化和应用生命周期开始，一步步建立运维技术体系和组织架构。
## 运维的价值
### 软件运行维护阶段很长
从软件生命周期的角度看，软件开发阶段只占整个生命周期的20%~30%左右，软件运行维护阶段是最长尾的。
### 除去业务需求实现层面的事情，其他都是运维的范畴
一个公司对于开发的诉求是全力实现业务需求，并将需求尽快发布上线以实现商业上的收益。但是，在一个公司里，除了专注于业务需求的开发和测试角色外，还会有另外一大类开发，比如我们常见的中间件开发、稳定性开发、工具开发、监控开发、IaaS获PaaS平台开发，甚至专注于底层基础架构的内核开发、网络开发、协议开发等等，这些技术岗位都是为软件生命周期中的运行维护阶段服务的，这些角色的作用就是提升研发效率和稳定性，进而降低成本。虽然他们并没有全部被定义为运维岗位，但是本质上他们是跟业务软件的运行维护阶段直接相关的。
所以，从运维的范畴上来讲，我认为，一个研发团队内，除去业务需求实现层面的事情，其他都是运维的范畴，这个范畴内的事情本质上都是在为软件生命周期中的运行维护阶段服务。
### 运维能力是整体技术架构能力的体现
运维能力是整体技术架构能力的体现，运维层面爆发的问题或故障，一定是整体技术架构中存在问题，割裂两者，单纯地看技术架构或运维都是毫无意义的。
运维思路上的转变，远比单纯提升运维技术更有价值，而运维真正的价值应该跟研发团队保持一致，真正聚焦到效率、稳定和成本上来。
## 运维的职责
研发团队对运维团队的诉求，以及运维呈现的价值已经发生了变化，我们更加需要能够帮助团队建设出高效运维体系的角色，而不是能够被动响应更多问题的角色。
运维接触更多的是软件生命周期中的运行维护阶段，在这个阶段要做如下一些事情。
![image.png](https://cdn.nlark.com/yuque/0/2022/png/22983971/1667308159454-307ee76c-7beb-42a4-b695-0adc0889640c.png#averageHue=%23b6e6a7&clientId=uac78eac5-8e9b-4&from=paste&height=266&id=PUvhF&originHeight=332&originWidth=869&originalType=binary&ratio=1&rotation=0&showTitle=false&size=145167&status=done&style=none&taskId=u2fab5300-4767-4c07-b451-7be10e8a151&title=&width=695.2)
1、基础架构标准化（是运维的基础和核心。参与制定基础架构标准，并强势地约束）
2、基础架构服务化（让开发依赖平台的能力自助完成对基础组件的需求，而不是依赖运维的人）
3、持续交付体系建设（是拉通运维和业务开发的关键纽带，是提升整个研发团队效率的关键部分）
4、稳定性体系建设
5、技术运营体系建设（确保上述的建设落地）
## 谷歌SRE运维模式解读
> SRE是一个岗位，但更是一种运维理念和方法论。

《SRE：Google运维解密》
SRE（Site Reliability Engineer），直译过来是网站稳定性工程师
SRE != 运维
SRE理念的核心是：用软件工程的方法重新设计和定义运维工作
SRE岗位的职责：效率&稳定。以稳定性为目标，围绕着稳定这个核心，负责可用性、时延、性能、效率、变更管理、监控、应急响应和容量管理等相关的工作。
分解一下，这里主要有管理和技术两方面的事情要做。
管理体系上，涉及服务质量指标（SLI、SLA、SLO）、发布规则、变更规则、应急响应机制、On-Call、事后复盘机制等一系列配套的管理规范和标准制定等。
技术体系上，以支持和实现上述标准和规范为目标，涉及自动化、发布、监控、问题定位、容量定位，最终以电子流程串联各个环节，做到事情的闭环。

来看几个主要的系统
自动化：谷歌内部大名鼎鼎的Brog系统，它的开源版本kubernetes已然成为业界容器编排体系标准，可以随时随地实现无感知的服务迁移。
问题定位：谷歌的Dapper大名鼎鼎，功能很强大，能够快速定位问题，国内外很多跟踪系统和思路都参考了Dapper的理论。
各类分布式系统：如分布式锁、分布式文件、分布式数据库，我们熟知的谷歌三大分布式论文，就是这些分布式系统的优秀代表，也正是这三大论文，开启了业界分布式架构理念的落地。
## 为什么Netfilx没有运维岗位？
> 合理的组织架构是保障技术架构落地的必要条件，用技术手段来解决运维过程中遇到的效率和稳定问题才是根本解决方案。


### Netfilx运维现状
没有运维岗位。在1亿用户，每天1.2亿播放时长，万级微服务实例的业务体量下，SRE人数竟然不超过10人。
### 为什么Netflix会做得如此极致？
可以从Netflix的技术架构、组织架构、企业文化来看

#### 技术架构：微服务架构的最佳实践典范（Spring Cloud Netflix 就是出自此）
微服务架构下的运维就必须要靠软件工程思路去打造工具支撑体系来支持了，也就是要求微服务架构既要能够支撑业务功能，还要能够提供和暴露更多的在后期交付和线上运维阶段所需的基础维护能力。
简单举几个例子，比如服务上下线、路由策略调整、并发数动态调整、功能开关、访问ACL控制、异常熔断和旁路、调用关系和服务质量日志输出等等，要在这些能力上去建设我们的运维工具和服务平台。
在微服务架构模式下，运维一定要与微服务架构本身紧密结合起来，运维已经成为整体技术架构和体系中不可分割的一部分，两者脱节就会带来后续一系列的严重问题。

#### 组织架构：将中间件、SRE、DBA、交付和自动化工具、基础架构等团队都放在统一的云平台工程这个大团队下，在产品层面统一规划和建设，从而能够最大程度地发挥组织能力，避免了开发和运维的脱节。
业界大名鼎鼎的NetflixOSS开源产品体系里，绝大部分的产品都出自这个团队。比如持续交付系统Spinnaker；稳定性保障工具体系Chaos Engineering（混沌工程），这里面最著名的就是那只不安分的猴子，也正是这套稳定性理念和产品最大程度地保障了Netflix系统的稳定运行；被Spring Cloud引入并得以更广泛传播的Common Runtime Service&Libraries.

#### 企业文化：Freedom&Responsibility  自由和责任并存
在这种文化的驱使下，技术团队自然会考虑从开发设计阶段到交付和线上运维阶段的端到端整体解决方案，而不会是开发就只管需求开发，后期交付和维护应该是一个叫运维的角色去考虑，No，文化使然，在Netflix是绝不允许这种情况存在的，你是开发，你就是Owner，你就要端到端负责。

## 微服务架构时代，运维体系建设为什么要以应用为核心？
> 在微服务架构模式下，我们的运维视角一定转到应用这个核心概念上来，一切要从应用的角度来分析和看待问题。

### 应用
从业务角度拆出来的每个微服务就是一个应用，他有唯一的标识符：应用名
### 应用模型及关系模型的建立
通过下面的梳理，我们就可以建立出如下这样的以应用为核心的应用模型和关联关系模型了，基于这个统一的应用概念，系统中原本分散杂乱的信息，最终都被串联了起来，应用也将成为整个运维信息管理及流转的纽带。
![Screenshot_20221103_155102.jpg](https://cdn.nlark.com/yuque/0/2022/jpeg/22983971/1667461909256-fb8aa722-14b7-4582-b2ba-6774fdd36dd0.jpeg#averageHue=%23e7ecde&from=url&id=DFJkn&originHeight=730&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=100217&status=done&style=none&title=)
#### 应用业务模型
应用业务模型，也就是每个应用对外提供的业务服务能力，并以API的方式暴露给外部。
更多聚焦在业务逻辑上，运维一般不必关注太多。
#### 应用管理模型
应用管理模型，也就是应用自身的各种属性。
应用元信息、代码信息、部署信息、脚本信息、日志信息等。
如应用名、应用功能信息、责任人、Git地址、部署结构（代码路径、日志路径以及各类配置文件路径等）、启停方式、健康检查方式等等。
应用名是应用的唯一标识，用AppName来表示。
#### 应用运行时所依赖的基础设施和组件
资源层面（IaaS）：IDC机房、机柜、机架、网络设备、服务器等。物理机、虚拟机或容器等，如果对外提供HTTP服务，就需要虚IP和DNS域名服务。
基础组件（中间件体系，PaaS）：存储和访问数据需要有数据库和数据库中间件；更快访问数据同时减轻DB压力，需要缓存；应用之间数据交互和同步，需要消息队列；文件存储和访问，需要存储系统等等。
#### 关系模型的建立
Step1.建立各个基础设施和组件的数据模型，同时识别出它们的唯一标识。
Step2.也是最关键的一步，就是识别出基础设施及组件可以与应用名AppName建立关联关系的属性，或者在基础组件的数据模型中增加所属应用这样的字段。
## 标准化体系建设
### 应用标准化体系和模型
> 标准先行！标准先行！标准先行！于纷繁复杂中抽象出标准规范的东西，是我们后续一系列自动化和稳定性保障的基础。

标准化的套路（基础设施层面的标准化&应用层面的标准化）
Step1.识别对象
Step2.识别对象属性
Step3.识别对象关系
Step4.识别对象场景（识别对象场景也就是识别出针对运维对象所实施的日常运维操作有哪些）
信息固化不是目的，也没有价值，只有信息动态流转起来才有价值。
### 基础架构标准化及服务化体系
> 我们要做的事情，可以归纳为两步：第一步是基础架构标准化，第二步是基础架构服务化。

#### 常见分布式基础架构组件
分布式服务化框架：Dubbo/Spring Cloud
分布式缓存及框架：Redis/Memcached，框架如Codis/Redis Cluster
数据库及分布式数据库框架：Mysql/Oracle/MariaDB/DRDS/Sharding-JDBC/TiDB
分布式的消息中间件：Kafka/RabbitMQ/ActiveMQ/RocketMQ
前端接入层部分：四层负载LVS/七层负载Nginx或Apache/硬件负载F5
#### 基础架构组件的选型问题
对基础架构要有统一的规划和建设。原则上，每种基础组件只允许选一种选型，至少就能满足90%甚至更多的应用场景。
比如数据库就只允许使用Mysql，然后版本统一，同时配套的中间件也必须统一，其它的关系型数据库没有特殊情况坚决不用，如果遇到特殊情况具体分析。
基础架构组件用多种会出现的问题：开发层面和运维层面，均需做大量适配工作，不同组建的经验还不能互通和传递
#### 基础架构组件的服务化
我们对基础架构组件做了标准化之后，下一步要做的就是服务化。
基于组件的原生能力进行封装，结合运维场景，将能力服务化，这样就大大提升了使用的方便性。
这个服务化的过程其实就是PaaS化的过程。换言之，如果我们能把基础架构组件服务化完成，我们的PaaS平台也就基本成型了。
## 如何从生命周期的视角看待应用运维体系建设？
> 从生命周期入手，划分阶段，提炼属性，理清关系，固化基础信息，实现运维场景。

一个对象不同生命周期阶段可能具备不同的属性、关系和场景。
对应用的生命周期阶段进行分解，大致分为五个部分，应用的创建阶段、研发阶段、上线阶段、运行阶段和销毁阶段。
做运维架构的切入点：从生命周期入手，划分阶段，提炼属性，理清关系，固化基础信息，实现运维场景。

| 生命周期阶段 | 运维职责 |
| --- | --- |
| 应用的创建阶段 | 1.最重要的工作，是确认应用的基础信息与基础服务的关系，要同时固化下来，从应用创建之初，就将应用与各类基础服务的生命周期进行挂钩。
2.另一个很重要的工作，就是要开启与应用相关的各类基础服务的生命周期。 |
| 应用的研发阶段 | 最重要的工作，是为研发团队打造完善的持续集成体系和工作链支持 |
| 应用的上线阶段 |  |
| 应用的运行阶段（应用生命周期最重要最核心的阶段） | 这个阶段应用最重要的属性就是应用本身以及相关联的基础服务的各项运行指标。
1.制定每个运维对象的SLI、SLO、SLA，同时要建设能够对这些指标进行监控和报警的监控体系
2.这里仍然会依赖到上述应用研发阶段的持续集成过程，并最终与线上发布形成持续交付这样一个闭环体系
3.出现了应用之间的依赖管理和链路跟踪的场景
4.出现了线上稳定性保障的场景（比如流量激增时的限流降级、大促前的容量规划、异常时的容灾、服务层面的熔断等等） |
| 应用的销毁阶段 | 不仅仅是应用自身要销毁，围绕着该应用所产生出来的基础设施、基础服务以及关联关系都要一并清理，否则将会给系统中造成许多无源头的资源浪费。 |

## 如何在CMDB中落地应用的概念？
> 新的时期，对CMDB的理解也要与时俱进，这个时候，思路上的转变，远比技术上的实现更重要。
> 运维能力的体现，一定是整体技术架构能力的体现，割裂两者单独去看，都是没有意义的。

CMDB，Configuration Management DataBase，配置管理数据库，是与IT系统所有组件相关的信息库，它包含IT基础架构配置项的详细信息。
随着云计算技术的蓬勃发展，逐步屏蔽了IDC、网络设备以及硬件服务器这样的底层基础设施的复杂度，有公有云或私有云厂商来专注聚焦这些问题，让运维不必再花过多的精力在这些基础设施上面。配置管理的范畴不再是简单的硬件资源配置管理，而是外延到应用以及以应用为核心的分布式服务化框架、缓存、消息、DB、接入层等基础组件。
应用的集群服务分组建设
应用管理思路：产品线-业务团队-应用-集群服务分组-资源
为什么会有集群服务分组呢？
场景一：多环境问题
开发联调环境、集成测试环境、预发环境、线上环境
场景二：多IDC问题
对于大型互联网业务，会做业务单元化，或者海外业务拓展需求的场景，我们会在多个IDC机房部署应用，应用代码是相同的，但是配置可能完全不同。
场景三：多服务分组问题
核心应用和非核心应用分组
交易支付链路上的应用属于核心应用，任何时候都必须要优先保障。
商品中心IC这个应用下面，就会有交易分组，广告分组，电商分组。
这类分组相对固定和静态
场景因素决定分组
大促时的秒杀场景
商品中心IC这个应用下面，就需要有多个不同的秒杀分组。
这类分组就需要根据实际业务场景决定，是个动态调整的过程，需要开发和运维一起来讨论和验证。
![Screenshot_20221104_100940.jpg](https://cdn.nlark.com/yuque/0/2022/jpeg/22983971/1667527823674-9cab1328-851f-4ea2-8c30-06d76bd04061.jpeg#averageHue=%23fcfcfb&from=url&id=ZnvJr&originHeight=1228&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=171508&status=done&style=none&title=)
# 效率和稳定性最佳实践
效率和稳定性最佳实践，这是运维价值的体现。围绕持续交付和稳定性建设两方面，打造不需要任何运维参与的端到端交付过程，打造稳定性保障体系。
## 持续交付
> 配置管理、提交管理、构建和部署发布是持续交付的重中之重，是关键路径，是从开发代码开始，到发布上线的必经之路。

![image.png](https://cdn.nlark.com/yuque/0/2022/png/22983971/1667638783443-12b7f411-0294-4b5c-b638-cd811f7aa69a.png#averageHue=%23d2ceae&clientId=u22309499-708c-4&from=paste&height=312&id=uac23b2c1&originHeight=390&originWidth=636&originalType=binary&ratio=1&rotation=0&showTitle=false&size=101634&status=done&style=none&taskId=ud6d6d6c9-ddda-4201-8966-5d2468f373d&title=&width=508.8)
持续交付代表着从业务需求开始到交付上线之后的端到端的过程。
### 持续交付（流水线构建）的关键点
配置管理、提交管理、构建和部署发布是持续交付的重中之重，是关键路径，是从开发代码开始，到发布上线的必经之路。
![image.png](https://cdn.nlark.com/yuque/0/2022/png/22983971/1667652156047-7e66568c-a5de-4536-bbe9-4e3983f7f3d0.png#averageHue=%23e5e5e2&clientId=u22309499-708c-4&from=paste&height=280&id=u250e79eb&originHeight=350&originWidth=835&originalType=binary&ratio=1&rotation=0&showTitle=false&size=182701&status=done&style=none&taskId=u3076d58b-952a-477b-bbd8-b7b4269080c&title=&width=668)
#### 配置管理（配置管理是基础，是关键）
前提：一定要做到代码和配置的分离
##### 版本控制（SVN/Git等版本管理工具）
主要作用：保证团队在交付软件的过程中能够高效协作，提供了一种保障机制
##### 依赖配置（Maven/Gradle/Ant等依赖管理工具）
主要作用：二方包、三方包的仓库管理；依赖管理；构建打包。
##### 软件配置（代码配置&应用配置）
代码配置和应用配置最大的区别就是看跟环境是否相关。
###### 代码配置：代码配置是跟代码运行时的业务逻辑相关的。
比如应用的服务接口、并发线程数、超时时间等这些运行时参数；还有类似于业务或技术上的开关，比如商品评论是否开放、优惠时间段设置等等。
###### 应用配置：应用配置就是应用这个对象的属性和关系信息。
我们把应用配置放到持续交付这个场景中进行分析，对于这个配置可以细分为：
应用构建时配置：编程语言、Git地址以及构建方式等
应用的部署配置：源代码目录、应用日志目录、Web日志目录、临时目录、脚本目录等
应用的运行配置：应用启停、服务上下线方式、健康检测方式等
应用运行时与基础组件的关联关系：应用依赖的DB、缓存、消息以及存储的IP地址、域名、端口、用户名或Token等。
##### 环境配置（准确地说，应该是不同环境下的应用配置管理）
环境配置管理主要是针对应用对基础设施和基础服务依赖关系的配置管理。如果是针对不同客户进行私有化部署的软件，那么应用的基本属性信息可能也会发生变化。

| 开发环境 | 开发人员进行单元测试、联调和基本的业务功能验证 |
| --- | --- |
| 集成环境 | 测试人员验证 |
| 预发环境 | 真实的生产数据环境，但不会接入线上流量 |
| Beta环境（灰度环境/金丝雀发布模式） | 引入线上万分之一或千分之一的用户流量 |
| 线上环境 | 正式环境 |

不同环境配置不同解决思路
1、多个配置文件，构建时替换
2、占位符模板模式
3、AutoConfig方案
![image.png](https://cdn.nlark.com/yuque/0/2022/png/22983971/1667651774979-aa0790fd-7bc7-46e5-a2bc-c20f94d0d1ff.png#averageHue=%23d0ceca&clientId=u22309499-708c-4&from=paste&height=382&id=ua6283930&originHeight=478&originWidth=893&originalType=binary&ratio=1&rotation=0&showTitle=false&size=474508&status=done&style=none&taskId=u983f4425-ffe3-430f-a930-f7753025bbf&title=&width=714.4)

#### 提交管理（代码分支的合并策略选择就是提交管理）
#### 构建打包（将提交后的代码编译成可发布的软件包）
![image.png](https://cdn.nlark.com/yuque/0/2022/png/22983971/1667652599995-63d0fc5c-2fed-4638-8bae-6747bfba9f61.png#averageHue=%23d2d0cc&clientId=u22309499-708c-4&from=paste&height=187&id=u7a22ccc3&originHeight=234&originWidth=873&originalType=binary&ratio=1&rotation=0&showTitle=false&size=197959&status=done&style=none&taskId=u22c982cd-d600-4fad-809c-1f9439d8c47&title=&width=698.4)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/22983971/1667652660751-9ad50b82-4ad9-4488-aaa1-27ed4cb5ab28.png#averageHue=%23dfdebc&clientId=u22309499-708c-4&from=paste&height=610&id=ue92e8984&originHeight=763&originWidth=872&originalType=binary&ratio=1&rotation=0&showTitle=false&size=364287&status=done&style=none&taskId=uf290b19a-6beb-4bd6-904c-85a4add2622&title=&width=697.6)
#### 自动化测试（功能测试和非功能性测试）
![image.png](https://cdn.nlark.com/yuque/0/2022/png/22983971/1667653895519-6797ce42-63bc-40e6-8e8d-dc3d9abc83ac.png#averageHue=%23f7f7f6&clientId=u22309499-708c-4&from=paste&height=409&id=ubfa5ed5d&originHeight=511&originWidth=878&originalType=binary&ratio=1&rotation=0&showTitle=false&size=305049&status=done&style=none&taskId=ud3c9b6b8-9188-4860-b042-0a22faa17f8&title=&width=702.4)
#### 部署发布
![image.png](https://cdn.nlark.com/yuque/0/2022/png/22983971/1667654172748-887e181a-bffb-4f21-9e56-f118cc27a231.png#averageHue=%23fcfefc&clientId=u22309499-708c-4&from=paste&height=272&id=u82e53e1f&originHeight=340&originWidth=656&originalType=binary&ratio=1&rotation=0&showTitle=false&size=170117&status=done&style=none&taskId=u3cf3fd89-eeb9-4496-abde-1f932a0d0c4&title=&width=524.8)
## 稳定性保障
### 极端业务场景下，我们应该如何做好稳定性保障？
> 对于稳定性而言，用户访问模型才是关键。这个摸不准，只有技术是没用的，这就更需要我们能够深入业务，理解业务。

#### 极端业务场景
可预测性场景：电商每年大促618、双11等，业务峰值和系统压力峰值会出现在某几个固定的时间点
策略：在系统承诺容量内，保证系统的核心功能能够正常运行，对于非核心功能进行降级。对于超出系统承诺容量的部分进行流量限流，并确保在某些异常状况下能够熔断或旁路。
不可预测性场景：突发热点事件，无法提前准备
#### 技术挑战
1、运维自动化
2、容量评估和压测
3、限流降级
熔断是被动降级；降级是指主动降级。
4、开关预案
业务功能开关&系统功能开关
5、故障模拟
6、监控体系
### 容量规划
#### 业务场景分析
> 容量规划，就是对复杂业务场景的分析，通过一定的技术手段（如压测），来达到对资源合理扩容、有效规划的过程。

![image.png](https://cdn.nlark.com/yuque/0/2022/png/22983971/1667655534016-aaf276d1-414e-43f4-bc47-687e6c690746.png#averageHue=%23d1cfcb&clientId=u22309499-708c-4&from=paste&height=96&id=u470b4d4b&originHeight=120&originWidth=874&originalType=binary&ratio=1&rotation=0&showTitle=false&size=111940&status=done&style=none&taskId=udb20d26c-54df-495c-a681-4dbfefcea29&title=&width=699.2)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/22983971/1667655496591-e2f06a4b-e502-4ffb-9eab-48a874e52dc3.png#averageHue=%23455d69&clientId=u22309499-708c-4&from=paste&height=423&id=uf23b29db&originHeight=529&originWidth=850&originalType=binary&ratio=1&rotation=0&showTitle=false&size=262606&status=done&style=none&taskId=u0ef12b8d-931a-4948-bb3a-d9981049328&title=&width=680)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/22983971/1667655630769-e03c893e-c78a-4638-ae90-8c9beaaa038b.png#averageHue=%23ceccc8&clientId=u22309499-708c-4&from=paste&height=595&id=ueb1d5a10&originHeight=744&originWidth=873&originalType=binary&ratio=1&rotation=0&showTitle=false&size=706148&status=done&style=none&taskId=u6c064842-c8a1-4d47-89a3-f81e3fc27b5&title=&width=698.4)
#### 压测系统建设
> 压力测试四维度：压测粒度、压测接口及流量构造方式、施压方式、数据读写。

![image.png](https://cdn.nlark.com/yuque/0/2022/png/22983971/1667655644741-1959344f-ac04-43c0-abdd-788b6c312a30.png#averageHue=%23d3d1cc&clientId=u22309499-708c-4&from=paste&height=120&id=BKjrX&originHeight=150&originWidth=881&originalType=binary&ratio=1&rotation=0&showTitle=false&size=186869&status=done&style=none&taskId=u8cb760b6-70d5-4489-90c9-5234ee33b7b&title=&width=704.8)
### 限流降级
> 限流降级的难点和关键还是在于整体技术栈的统一，以及后期对每个应用限流降级资源策略的准确把握和配置。

![image.png](https://cdn.nlark.com/yuque/0/2022/png/22983971/1667656297677-b1c94c39-0c4f-4de6-96a1-09e83cf92a2f.png#averageHue=%23ccc9c5&clientId=u22309499-708c-4&from=paste&height=269&id=uef8c21bc&originHeight=336&originWidth=871&originalType=binary&ratio=1&rotation=0&showTitle=false&size=290539&status=done&style=none&taskId=ubd1cb752-bf41-46b9-a84c-073edd61f97&title=&width=696.8)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/22983971/1667656435062-d8c834bc-4efb-4f13-972c-99dd3657174b.png#averageHue=%23d4d3ce&clientId=u22309499-708c-4&from=paste&height=277&id=udbbc6c5b&originHeight=346&originWidth=850&originalType=binary&ratio=1&rotation=0&showTitle=false&size=408110&status=done&style=none&taskId=u1f1ae0a2-ebc6-44f1-995b-55f4924bec6&title=&width=680)
常见的限流解决方案

| 接入层限流 | Nginx限流
API路由网关模式 |
| --- | --- |
| 应用限流 |  |
| 基础服务限流 | 主要针对数据库、缓存以及消息等基础服务组件的限流而设定 |

几个关键的技术点
![image.png](https://cdn.nlark.com/yuque/0/2022/png/22983971/1667656732560-b43b41fa-fe50-4aaf-bb43-e0d925c5aa64.png#averageHue=%23d0cec9&clientId=u22309499-708c-4&from=paste&height=619&id=ua1489e55&originHeight=774&originWidth=857&originalType=binary&ratio=1&rotation=0&showTitle=false&size=735974&status=done&style=none&taskId=u975baca0-a26a-48d6-8859-08946c852fb&title=&width=685.6)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/22983971/1667656760361-47262ac5-b1b9-4ec0-b53b-8b90d0980a56.png#averageHue=%23f8f8f8&clientId=u22309499-708c-4&from=paste&height=402&id=u49cf988e&originHeight=502&originWidth=786&originalType=binary&ratio=1&rotation=0&showTitle=false&size=101819&status=done&style=none&taskId=ue56c0365-a87d-42b3-b0d7-18d7adbee87&title=&width=628.8)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/22983971/1667656805874-42cca2aa-b880-4293-a951-0bed48bd5bde.png#averageHue=%23d1cfca&clientId=u22309499-708c-4&from=paste&height=646&id=u0a2d8930&originHeight=808&originWidth=857&originalType=binary&ratio=1&rotation=0&showTitle=false&size=804812&status=done&style=none&taskId=u85cd10e8-0d41-4246-9bdc-eb43e77874e&title=&width=685.6)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/22983971/1667656824141-4ba536e8-6f8d-4e76-a771-ae7f53b3cbff.png#averageHue=%23f9f9f9&clientId=u22309499-708c-4&from=paste&height=330&id=u21659994&originHeight=412&originWidth=876&originalType=binary&ratio=1&rotation=0&showTitle=false&size=114331&status=done&style=none&taskId=uda38a5e1-9d58-4a89-817d-61a8782cd04&title=&width=700.8)
### 开关和预案
> 开关，主要是针对单个功能的启用和停止进行控制，或者将功能状态在不同版本之间进行切换。
> 预案，可以理解为让应用或业务进入到某种特定状态的复杂方案执行。

![image.png](https://cdn.nlark.com/yuque/0/2022/png/22983971/1667657013634-15ae24ff-6871-490b-8649-809223512c43.png#averageHue=%23f2f2f1&clientId=u22309499-708c-4&from=paste&height=226&id=ufda3d926&originHeight=282&originWidth=873&originalType=binary&ratio=1&rotation=0&showTitle=false&size=216492&status=done&style=none&taskId=u005e1cfc-f278-4e31-b147-5d023d00792&title=&width=698.4)
### 全链路跟踪系统，技术运营能力的体现
> 我们做全链路跟踪系统，要解决的首要问题就是在纷繁复杂的服务调用关系中快速准确的定位问题。

关于这一块的技术解决方案，在Google的Dapper论文发表之后，近些年业界已经有非常多且成熟的实践经验和开源产品。
比如阿里的鹰眼系统；比如国内分布式监控技术专家吴晟创建的开源项目Skywalking。还有大量优秀商业产品，通常叫APM，应用性能管理系统。
![image.png](https://cdn.nlark.com/yuque/0/2022/png/22983971/1667657429190-a807f88e-1e08-400a-bdbd-7a3a19c17f31.png#averageHue=%23d1cfcb&clientId=u22309499-708c-4&from=paste&height=208&id=u9a663cff&originHeight=260&originWidth=887&originalType=binary&ratio=1&rotation=0&showTitle=false&size=267382&status=done&style=none&taskId=ubab903a0-edd1-4bfd-a2ed-a4f8e93f1f5&title=&width=709.6)
#### 技术运营场景
1、问题定位和排查
2、服务运行状态分析（服务运行质量、应用和服务依赖、依赖关系的服务质量）
3、业务全息
业务全息就是全链路跟踪系统与业务信息的关联。
![image.png](https://cdn.nlark.com/yuque/0/2022/png/22983971/1667657638775-79cdb3fa-d34c-4d14-9337-dc6c64e61b8d.png#averageHue=%23d3d1cc&clientId=u22309499-708c-4&from=paste&height=125&id=ub155313b&originHeight=156&originWidth=870&originalType=binary&ratio=1&rotation=0&showTitle=false&size=167705&status=done&style=none&taskId=ue5d90dd7-af7a-491b-b8ea-70ca0429166&title=&width=696)
## 故障管理
> 系统正常，只是该系统无数异常情况下的一种特例。故障永远只是表面现象，其背后技术和管理上的问题才是根因。
> 
> 异常与故障的区别
> 异常：不同于平常。但不一定出现故障。
> 故障：不可用。一定出现了异常。

![image.png](https://cdn.nlark.com/yuque/0/2022/png/22983971/1667657801589-99c2ba01-5aa9-413b-a95c-49841b7aca05.png#averageHue=%23c8c6c1&clientId=u22309499-708c-4&from=paste&height=118&id=u1ea83625&originHeight=147&originWidth=871&originalType=binary&ratio=1&rotation=0&showTitle=false&size=178389&status=done&style=none&taskId=ua1ea48c7-04e8-4a3d-9f19-e905b9944ef&title=&width=696.8)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/22983971/1667657830640-aa82e218-091c-4da5-870d-b7611610096c.png#averageHue=%23d2d0cb&clientId=u22309499-708c-4&from=paste&height=442&id=ud30f8d80&originHeight=553&originWidth=874&originalType=binary&ratio=1&rotation=0&showTitle=false&size=554404&status=done&style=none&taskId=uc582eadb-00ba-43ba-b418-608dcc46dce&title=&width=699.2)
### 故障应急
> 凡是没有演练过的预案，都是耍流氓。故障模拟和恢复演练要下在平时，注意建设各种工具和平台，同时要尽可能地思考和模拟各种故障场景。

第一原则：优先恢复业务，而不是定位问题
![image.png](https://cdn.nlark.com/yuque/0/2022/png/22983971/1667658303803-13014248-7229-4dfd-b4f9-141a94fd9f1e.png#averageHue=%23ceccc7&clientId=u22309499-708c-4&from=paste&height=610&id=u1b0bf8b1&originHeight=762&originWidth=892&originalType=binary&ratio=1&rotation=0&showTitle=false&size=686194&status=done&style=none&taskId=u735c97c8-73a6-4149-9106-44991135b2f&title=&width=713.6)
### 故障复盘
![image.png](https://cdn.nlark.com/yuque/0/2022/png/22983971/1667658156028-05390796-a0f9-4b93-8a8f-ba975904d3ef.png#averageHue=%23cfcdc9&clientId=u22309499-708c-4&from=paste&height=615&id=u36f931cb&originHeight=769&originWidth=877&originalType=binary&ratio=1&rotation=0&showTitle=false&size=771039&status=done&style=none&taskId=uefdcf9db-a933-480d-9b83-62134dfbce7&title=&width=701.6)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/22983971/1667658169255-0144cd92-09d3-43d4-8d53-fd8ca746c0e6.png#averageHue=%23cfcdc8&clientId=u22309499-708c-4&from=paste&height=298&id=u5179b274&originHeight=372&originWidth=880&originalType=binary&ratio=1&rotation=0&showTitle=false&size=393639&status=done&style=none&taskId=udd50b1e9-41c6-449c-9ff2-a617393c4ff&title=&width=704)
## 运维与安全
> 在双方（运维与安全）工作的协作上，我一直认为运维不能只是被动响应，而应该主动与安全合作，共建安全体系，与运维体系融合，把防线建设好，从源头控制。

# 云计算时代的运维实践
混合云、云存储、静态化以及CDN的实践经验
## 选择云服务的理由
> 如果想要技术为业务带来更多的可能性，拥抱云计算是最好的选择。

所面临的问题
1.成本闲置问题
2.基础设施维护问题
3.底层技术投入和人才的问题

纵观技术发展趋势
1.软件架构发展趋势：物理机->虚拟机->Docker->Serverless
随着云计算的不断发展，对于资源的依赖越来越少
Serverless就是在公有云平台上提升资源利用率衍生出来的，它也只有在公有云上才有意义。在私有云，或者是自建或托管IDC中，因为资源规模问题，没有看到太多的实践价值。
2.未来人工智能的发展和应用，必然会依托于云计算。
## 页面静态化架构和二级CDN建设
> 公有云也好，云计算也好，都不能为我们提供完美的定制解决方案。正所谓具体问题具体分析，找出问题，优化解决路径，量体裁衣，才能得到最适合我们的“定制方案”。

### CDN：静态内容，就近访问原则
通常意义上讲的CDN，更多是针对静态资源类的内容分发网络，最典型的就是电商的各类图片，还有JS和CSS这样的样式文件。通过CDN能够让用户就近访问，提升用户体验。这类文件只是以单纯的资源存在，与业务逻辑没有强关联。
### 页面静态化架构
把静态化的内容提取出来单独存放，业务请求时直接返回，而不用再通过调用应用层接口的方式，去访问缓存或查询数据库，那访问效率一定是会大幅提升的。
ATS，Apache Traffic Server，是一个开源产品，本质上跟Nginx、Squid以及Varnish这样的HTTP反向代理是一样的。但是它能对动静态分离的场景提供很好的支持。
![Screenshot_20221104_114115.jpg](https://cdn.nlark.com/yuque/0/2022/jpeg/22983971/1667533337226-077b15ea-f6e7-446e-84c7-1c3eb85813f1.jpeg#averageHue=%23e4d3c0&from=url&id=usQCi&originHeight=1085&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=233037&status=done&style=none&title=)
### 二级CDN建设：静态化与公有云相结合的方案
![Screenshot_20221104_114048.jpg](https://cdn.nlark.com/yuque/0/2022/jpeg/22983971/1667533335848-ce917890-16fa-4a30-82b9-e58c42c080df.jpeg#averageHue=%23fdfdfc&from=url&id=DeQRN&originHeight=608&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=45605&status=done&style=none&title=)
## 弹性伸缩
> 对于运维，一定要准确识别出日常运维过程中不同的运维对象，然后在进一步去分析这个对象所对应的运维场景是什么，进而才是针对运维场景的分解和开发。

弹性伸缩是一个运维场景，场景的主体可以有很多种，例如资源、服务器、容量、应用以及业务等等。
弹性伸缩=水平扩展=自动化扩缩容
我们在日常思考和工作中应该注意以下两点。
第一，一定是从实际问题出发，找到问题的主体，然后才是针对问题的解决方案。
要反复问自己和团队，我们解决的问题是什么？解决的是谁的问题？切记，一定不要拿着解决方案来找问题，甚至是制造问题。
比如弹性扩容这个概念，它就是解决方案，而不是问题本身，问题应该是：业务服务能力不足时，如何快速扩容？业务服务能力冗余时，如何释放资源，节省成本？按照这个思路，我们自然就提炼出业务服务能力这个主体，面对的场景是快速扩缩容，然后针对场景进一步细化和分解。
第二，如果问题处于初期，且是发散状态时，主体可能表现出很多个，这时我们一定要找到最本质的那一个，往往这个主体所涉及的运维场景就包括了其它主体的场景。
## 云计算和AI带给我们的挑战
云计算发展到今天，已经不是我们想象中的只能提供IaaS服务的云平台了，目前各大公有云上的PaaS产品体系也已经非常完善，各类分布式中间件产品都有覆盖，而且这些产品，还都是各大公有云平台公司在自有业务上锤炼出来的非常优秀的产品。
简单一句话，现在我们去做一个业务，基于这些基础服务，完全无需自研纯技术产品，只要专注业务逻辑开发即可。我了解到国内某新兴的O2O，每日超过千万笔的订单量，除业务代码外，其它基础层面的服务就完全依赖于某大型公有云的IaaS、PaaS以及周边的各类服务体系。
这种情况下，非但不需要大量的如SA、网络工程师、DBA以及应用运维这些岗位，就连技术门槛较高的分布式中间件研发岗位也会大量缩减，所以这个挑战和危机就会非常大了。
AI和Ops的结合，更多还是场景驱动的。就是我们要处理的数据量越来越多，面对的场景越来越复杂，而且会大大超出我们人力的认知范畴。比如BAT这样的公司，几十万台服务器的规模，出现一个问题，我怎么能够快速发现，快速定位，并最终快速恢复？如果是几百甚至几千台服务器，靠人还是可以搞定的，但是几十万台，靠人就不可能了。
## 运维需要懂产品和运营吗？
> 我们强调的是运维要有产品和运营意识，总结起来最本质的就两点：第一，能将需求讲清楚；第二，能将产品推广落地。


# 其他


学习是一个从厚到薄的过程。

软件架构的目的，是将构建和维护所需的人力资源降到最低。

总结回顾是最好最快的提升方式。而总结回顾最好的方式是写作。希望你可以养成记录日志和博客的习惯，真的会受益匪浅。

要能学以致用。

教学相长，教给别人的时候，自己领悟的更深刻。

故障模拟 Netflix的Chaos Engineering，其中的Chaos Monkey，就是专门搞线上破坏，模拟各种故障场景

全链路跟踪（也称分布式链路跟踪）关于Google的Dapper论文发表之后，近些年业界已经有非常多且非常成熟的实践经验和开源产品。

想深入了解相关内容，推荐极客时间上陈皓老师的《左耳听风》和杨波老师的《微服务架构核心20讲》，两位都是骨灰级的微服务和分布式架构专家

RT：响应时间

《SRE：Google运维解密》这本书绝大部分章节就是在介绍故障相关的内容
从本质上讲，SRE的岗位职责在很大程度上就是应对故障

故障是一种常态，系统正常只是该系统无数异常情况下的一种特例

稳定性保障，在故障隔离、快速恢复、容灾切换上做好

Design for Failure理念：我们的目标和注意力不应该放在消除故障，或者不允许故障发生上，因为我们无法杜绝故障。所以，我们更应该考虑的是，怎么让系统更健壮，在一般的问题面前，仍然可以岿（kui，一声）然不动，甚至是出现了故障，也能够让业务更快恢复起来。

故障只是表象，其背后技术和管理上的问题才是根因。

论文价值思考：有故障快速察觉（监控&告警），快速根因定位（定位效率高），快速恢复业务
告警可以往后放，先尝试自己解决，如果解决不了，再进行告警（避免告警太多，人员麻痹）
给故障定级，优先排查级别高的故障（定级可以设置），不通故障定级，在故障应对时采取的策略也就不同。一般来说，P2及以上故障就需要所有相关责任人马上上线处理，并及时恢复业务。对于P3或P4的问题，要求会适当放宽。


对象：运行中的应用
出现故障/故障模拟->异常检测->监控、告警->故障定级（根据故障定级标准，快速做出初步判断，确认影响面以及故障等级）->恢复演练（验证预案可用）->根因定位->故障复盘、故障定责
获取故障渠道：监控、告警、业务反馈、用户商家投诉

故障生命周期
发生前：故障演练（故障模拟和恢复演练）
发生时：故障应急（应急预案）
发生后：故障复盘（根因定位，定级定责）

现有问题：
1.告警太频繁，人员麻痹（面对繁多的报警信息，运维人员应该如何处理）
2.服务数量呈指数级增长
3.故障发生时，如何迅速定位问题
《[AIOps是运维发展的必然趋势？](https://time.geekbang.org/column/article/1365)》
AIOps 就是希望基于已有的运维数据（日志、监控信息、应用信息等）并通过机器学习的方式来进一步解决自动化运维没办法解决的问题。
就目前来看，国内的百度、搜狗、宜信、阿里巴巴都已经探索尝试了 AIOps，并且取得了不错的收益。在 2017 年 InfoQ 举办的 CNUTCon 全球运维技术大会上，也有不少 AIOps 相关的议题，甚至会议主题也从去年的容器生态迭代到今年的智能时代的新运维，感兴趣的读者可以关注。

随着业务体量快速膨胀，衍生出对稳定性有极高的要求，这时我们现在长听到的全链路跟踪、容量评估、限流降级、强弱依赖等稳定性的解决方案就涌现出来。

云计算发展，传统的网络、硬件和系统维护的职责在逐渐的被弱化，也在逼迫着运维的关注点从底层转向应用和业务层面。所以，我们看到就在近 2-3 年，自动化、发布系统、稳定性平台这些系统成为了运维团队重点关注和建设的部分。

回到 AIOps 上来，当前这个阶段，现实情况，系统里面已经有大量软硬件模块、日志、监控告警指标也纷繁复杂，一方面是无法在问题萌芽状态就发现问题，无法提前做出预判，另一方面是发生了问题又无法快速确定根因，造成持续的资损。技术发展上，随着计算能力、数据量的积累、以及机器算法的进步，如何更加高效的开展 Ops 这个问题就摆在我们面前，AIOps 的模式应运而生。

InfoQ：AIOps 的出现是为了解决哪些问题？这些问题运维自动化无法解决吗？
赵成：主要还是解决复杂环境下问题的快速发现甚至提前预判，以及出现问题后的如何在复杂的告警、报错和日志中快速进行根因分析。（快速发现问题和快速判断根因，甚至提前预判）
运维自动化无法解决吗？我的理解，AI 和 Ops 要解决的还是两个层面的问题，可以类比到人，AI 相当于人的大脑，我们手脚和躯干是执行系统，大脑负责决策判断，手脚躯干负责完成大脑下发的动作指令。对应到运维上面，AI 要解决的是怎么快速发现问题和判断根因，而问题一旦找到，就需要靠我们高度完善的自动化体系去执行对应的运维操作，比如容量不够就扩容、流量过大就应该触发限流和降级等等。AI 是能够让 Ops 执行的更加高效的强大助推力，下面是我之前整理出来的，我理解的 AIOps 的体系和建设思路。
AI 是能够让 Ops 执行的更加高效的强大助推力，下面是我之前整理出来的，我理解的 AIOps 的体系和建设思路。
![image.png](https://cdn.nlark.com/yuque/0/2022/png/22983971/1667206895899-4f364534-f60d-4ad9-930c-40df5b09de67.png#averageHue=%23f2f5f3&clientId=u9c9aa764-f0dc-4&from=paste&id=ufc6e417c&originHeight=635&originWidth=474&originalType=url&ratio=1&rotation=0&showTitle=false&size=179982&status=done&style=none&taskId=uee761985-1fa8-40c7-b37b-f11887191e9&title=)

InfoQ：可否谈谈你们的 AIOps 落地场景？赵成：这块我们还在实践中，一块是异常检测，做一些关键监控 Metrics 的曲线监控，这块用到的基本是常见的指数平滑、3-Sigma 算法等。另一块是根因分析，在服务化的架构中，最头痛的还是出现了故障，无法快速的定位原因。大致思路是，根据全链路跟踪系统的每一次请求的依赖关系，做调用的关联度分析，当一个模块出现问题时，会同时导致依赖这个模块的所有模块都会告警，甚至还有业务层面的告警，这时就需要快速的根因分析，确定问题在哪儿。
极客时间版权所有: https://time.geekbang.org/column/article/1365

《[AI 时代，我们离 AIOps 还有多远？](https://www.infoq.cn/article/2017/08/AI-how-long-AIOps)》

# 清华裴丹：AIOps 落地路线图
[https://www.infoq.cn/article/e058GR977BowXj6bmSTa](https://www.infoq.cn/article/e058GR977BowXj6bmSTa)
异常检测、异常定位、根因分析、异常预测
推荐阅读：Google搜索，清华大学裴丹老师的《基于机器学习的智能运维》

[https://www.infoq.cn/](https://www.infoq.cn/)搜索赵宇辰即可


AI发挥的作用是，动态变化场景的复杂条件下，能够做出高效准确的决策判断。回到运维上来，我们现在常看到的监控告警、根因分析、日志异常检测、报警聚合、容量预测、故障预测等等，这些都是要基于海量的线上运行时数据，做出分析判断的，所以在这一块，我们会看到大量的跟AI结合的AIOps的解决方案，特别是智能监控。