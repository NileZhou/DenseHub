
# 数据脱敏([desensitization）](http://wiki.intra.xiaojukeji.com/pages/viewpage.action?pageId=727058978)

## [《国际化PII分级定义》](http://wiki.intra.xiaojukeji.com/pages/viewpage.action?pageId=693769551)




原版参考- [1、PII 分级定义](http://wiki.intra.xiaojukeji.com/pages/viewpage.action?pageId=509489746)
结合实际业务场景和使用频度，针对PII字段进行分级定义，本次改造范围限定为高风险九类P0和P1
【P0 ：Sensitive PII】、【P1 ：General PII】、【P2 ：other PII】

| **PII 类型 (9类)** | **风险级别** | **脱敏要求** | **用户自身查询** | **员工查询** | **数据存储** | **备注** |
| --- | --- | --- | --- | --- | --- | --- |
| **PII 类型 (9类)** | **风险级别** | **脱敏要求** | **用户自身查询** | **员工查询** | **数据存储** | **备注** |
| 身份证件号 | P0 | 强制 | 单向掩码 | 双向加密 | 双向加密 | 

 |
| 银行卡号 | P0 | 强制 | 单向掩码，二次校验 | 双向加密 | 双向加密 | 

 |
| 驾驶证号 | P0 | 强制 | 单向掩码 | 双向加密 | 双向加密 | 

 |
| 精确位置 | P0 | 强制 | 单向掩码 | 单向掩码 | 双向加密 | 地图轨迹目前可以展示 |
| 税号 | P0 | 强制 | 单向掩码 | 双向加密 | 双向加密 | 

 |
| 手机号 | P1 | 强制 | 单向掩码 | 双向加密 | 双向加密 | 

 |
| 电子邮箱 | P1 | 强制 | 单向掩码，二次校验 | 双向加密 | 双向加密 | 

 |
| 姓名 | P1 | 强制 | 单向掩码 | 单向掩码 | 双向加密 | 

 |
| 车牌号 | P1 | 强制 | 单向掩码 | 双向加密 | 双向加密 | 

 |
| IP地址 | P2 | 建议 | 不能查询 | 单向掩码 | 双向加密 | 

 |
| MAC地址 | P2 | 建议 | 不能查询 | 不能采集 | 不能采集 | 

 |
| IMEI | P2 | 建议 | 不能查询 | 不能采集 | 不能采集 | 

 |
| IMSI | P2 | 建议 | 不能查询 | 不能采集 | 不能采集 | 

 |



## [《国际化PII脱敏标准》](http://wiki.intra.xiaojukeji.com/pages/viewpage.action?pageId=693769484)

单向掩码，不变长；双向脱敏，整个字符串会根据加密算法变长
【P0 ：Sensitive PII】、【P1 ：General PII】、【P2 ：other PII】
完整版参考：[https://cooper.didichuxing.com/docs/sheet/2199082862552#LNvaj](https://cooper.didichuxing.com/docs/sheet/2199082862552#LNvaj)

| **PII 类型** | **级别** | **要求** | **加密字段（GB为例）** | **兜底处理** | **加密算法** | **示例** | **单向掩码示例** | **双向加密示例（保留后四位）** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 身份证件号 | P0 | 强制 | 2，2 | 中间50% | D_FPE → AES | SC204987K | SC*****7K | F1B_zjidL987K |
| 银行卡号 | P0 | 强制 | 0，4 | 前75% | D_FPE → AES | 3714 4963 5398 4311 | **** **** **** 4311 | D1C_1Hez2D3RXJEf8tx4311 |
| 驾驶证号 | P0 | 强制 | 5，4 | 中间50% | D_FPE → AES | SMITH609258W99XT 45 | SMITH*********XT 45 | F1D_lFtCtLpzeuEBO5cT 45 |
| 精确位置 | P0 | 强制 | 逗号前第一个单词 | 前20% | 优先短地址、展现飘移 | 34 Dunster Gardens, St. Johns Street, John's Wood, London, NW8 7SG, UK | *****, St. Johns Street, John's Wood, London, NW8 7SG, UK | 无 |
| 税号 | P0 | 强制 | 4，3 | 中间50% | D_FPE → AES | GB887372864 | GB88****864 | F1F_4ZyPsyf2864 |
| 手机号 | P1 | 强制 | 3，4 | 中间30% | D_FPE → AES | (+44)07400 911050 | (+44)0******1050 | D1H_25c6uAYvsHkk41050 |
| 电子邮箱 | P1 | 强制 | fisrt word first char | wu | D_FPE → AES | henderson@[gmail.com](http://gmail.com/) | h*******n@[gmail.com](http://gmail.com/) | [f1I_57pm9kpb0@gmail.com](mailto:f1I_57pm9kpb0@gmail.com) |
| 姓名 | P1 | 强制 | 保留第一个单词 | 第一个单词 | AES | Henderson Jafferson James

 | Henderson** ********* ******* | A1J_=QuMQt5OPzGd1bgvASrOAg=7ames |
| 车牌号 | P1 | 强制 | 加密-3至-5 | 中间40% | D_FPE → AES | BD51SMR | BD***MR | A1K_=2J0PbcutkplethgKIAKxw=3 SMR |
| IP地址 | P2 | 建议 | 后30% | 后30% | D_FPE | 

 | 

 | 

 |
| MAC地址 | P2 | 建议 | 后30% | 后30% | D_FPE | 

 | 

 | 

 |
| IMEI | P2 | 建议 | 后30% | 后30% | D_FPE | 

 | 

 | 

 |
| IMSI | P2 | 建议 | 后30% | 后30% | D_FPE | 

 | 

 | 

 |



**端侧位置数据展示标准：**

| **APP** | **展示位置** | **UK** | **非UK国家** | **新开国** |
| --- | --- | --- | --- | --- |
| 乘客端 | 所有页面 | 长地址 | 长地址 | （根据当地法规判断）
1. 有隐私政策或个人数据保护相关规定的国家按照UK标准执行
2. 无隐私政策或个人数据保护相关规定的国家按照非UK国家标准执行 |
|  | 发票或收据 | 长地址 | 长地址 |  |
| 司机端 | 播单卡 | 隐藏地址 | 长地址 |  |
|  | 行程中 | 长地址 | 长地址 |  |
|  | 历史行程页 | 隐藏地址 | 隐藏地址 |  |
|  | 发票或收据 | 隐藏地址 | 隐藏地址 |  |

## 附录
通过AES+Base64编码后，针对给定的明文长度，其加密后输出的密文长度是变长范围如下：

| **明文长度（字节）** | **密文长度（字节）** |
| --- | --- |
| 0-15 | 28 |
| 16-31 | 48 |
| 32-47 | 68 |
| 48-63 | 92 |
| 64-79 | 112 |

如果明文是n字节长，则aes+base64后的密文长度，最长是 （n+16+2)/3*4 + 4 = 4n/3 + 28。



## [《脱敏改造手册》](http://wiki.intra.xiaojukeji.com/pages/viewpage.action?pageId=727059018)

### 一、展现层脱敏改造
原wiki参考：[2、【PRD】接入手册](http://wiki.intra.xiaojukeji.com/pages/viewpage.action?pageId=511548939)
服务端直接接入SDK改造即可，参考：[接口文档](https://z.didi.cn/4ZVoH)

### 二、存储层脱敏改造
原wiki参考：[08、改造手册](http://wiki.intra.xiaojukeji.com/pages/viewpage.action?pageId=584223977)
方案概述：
1、删除脱敏数据【最彻底】：推荐非必须的PII信息直接删除，从用户中心或者固定的几个接口内读取。
2、新增密文数据【最稳定】：新增密文字段，使用SDK加解密，[SDK接口文档](http://10.96.90.240:8801/manual/api/go/)，双写双读切换新字段。


# [数据跨境（crossborder）](http://wiki.intra.xiaojukeji.com/pages/viewpage.action?pageId=727058995)

## [《国际化数据跨境最佳实践和军规》](http://wiki.intra.xiaojukeji.com/pages/viewpage.action?pageId=693769517)


---

**五条军规摘要**：
1) 中国个人数据和重要数据不允许出境，若有业务需要必须出境的，需通过信息安全评估，并向监管部门报备。（出境）
2) 海外用户敏感个人数据、直接识别个人数据、间接识别个人数据不允许入境，脱敏处理并经信息安全评估后方可入境。（入境）
 3) 海外员工个人敏感数据、员工个人身份数据、员工个人联系数据、员工个人背景数据不允许入境，脱敏处理并经信息安全评估后方可入境。（入境）
4) 欧洲机房与美东机房之间不允许明文个人数据跨境传输，个人数据脱敏处理后方可传输。（跨境）
5) 业务数据和公司数据允许入境。（入境）


---

### 1. 目的
根据各国数据保护法律法规(GDPR、LGPD等)、中国法律法规（个人信息保护法、数据安全法、网络安全法、汽车数据安全管理若干规定）和公司相关数据保护制度，为明确国际化数据出境和入境的合规管控要求，特制定此规定。
### 2. 适用范围
本军规适用于为开展国际化业务而产生的数据跨境活动。
### 3.术语定义
1） **个人数据：**指任何已识别或可识别的自然人（“数据主体”）的相关信息，或以电子或者其他方式记录的与已识别或者可识别的车主、驾驶人、乘车人、车外人员等有关的各种信息，不包括匿名化处理后的信息。
2） **重要数据：**指一旦泄露可能直接影响国家安全、经济安全、社会稳定、公共健康和安全的数据，如未公开的政府信息，大面积人口、基因健康、地理、矿产资源等。重要数据的定义和范围还应根据法律法规、监管政策及行业规范中的具体范围进行划定。
3） **业务数据：**公司业务开展所需要的数据，如订单信息、交易详情，定价策略、营销策略等数据或文档。
4） **公司数据：**公司经营管理所需要的数据和产品，如经营战略、财务信息、并购及融资信息、系统的账号和密码、产品核心算法以及源代码等数据或文档。
5） **数据出境：**在中国境内收集和产生的个人数据和重要数据传到海外，或被海外员工访问。
6） **数据入境：**在中国境外收集和产生的个人数据传到中国境内，或被中国境内员工访问。
7） **数据跨境：**包括数据出境、数据入境和海外各国之间数据跨境处理。
### 4. 管理原则
**1）强意识**
先识别业务或系统是否涉及个人数据和重要数据，再联系信安同学评估、评估后准入
**2）控流程**
 遵循[《数据出入境白名单管理规范》](http://wiki.intra.xiaojukeji.com/pages/viewpage.action?pageId=682838502)，默认拒绝所有个人数据和重要数据的跨境传输和访问，并做到最小授权和严格审计
**3）重责任**
谁生产谁负责，谁审批谁监督、谁污染谁治理
### 5. 军规细则
1) 中国个人数据和重要数据不允许出境，若有业务需要必须出境的，需通过信息安全评估，并向监管部门报备。（出境）
2) 海外用户敏感个人数据、直接识别个人数据、间接识别个人数据不允许入境，脱敏处理并经信息安全评估后方可入境。（入境）
 3) 海外员工个人敏感数据、员工个人身份数据、员工个人联系数据、员工个人背景数据不允许入境，脱敏处理并经信息安全评估后方可入境。（入境）
