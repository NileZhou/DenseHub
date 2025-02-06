

[TOC]

# Key points



重点看evaluation方法，还有RL具体算法细节



- **Reusing trajectories**: 重复利用之前生成的轨迹，而不是from scratch 地重新生成。以此来imporve training efficiency
- **Context Length** 是RL + LLM领域继续scaling的一个key dimension，**无需**MCTS、value functions、process reward model这些复杂的技术
- **robust policy in RL **: long CoT训练加上 RL很可能不稳定，本文开发了一个稳定的算法 （**重点**）
- **Multimodalities**:  **jointly reasoning** over 2 modalities(text/vision)
- **Long2short**: 用多种方法(lenth penalty / model merging / RL)来将变长的CoT模型进行训练，使其生成更短的CoT  (猜想：**直觉思维**可能在这一步骤涌现)



# Pipeline

要达到Kimi k1.5，一共经历以下阶段:

1. pretraining
2. SFT
3. long-CoT SFT: 猜测是让模型在生成long CoT时变得稳定，不会因为生成 long CoT导致性能下降
4. RL (**本论文只关注这个阶段**，无其他阶段细节)，分为三个阶段:
   1. 人类精心构造的prompt集合作为cold start，启发模型的思维
   2. 高质量Long CoT warmup （文本/图文 QA对）进行Long-CoT SFT
   3. 正式强化学习




## RL Step1 -- Prompt Set Curation



作者的早期大量实验表明：在保证强化学习的有效性过程中，prompt的**quality** 和 **diversity** 非常关键。Well-constructed的prompt集合不止可以引导整个reasoning过程，使其robust，而且可以减轻rewards hacking的风险，缓解模型对一些superficial patterns的过拟合。



作者认为高质量RL prompt集合应该有以下特点:

- Diverse Coverage

  范围要广，STEM, coding, general reasoning都得有。且本文的prompt QA里包含纯文本与图文对。使用一个**tagging system**来对prompts进行打标，分为各个domain和discipline，保证训练数据在各个领域是均匀分布的。

- Balanced Difficulty

  由易到难地gradual learning，避免对一些复杂的偏难题进行过拟合，或者只能解决复杂度在某一个level的问题。

  这里作者也做了一个**tagging system**，用一个SFT后的模型回答10次，算pass@10，pass rate越低的难度越高，给每条数据的难度进行打标

- Accurate Evaluability

  Evaluation一定要足够**objective且reliable**，避免模型是靠猜或流于表面的回答来骗得高分。

  作者先把多选，true/false，基于证明的问题都排除了，因为觉得**模型太容易猜出来**。而且让一个模型不用CoT猜8次，只要有一次猜出来了，作者就将这条case去掉。

  然后用一个critic模型来评估(有正确答案作为参考) policy model回答的对不对



## RL step2 -- Long-CoT SFT



猜想：step1的prompt真的是prompt而不是数据，这些prompt是用来造数据的

走到这一步才真的有一个高质量的warmup数据集



有了refined后的RL prompt集合，作者使用prompt engineering构建一个高质量的long-CoT warmup数据集（拥有verified的推理路径），包含文本和图文问答。

这个数据集里有以下多种思维模式，非常类似人类的思考推理过程：

- planning: 系统性、分治地思考问题
- evaluation: 在中间步骤包含关键的评估步骤
- reflection: 使得模型能不断重新思考，且refine自己的思维路径
- exploration: 不断地想alternative的路径

这个阶段主要就是想**把这些思维模式内化在模型内部**，实验证明进行SFT后在多个推理任务上提高了模型的性能



## RL step3 -- reinforcement learning



### PS: planning algorithm

为了进一步提高模型推理能力，显示地用规则/策略引导模型的思维过程。其中的典型方法有:

- MCTS

MCTS: 设$\mathcal{T}$为一棵planning tree, 每个node是一个partial solution
$$
s = (x, z_{1:|s|})
$$
$s$ 包含了问题$x$和一个通向当前节点的thoughts序列 
$$
z_{1:|s|} = (z_1, \dots, z_{|s|})
$$
这里的$|s|$代表了序列里的thoughts个数。

planning algorithm还会使用一个critic model $v$ 来提供一个反馈:
$$
v(x, z_{1:|s|})
$$
帮助评估当前步骤中是否有错误且在当前的partial solution中识别是否有错。

注意这里的$v$既可以是一个score也可以是一段话，让planning 算法判断选择哪个节点继续努力。



过去t轮的past history 可以计作: 
$$
(s_1, v(s_1), \dots, s_{t-1}, v(s_{t-1}))
$$
即每一个step和其对应的reward / feedback，作者在文中使用$z$来代替$s$和$v$，即代表中间过程。

即，将所有本来应该是MCTS维护的信息都flatten成一个序列，也就是不需要显式构造一棵树，上下文历史本来就可以代表某种planning algorithm。





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

