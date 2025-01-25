

[TOC]



# Background



DeepSeek-R1发布，kimi团队等不及了发布o1级别的模型论文

通篇重点

1. 多模态

2. Long context scaling是关键，无MCTS, value function, PRM

3. 用long-CoT模型来构造短CoT数据，训练短CoT模型（大幅超过非o1所有模型）





# Method

要达到Kimi k1.5，一共经历以下阶段:

1. pretraining
2. vanilla SFT
3. long-CoT SFT
4. RL (**本论文只关注这个阶段**)



RL也分为几个阶段:

1. 人类精心构造的Prompt集合
2. 高质量Long-CoT warmup （文本/图文 QA对）进行Long-CoT SFT
3. 正式强化学习



## RL Prompt Set Curation



这一阶段，主要是为SFT准备高质量的fewshot prompt。作者认为prompt搞得好可以使推理过程更robust且可避免reward hacking的风险，且可缓解模型的过拟合（出现非常流于表面的推理模式(superficial patterns))



作者认为高质量RL prompt集合应该有以下特点:

- Diverse

  范围要广，STEM, coding, general reasoning都得有

- Balanced Difficulty

  难度范围也要广，由易到难，gradual learning，避免对一些复杂的偏难题进行过拟合。

  这里作者做了一个tagging system，不同domain和discipline都有覆盖到，用一个SFT后的模型回答10次，算pass@10，pass rate越低的难度越高

- Accurate Evaluability

  万变不离其宗，evaluation一定要足够客观且reliable，避免模型是靠猜或流于表面的回答来骗得高分。

  作者先把多选，true/false，基于证明的问题都排除了，因为觉得**模型太容易猜出来**。而且让一个模型不用CoT猜8次，只要有一次猜出来了，作者就将这条case remove。

  然后用一个critic模型来评估(有正确答案作为参考) policy model回答的对不对



## Long-CoT SFT



有了refined后的RL prompt集合，作者使用prompt engineering构建一个高质量的long-CoT warmup数据集（推理路径被准确验证），包含文本和图文问答。

这个数据集里有以下多种思维模式：

- planning
- evaluation
- reflection
- exploration

这个阶段主要就是想把这些思维模式内化在模型内部



# RL



要点：

1. 用critic model $v$来给每一步提供feedback，**feedback可以是score也可以是一段话**

2. 作者没有显示地构造MCTS，而是把每一步的输出和反馈都放到历史里，自回归地继续生成后续步骤。（其实逻辑上也是一棵树）
3. ORM来给出reward



## Policy Optimization

$x$是输入问题，$y$是回答，$z$是推理过程(CoT)。