4) 欧洲机房与美东机房之间不允许明文个人数据跨境传输，个人数据脱敏处理后方可传输。（跨境）
5) 业务数据和公司数据允许跨境。（跨境）

### 附录A：海外用户个人数据示例
| **数据类别** | **二级分类** | **三级分类** | **级别** | **示例** |
| --- | --- | --- | --- | --- |
| 用户个人数据 | 用户敏感个人数据 | 生物识别数据 | C4 | 人脸图、头像、录像、录音、手持证件照 |
|  |  | 健康/犯罪数据 | C4 | 疫情数据、无犯罪记录证明、毒品检测、毒理学检测、视力检测 |
|  | 直接识别个人数据

 | 个人身份数据 | C4 | 身份证号、驾驶证号、工作证号、税号、网约车资质证号、社保卡号、证件图片 |
|  |  | 个人联系数据 | C4 | 手机号、电子邮箱、联系地址、邮编 |
|  |  | 个人财产数据 | C4 | 银行账号、银行卡信息、银行卡图片 |
|  |  | 个人定位数据 | C4 | 个人定位地址、行踪轨迹 |
|  |  | 认证授权数据 | C4 | 个人登录密码、APP签名、数字签名及密钥key |
|  | 间接识别个人数据 | 个人基本数据 | C3 | 姓名、昵称、性别、生日、国籍、社交账号 |
|  |  | 个人设备/浏览器数据 | C3 | MAC（不允许收集）、IMEI（不允许收集）、IMSI、Android ID、GAID、IDFA、GUID、IP、Cookies、Other DeviceID |
|  |  | 车辆数据 | C3 | 车牌号、车辆识别代码、行驶证号、车辆许可证、车辆登记证、保险有效期 |
|  |  | 个人票据数据 | C3 | 发票、行程单、收据 |
|  |  | 其他资质数据 | C3 | 能力测试、人权证明 |
|  |  | 服务数据 | C3 | 评分数据、费用数据、交易记录、疲劳监测数据、用户输入信息（询问、投诉和调研等） |
|  | 其他个人数据 | 其他设备数据 | C2 | 手机厂商、CPU架构、处理器核心数、内存、硬盘、屏幕分辨率、运营商、运营商、UTC时区 |
|  |  | 其他个人基本数据 | C2 | 国家、城市、用户交互数据（点击量、访问量等） |



