

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