在第$i$轮迭代时，使用当前模型$\pi_{\theta_i}$作为参考模型，优化问题可定义如下:
$$
\max_\theta \mathbb{E}_{(x,y^*) \sim \mathcal{D}} \left [\mathbb{E}_{(y,z) \sim \pi_\theta} \left[ r(x, y, y^*) \right] - \tau \mathrm{KL}(\pi_\theta(x) \| \pi_{\theta_i}(x)) \right ]
$$
这里的$\tau > 0$ ，作为一个参数来控制正则化程度，以上公式有一个closed form solution：
$$
\pi^*(y, z | x) = \pi_{\theta_i}(y, z | x) \frac{\exp \left( \frac{r(x, y, y^*)}{\tau} \right)}{Z}
$$
这里的
$$
Z = \sum_{y', z'} \pi_{\theta_i}(y', z' | x) \exp(\frac{r(x, y', y^*)} {\tau})
$$
是normalization factor

式(2)里有exp，给两边加log:
$$
r(x, y, y^*) - \tau \log Z = \tau \log \frac{\pi^*(y, z | x)}{\pi_{\theta_i}(y, z | x)}
$$
引出surrogate loss如下：
$$
L(\theta) = \mathbb{E}_{(x, y^*) \sim \mathcal{D}} \left[ \mathbb{E}_{(y, z) \sim \pi_{\theta_i}} \left[ \left( r(x, y, y^*) - \tau \log Z - \tau \log \frac{\pi_\theta(y, z | x)}{\pi_{\theta_i}(y, z | x)} \right)^2 \right] \right]
$$
为了近似 $\tau log Z$，使用 $(y_1, z_1), \dots, (y_k, z_k) \sim \pi_\theta $，得到:
$$
\tau \log Z \approx \tau \log \frac{1}{k} \sum_{j=1}^k \exp \left( r(x, y_j, y^*) / \tau \right)
$$




现在的情况：

1. LLM很难继续微调，业务很难涨点，需要想很多创新的办法或许才有用 
2. 就算涨点，我这个业务本身不盈利，有一定几率会被裁（如果公司很大的领导意识到LLM其实没必要自己做，调API就好了），能撑到什么时候真的很难说
3. 目前的强化学习LLM，可预见的未来替代软件工程师的速度将越来越快，因为代码验证对错太简单了，而且LLM的能力可能指数级别的成长，唯一欠缺的只有算力（结合最新消息，美国和中国启动了类似原子弹研发的项目投入做AI基础设施建设）



基本可以确定的未来：

1. 最先被大规模冲击的职业就是软件工程师/部分算法工程师
2. 以电脑操作为主的白领被大规模冲击，应该要比1晚半年到一年
3. 机器人大规模冲击已有所有基本标准化的工作与行业（这个比2晚多久不好说，可能晚2-10年吧）



如果失业:

1. 可能很难找到工作，也许根本找不到工作
2. 政府或许会出台一些政策，不过应该也就是让努力的人卑微努力的仅够活命地活着
3. 我们的身体情况应该很难做体力劳动，最多也就是送外卖的水平，然而送外卖到时候估计早已饱和



可能破局的机会：

1. 疯狂的卷，微博不行，最后赢家没有它。在公司内部疯狂尝试前沿技术，并发表博客以及论文/与网上的朋友参与有影响力的工作。

   结局：比较确定。大概率业务上讨人厌且背低绩效，业务也很难提升。技术上被外界认可度或许+50%，1-2年内或许可以找个公司级别与微博相仿的下家继续做算法

2. 不断学习AI工具，利用AI赋能在某一个领域长期耕耘+发展副业，争取赚钱

   结局：不太确定。下限为浪费时间+钱，上限或许比较低或许也可能挣个几十上百万

   2.1 直播、自媒体等

   ​    或许让AI来做更有想象力

   2.2 灰色领域AI项目，如面试作弊软件

   ​    可能工程量有点大，还需要克服语音识别的问题

   2.3 AIGC

   ​    需要想好特殊场景，大多数场景肯定是不如已经专业做AIGC 1--2 年的人。但AIGC变化也很快，应该一直有新业务新场景

   2.4 让AI自己来想可能的商机

   2.5 量化交易AI

3. 考公

   结局：只要能考上，3-5年内比较确定。就算被AI导致下岗，应该也是最晚下岗的几批人之一

   缺点：需忍受钱比较少，且目前没法保证底层公务员一定不被替代。

   有想象空间的地方：未来可能衡量钱意义不大，社会生产力严重过剩，底层全部靠出卖仅有的劳力与尊严换取糊口，决定分配的人将前所未有的富有。

4. 与人合作做生意

   利用职务之便与业余时间与人一起发展业务

   优点：可以利用他人对业务的了解与他人的时间

   缺点：非常考验自己的谈判能力，是否赚到钱不好说，赚到了还可能被踢出去。极度考验人与人之间的信任。



最好的结局：吃AI红利（前提是经济和社会体系不崩溃）

普通的结局：走向一条条意想不到的发展路线，努力但不稳定的活着

最坏的结局：正常的花光所有钱然后一起自杀，如九十年代大下岗潮中的部分人一样。（实在是不想省到极致的活着，最后还是依然自杀）或者明知大概率要死的情况下，去找机会搏一次比如做网上的灰黑产