### 附录B：海外员工个人数据示例
| **数据类别** | **二级分类** | **三级分类** | **级别** | **示例** |
| --- | --- | --- | --- | --- |
| 员工数据 | 员工个人敏感数据 | 健康/犯罪记录 | C4 | 无犯罪记录 |
|  |  | 种族 | C4 | 种族 |
|  | 员工重要个人数据 | 员工身份数据 | C4 | 证件号、证件附件、税号 |
|  |  | 员工联系数据 | C4 | 手机号、个人邮箱、现居详细地址 |
|  |  | 员工财务数据 | C4 | 银行卡信息、薪酬、股权 |
|  |  | 绩效考核数据 | C4 | 职级、绩效 |
|  |  | 员工监控数据 | C4 | CCTV监控、LCA监控、邮件监控 |
|  | 员工一般个人数据 | 员工基本数据 | C3 | 姓名、用户名、昵称、生日、年龄、头像、工卡照、出生国家/地区、婚姻状况、出生城市、爱好、星座、国籍 |
|  |  | 员工教育数据 | C3 | 学历、毕业院校 |
|  |  | 员工工作数据 | C3 | 工龄、工作许可文件编号、职称 |



### 附录C：中国重要数据示例
| **数据类别** | **二级分类** | **级别** | **示例** |
| --- | --- | --- | --- |
| 重要数据 | 重要敏感区域数据 | C4 | 军事管理区、国防科工单位以及县级以上党政机关等重要敏感区域的地理信息、人员流量、车辆流量等数据 |
|  | 经济运行情况数据 | C4 | 车辆流量、物流数据等 |
|  | 运行数据 | C4 | 汽车充电网的运行数据 |
|  | 视频/图像数据 | C4 | 人脸信息、车牌信息等的车外视频、图像数据 |
|  | 主体个人信息 | C4 | 涉及个人信息主体超过10万人的个人信息 |
|  | 其他重要数据 | C4 | 国家网信部门和国务院发展改革、工业和信息化、公安、交通运输等有关部门确定的其他可能危害国家安全、公共利益或者个人、组织合法权益的数据，如金融数据、测绘数据等 |



### 附录D：业务数据示例
| **数据类别** | **二级分类** | **三级分类** | **级别** | **示例** |
| --- | --- | --- | --- | --- |
| 业务数据 | 业务重要信息 | 用户数 | C3 | 注册乘客数、注册司机数、新增乘客数、新增司机数 |
|  |  | 订单统计信息 | C3 | 完成订单数、抢单成功订单数、评论订单数、爽约订单数、重发单数、作弊订单数、xx天呼叫专车订单数…… |
|  |  | 地图数据 | C3 | 经纬度、POI |
|  |  | 奖励信息 | C3 | 补贴信息、券信息、红包信息、积分信息 |
|  |  | 服务定价 | C3 | 起步价、平台加价、动调价格 |
|  | 非敏感业务信息 | 点击量统计 | C2 | 手机验证页点击pv、基本信息页点击pv、上传资料页点击uv、设置密码页点击uv |
|  |  | 逻辑判断数据 | C2 | 实体层级 （1：大区 2：城市 3：行政区、县）；合同: （1未签2签订）；淘汰: （0 未淘汰 1 淘汰） |
|  |  | 距离 | C2 | 公司距离、平均成交距离、抢单距离、订单距离 |
|  |  | 统计时间 | C2 | 各类统计的（日、月、年）信息 |
|  |  | ID类信息 | C2 | 用户信息ID、交易信息ID、活动信息ID、城市ID、订单ID |
|  | 公开信息 | 时间 | C1 | 日、月、年 |
|  |  | 币种 | C1 | 人民币、美元 |

### 附录E：公司数据示例


| **数据类别** | **二级分类** | **三级分类** | **级别** | **示例** |
| --- | --- | --- | --- | --- |
| 公司数据 | 公司财务信息 | 投、融资信息 | C4 | 资本投资计划及变动、重大借款、融资活动 |
|  |  | 债务债权信息 | C4 | 发行新的股票或债务、债务拖欠 |
|  |  | 财务税务信息 | C4 | 资产价值变动信息；各类财务报告、财务报表、税务表、财务预算报表；盈余或盈余预测；总收入、费用、补贴信息 |
|  | 公司经营信息 | 公司重要谈判、决策、策划 | C4 | 公司经营计划、并购或变卖重要子公司或资产的谈判、新签订的重大合同或重大合同意向的破裂、重大的市场计划或该计划的变动 |
|  |  | 产品信息 | C4 | 孵化中的重大产品、服务 |
|  |  | 采购信息 | C4 | 采购价格 |
|  | 公司技术信息 | 产品及业务策略 | C4 | 定价策略、营销方案、核心业务规则、安全管理策略 |
|  |  | 核心知识产权信息 | C4 | 开发设计文档、核心代码、算法 |
|  | 其他信息 | 管理层变动、调查、诉讼 | C4 | 未经正式公告的任何有关高管层或董事会成员的重大诉讼、政府调查或质询、重大人员变动，任何能够极大影响公司盈余或发展前景的重大变动。 |
|  |  | 人车安全信息 | C4 | 事故量、伤亡事故量 |
|  | 公开信息 | 公司正式渠道发布信息 | C1 | 官方微博、微信发布信息；已经披露的年报；其他公司有权部门发布的信息 |



## [《海关区》接入手册](http://wiki.intra.xiaojukeji.com/pages/viewpage.action?pageId=727059076)
**整体概述**：**所有专线跨境数据必须过海关区，严禁偷渡行为，基于海关区，做到接口级别的流量和内容可控、可管、可审计。**
**名词解释**
a、**海关区**：类似于国内公民要出境，只能通过海关区出入境，严禁“偷渡”；基于吞吐和性能分级考虑，海关区也会有基于内容和场景的不同海关区，比如：运维监控海关区，效能工具海关区，紧急调试海关区等。
b、**护照**：护照是跨境发起方的唯一标识符，在**出入境管理中心**申请和下发。按照期限和类型，分为三种护照
**单次护照**：单次进行出入境数据交互，规定时间内，交互成功后时效。（针对特殊数据传输，比如：紧急调试，单次传输大批量数据等场景）
**期限护照**：规定时间内，规定内容和规定流量上限，不限制出入境次数
**特区护照**：针对极少数特殊场景，规定时间、规定内容、规定流量上限、规定IP，不限制接口和出入境次数。
c、**出入境管理中心**：申请护照，出入境管理数据管理、审计工具平台。
d、**出入境基本单元**：原则上出入境的最基本原子单元是 【护照 + 接口】，也就是申请护照后，对于出入境的接口都需要进行登记。
e、**偷渡行为**：不经过出入境管理中心，通过私拉代理走专线的行为，一经发现按照**“出入境管理制度”**通告处理。
f、 **假冒行为**：使用的护照非本业务，或者接口出入境的内容非登记内容，都会视为假冒行为，一经发现按照**“出入境管理制度”**通告处理。

**接入指南**
step1：**【确认数据】**按照出入境军规，判定出入境输入符合海内外监管要求，同时，确认数据出入境的必要性。（非必须不出入境）
step2：**【申请护照】**按照出入境申请表，申请出入境护照和注册接口，参考出入境申请表（出入境管理中心申请）。
step3：**【跨境传输】**传输过程中使用护照按照对应的方式进行跨境，参考[海关区接入流程](http://wiki.intra.xiaojukeji.com/pages/viewpage.action?pageId=705154489#id-1%E3%80%81%E4%B8%93%E7%BA%BF%E6%8E%A5%E5%85%A5%E6%B5%B7%E5%85%B3%E5%8C%BA%E6%8C%87%E5%8D%97-2.2%E6%B5%B7%E5%85%B3%E5%8C%BA%E6%8E%A5%E5%85%A5%E6%96%B9%E5%BC%8F)

**备注：试点阶段，能力具备，平台搭建中，大家接入直接找刘旺（wangliuliu@）or 崔涣（cuihuan@），手动申请信息如下**

---

**

附件一、申请护照表格

| **服务名称** | **负责人** | **护照类型** | **服务一级分类** | **服务二级分类** | **跨境方式** | **跨境使用原因** | **是否牵涉**
**个人数据/**
**重要数据** | **传输协议** | **日最大传输**
**数据量** | **日最大传输次数** | **请求内容示例** | **返回内容示例** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 弹性云任务管理平台 | 张健 | 单次护照
期限护照
特区护照 | 参考服务分类
eg: 监控数据
效能工具
测试工具等 | 继承一级

 | 国内 → 美东 | 弹性云目前国内外一套管理平台，不包含敏感信息，后续迁移国内 | 否 | https | 10MB | 1000次 | {
Hostname: "xxx",
ReportTasks: {
ID: xx,
TS: "xx",
Status: "xx",
Stdout: "xx",
Stderr: "xx",
}
} | {
Message: "xx";
Script: "xx";
Args: "xx";
Account: "xx";
} |



附件二、注册接口表格

| **接口名称** | **负责人** | **接口意义** | **目的IP** | **服务二级分类** | **跨境方式** | **是否牵涉**
**个人数据/**
**重要数据** | **传输协议** | **日最大传输**
**数据量** | **日最大传输次数** | **请求内容示例** | **返回内容示例** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| monitorData | cuihuan | 

 | 当前支持
VIP
DISF
IPs (默认自动寻址，不会摘除)

 | 继承一级

 | 国内 → 美东 | 否 | https | 10MB | 1000次 | {
Hostname: "xxx",
ReportTasks: {
ID: xx,
TS: "xx",
Status: "xx",
Stdout: "xx",
Stderr: "xx",
}
} | {
Message: "xx";
Script: "xx";
Args: "xx";
Account: "xx";
} |




# 数据分享(share)

# 三方管理(vendor)[《欧洲第三方机构准入管理规范》](http://wiki.intra.xiaojukeji.com/pages/viewpage.action?pageId=693769618)



## 一、目的/Purpose
为保护滴滴用户和员工的个人数据，约束第三方机构的准入，根据GDPR第28条、国际化信息安全与个人数据保护管理要求，特制定此规范。
In order to protect the personal data of users and employees of DiDi,  this specification is formulated according to Article 28 of GDPR and international infosec & personal data protection regulation requirements.
## 二、范围/Scope

1. 本规范所称个人数据是指在欧盟境内直接采集的个人数据，或在欧盟境内处理的境外采集个人数据，包括用户个人数据、员工个人数据，个人数据范围参见[PII分级定义](http://wiki.intra.xiaojukeji.com/pages/viewpage.action?pageId=509489746)。
The personal data defined by the specification below refer to personal data directly collected within EU, or personal data processed within EU which collected outside EU, including user personal data, employee personal data. Please Refer to[PII classification](http://wiki.intra.xiaojukeji.com/pages/viewpage.action?pageId=509489746). 
2. 本规范所称第三方机构是指处理滴滴欧盟用户和员工个人数据的第三方供应商或合作伙伴，包括但不限于SaaS服务商、咨询机构、线下数据处理供应商、合作商家等。
The 3rd-party defined by the specification below refer to the 3rd-party suppliers or partners that process  the personal data of DiDi EU users and employees, including SaaS service providers, consulting institution, offline data processing providers, and business partners, etc.
## 三、规范要求/ Regulation Requirement
| 一级类目
Primary Category | 二级类目
Secondary Category | 序号
No. | 规范描述
Specification Description | 要求等级
Requirement Level | 是/否
Yes/No | 详细描述
Details |
| --- | --- | --- | --- | --- | --- | --- |
| **1. 信安资质/InfoSec Qualifications** |  |  |  |  |  |  |
| 信安资质
InfoSec Qualifications | 国际认证
International Certificate | 1 | 获得信息安全相关认证，如ISO/IEC27001，PCI-DSS等
Obtained Information Security related certification, e.g. ISO27001, PCI-DSS, etc. | 增强要求
Recommended Requirement | 

 | 

 |
|  |  | 2 | 获得隐私合规相关认证，如ISO/IEC27701，BS10012等
Obtained privacy compliance certification，e.g. ISO/IEC27701, BS10012, etc. | 增强要求
Recommended Requirement | 

 | 

 |
|  | 第三方审计
3rd Party Audit | 3 | 具有第三方机构的安全审计报告，如SOC1/2，ISAE，ITGC/AC等
Obtained a 3rd party infosec audit report, e.g. SOC Ⅰ/Ⅱ, ISAE, ITGC/AC, etc. | 增强要求
Recommended Requirement | 

 | 

 |
| **2. 数据泄露/Data Breach** |  |  |  |  |  |  |
| 数据泄露
Data Breach | 数据泄露报告
Data Breach Report | 4 | 近三年未发生或数据泄露和信息安全事件
Whether a data breach or other accident has occurred in the past three years | 增强要求
Recommended Requirement | 

 | 

 |
|  | 数据泄露响应机制
Data Breach Response Procedure | 5 | 当发生个人数据泄露事件时，应具备沟通及处置机制，及时通知滴滴和用户，并履行个人数据保护法的要求
Whether when a data breach or other accident has occurred, or there is a high probability that an accident has occurred, there is reporting and communication mechanism to notify DiDi users? Fill in the document name and the document update date. | 增强要求
Recommended Requirement | 

 | 

 |
| **3. 法律文档/Legal Documents** |  |  |  |  |  |  |
| 法律文档
Legal Documents | 数据处理协议
Data Processing Agreement | 6 | 需签署书面数据处理协议，并规定数据处理的责任与权利、处理期限、处理性质与目的、个人数据的类型、数据主体的类型等。
It's required to sign a data processing agreement , and specify the obligations of controller and processor, the data retention period, the nature and purpose of the processing, the categories of personal data, the categories of data subject, etc. | 合规要求
Compliance Requirement | 

 | 

 |
|  | 保密协议
Non-Disclosure Agreement | 7 | 需签署保密协议，包括第三方机构和处理滴滴个人数据的第三方机构员工
It's required to sign a non-disclosure agreement, including the 3rd party institution and the employees of the 3rd party institution that handle our personal data | 合规要求
Compliance Requirement | 

 | 

 |
|  | 隐私政策
Privacy Policy | 8 | 第三方个人数据处理方式和目的需包含在滴滴隐私政策中，并获取相关用户的同意。如果未包含，需联系法务更新隐私政策
This personal data processing activity and purpose should be covered by our privacy policy, and obtain users' consent before we send their data to the 3rd party. If not cover, please contact Legal to update the privacy policy | 合规要求
Compliance Requirement | 

 | 

 |
| **4. 数据跨境/Data Cross-border** |  |  |  |  |  |  |
| 数据跨境
Data Cross-border | 本地存储
Data Localization | 9 | 个人数据需在欧盟境内处理和存储，无论是自有机房还是公有云服务
Personal data should be processed and stored within the EU territory，both the IDC and SaaS | 合规要求
Compliance Requirement | 

 | 

 |
|  | 数据跨境
Data Cross-border | 10 | 如业务需要将个人数据传输至欧盟境外第三国，需评估第三国的法律环境，并签署SCC
If personal data need to be transferred to the 3rd country outside the EU based on business need, it's required to assess if the law of the 3rd country impinges on the effectiveness of the appropriate safeguards, and sign SCC. | 合规要求
Compliance Requirement | 

 | 

 |
| **5. 数据审批/Data Approval** |  |  |  |  |  |  |
| 数据审批
Data Approval | 数据审批
Data Approval | 11 | 外发个人数据，需提交[数据外发流程](https://bpm.didichuxing.com/process/form/bykey/International_security_data_process?tenantId=AQ&jumpType=nameSearch)
申请，明确外发数据字段、接收方、处理目的、保障方式等
Strictly follow the data sharing procedure, specify the data categories, recipient, purpose of processing, security measures, etc. | 合规要求
Compliance Requirement | 

 | 

 |
| **6. 隐私评估/Privacy Assessment** |  |  |  |  |  |  |
| 隐私评估
Privacy Assessment

 | 数据最小化
Data Minimization | 12 | 外发个人数据处理基于目的必要性，满足最小化原则
The personal data processed by the 3rd party is based on the necessity of purpose and meets the principle of minimization | 合规要求
Compliance Requirement | 

 | 

 |
|  | 数据使用
Data Usage | 13 | 个人数据处理仅限于第三方机构正式员工，并遵循严格的访问控制政策
Only official employees of the 3rd party can process our personal data, and access control policy need to be in place | 合规要求
Compliance Requirement | 

 | 

 |
|  |  | 14 | 个人数据处理不得使用员工个人电脑或移动存储
It's prohibited to process or store DiDi's personal data on personal computers and storage media | 增强要求
Recommended Requirement | 

 | 

 |
|  |  | 15 | 未经滴滴书面授权不得将数据处理活动移交至第四方、第五方处理
It's prohibited to transfer DiDi's personal data to the 4th and 5th parties without the written authorization of DiDi | 合规要求
Compliance Requirement | 

 | 

 |
|  | 数据传输
Data Transfer | 16 | 个人数据必须加密传输
The data transfer must be encrypted | 合规要求
Compliance Requirement | 

 | 

 |
|  | 数据销毁
Data Disposal | 17 | 合同服务期满且不再合作后应按滴滴要求格式化所有主机硬盘、并销毁业务相关的纸质资料。
All hard disks of host shall be formatted and paper materials related to business shall be destroyed after the business is no longer used by Didi.  | 合规要求
Compliance Requirement | 

 | 

 |
|  | 权利响应
Privacy Rights Response | 18 | 需协助滴滴履行对数据主体的权利响应，包括访问权、修改权、删除权、限制处理权、拒绝权、可携带权、拒绝自动化决策权
When possible, it's required to support DiDi when complying with its obligation to respond to the data subject rights, including access, rectification, erasure, restriction of processing, objection, portability, and the right to refuse automated individual | 合规要求
Compliance Requirement | 

 | 

 |
|  |  | 19 | 对于数据可携带权和删除权，需建立数据处理能力和响应机制。
It's required to establish a procedure and data processing capability to respond the right of data portability and erasure | 合规要求
Compliance Requirement | 

 | 

 |
|  | 数据处理活动记录
Records of Processing Activities | 20 | 需建立滴滴个人数据的处理活动记录
It's required to maintain records of processing activities for DiDi's personal data | 合规要求
Compliance Requirement | 

 | 

 |
| **7. 信息安全评估/Infosec Assessment** |  |  |  |  |  |  |
| **信息安全评估**
Infosec Assessment | 组织管理
Organizational Management | 21 | 需建立信息安全相关制度规范
It's required to establish information security policies, standards, procedures, guidelines, etc. | 合规要求
Compliance Requirement | 

 | 

 |
|  |  | 22 | 员工提供服务前进行岗前培训，培训内容应包含信息安全、隐私数据安全、保密协议相关内容。
Pre-job training is required before employees processing DiDi‘s personal data. The training content shall include but not limited to information security requirements, privacy security requirements, confidential agreements. | 增强要求
Recommended Requirement | 

 | 

 |
|  | 应用安全
Application Security | 23 | 数据交互接口上线前应接入[SDL平台](http://sdl.xiaojukeji.com/sdl/ratel/selfService)检测
Perform [SDL](http://sdl.xiaojukeji.com/sdl/ratel/selfService) testing before the data interaction interface goes online | 合规要求
Compliance Requirement | 

 | 

 |
|  |  | 24 | 对于互联网可访问的数据交互接口需进行渗透测试
Perform Penetration test for the data interaction interface with internet access | 增强要求
Recommended Requirement | 

 | 

 |
|  | 访问控制
Access Control | 25 | SaaS服务需接入滴滴SSO
Access to SaaS should be authenticated through DiDi's SSO | 合规要求
Compliance Requirement | 

 | 

 |
|  |  | 26 | 需使用多因素进行身份验证
Multi-factor authentication is required | 增强要求
Recommended Requirement | 

 | 

 |
|  | 审计管理
Audit Management | 27 | 需记录个人数据处理的审计日志，包括但不限于账号、权限、时间、操作、成功或失败等，并定期同步日志给滴滴
The audit log of personal data processing shall be recorded, including but not limited to account information, permission, timestamp, operation, success or failure, etc., and the log shall be synchronized to Didi regularly | 合规要求
Recommended Requirement | 

 | 

 |
|  |  | 28 | 一旦滴滴提出审计需求，需配合滴滴接受外部机构进行信息安全或隐私保护审计工作
It's required to provide cooperation to respond information security or privacy protection auditing carried out by external institutions on behalf of DiDi once DiDi puts forward audit requests. | 增强要求
Recommended Requirement | 

 | 

 |


