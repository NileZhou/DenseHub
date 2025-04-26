## 纯文本R1复现工作总结



# 2025.0102, PRIME-RL

| Project or Paper      | [Process Reinforcement through Implicit Rewards](https://arxiv.org/abs/2502.01456) |
| --------------------- | ------------------------------------------------------------ |
| GitHub                | [PRIME-RL/PRIME](https://github.com/PRIME-RL/PRIME)          |
| Backbone Model        | Qwen2.5-Math-7B-Base                                         |
| RL Algorithm          | PPO/REINFORCE++/RLOO/GRPO + Online PRM                       |
| Training Dataset      | [PRIME-RL/Eurus-2-RL-Data](https://huggingface.co/datasets/PRIME-RL/Eurus-2-RL-Data), 150K |
| Rollout Configuration | 256 prompts * 4 responses Online Prompt Filtering (Accuracy in [0.2,0.8]) |
| Reward Function       | Rule-based Rewards + Implicit Process Rewards                |
| Policy Optimization   | PPO loss, without KL loss                                    |
| Benchmark             | GPT-4o level on AIME 2024, AMC, MATH-500, Minerva Math, OlympiadBench, LeetCode, and LiveCodeBench |
| Core Insights         | Implicit PRM efficiently addresses reward sparsity, distribution shift, and scalability by directly learning token-level rewards within a language model framework, eliminating the need for separate value models or prior training. |
| Additional Notes      |                                                              |



# 2025.0122, DeepSeek-R1

| Project or Paper      | [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/pdf/2501.12948) |
| --------------------- | ------------------------------------------------------------ |
| GitHub                | [deepseek-ai/DeepSeek-R1](https://github.com/deepseek-ai/DeepSeek-R1) |
| Backbone Model        | DeepSeek-V3-Base                                             |
| RL Algorithm          | GRPO                                                         |
| Training Dataset      | Unclear                                                      |
| Rollout Configuration | 4~64 samples for each prompt, temperature = 0.6              |
| Reward Function       | Rule-based Rewards                                           |
| Policy Optimization   | vanilla GRPO Loss                                            |
| Benchmark             | OpenAI-o1 level on AIME 2024, Codeforces, GPQA Diamond, MATH-500, MMLU, SWE-bench Verified. |
| Core Insights         | RL can boost LLMs' reasoning. DeepSeek - R1 series models prove effective, and distilling reasoning to small models works, while highlighting challenges in other methods. |
| Additional Notes      |                                                              |



# 2025.0122, Kimi k1.5

| Project or Paper      | [Kimi k1.5: Scaling Reinforcement Learning with LLMs](https://arxiv.org/pdf/2501.12599) |
| --------------------- | ------------------------------------------------------------ |
| GitHub                | [MoonshotAI/Kimi-k1.5](https://github.com/MoonshotAI/Kimi-k1.5) |
| Backbone Model        | Kimi k-series model (closed source)                          |
| RL Algorithm          | Online Policy Mirror Decent/Length Penalty Reward/Curriculum Sampling/Prioritized Sampling/Chain-of-Thought RM/Long2short RL |
| Training Dataset      | Code: 1000 contest problem; </br>Math: 800k in-context learning/800k chain-of-thought data; </br> Vision: unknown number of real-world/synthetic visual reasoning/text-rendered data |
| Rollout Configuration | None                                                         |
| Reward Function       | Outcome Reward+Length Penalty Reward                         |
| Policy Optimization   | Online Policy Mirror Decent                                  |
| Benchmark             | Matching OpenAI’s o1 on AIME/MATH500/Codeforces/MathVista    |
| Core Insights         | Effective long2short methods that use long-CoT techniques to improve short-CoT models, yielding state-of-the-art short-CoT reasoning results, outperforming existing short-CoT models. |
| Additional Notes      |                                                              |



# 2025.0124, TinyZero

| Project or Paper      | not applicable                                               |
| --------------------- | ------------------------------------------------------------ |
| GitHub                | [Tiny-Zero](https://github.com/Jiayi-Pan/TinyZero) |
| Backbone Model        | QWen-2.5-3B                                                  |
| RL Algorithm          | GRPO                                                         |
| Training Dataset      | countdown                                                    |
| Rollout Configuration | 1024                                                         |
| Reward Function       | 0/1 reward                                                   |
| Policy Optimization   | vanilla GRPO: (KL Loss; Length Penalty; Token-level loss)    |
| Benchmark             | test set of countdown                                        |
| Core Insights         | Aha moment can be reproducible on puzzle-style data.         |
| Additional Notes      |                                                              |



# 2025.0125, SimpleRL

| Project or Paper      | [7B Model and 8K Examples: Emerging Reasoning with Reinforcement Learning is Both Effective and Efficient](https://hkust-nlp.notion.site/simplerl-reason) |
| --------------------- | ------------------------------------------------------------ |
| GitHub                | [hkust-nlp/simpleRL-reason](https://github.com/hkust-nlp/simpleRL-reason) |
| Backbone Model        | Qwen2.5-Math-7B                                              |
| RL Algorithm          | PPO based on OpenRLHF                                        |
| Training Dataset      | [MATH](https://huggingface.co/datasets/EleutherAI/hendrycks_math), 8k Level3-Level5 |
| Rollout Configuration | 128 prompts * 8 responses; Temperature = 0.6                 |
| Reward Function       | Rule-based Rewards                                           |
| Policy Optimization   | PPO loss with 0.01 KL coefficient                            |
| Benchmark             | GPT-4o level on AIME2024, AMC2023, College Math, Gaokao2023en, GSM8k, MATH500, Minerva Math, and OlympiadBench. |
| Core Insights         | Long Chain-of-Thought (CoT) and self-reflection can emerge on a 7B model with only few high-quality examples with rule-based rewards only. |
| Additional Notes      |                                                              |



# 2025.0206, Demysitify-long-CoT

| Project or Paper      | [Demystifying Long Chain-of-Thought Reasoning in LLMs](https://arxiv.org/pdf/2502.03373) |
| --------------------- | ------------------------------------------------------------ |
| GitHub                | [eddycmu/demystify-long-cot](https://github.com/eddycmu/demystify-long-cot) |
| Backbone Model        | Qwen2.5-Math-7B Llama-3.1-8B                                 |
| RL Algorithm          | PPO (OpenRLHF)                                               |
| Training Dataset      | 7500 training samples of MATH                                |
| Rollout Configuration | 512 prompts * 8 responses; temperature=0.7, top-p=0.95 Context Length Prompt=2048, Gen=14384 tokens |
| Reward Function       | Rule-based Reward + Cosine Length Reward + Repetition Penalty Reward |
| Policy Optimization   | KL coefficy=0.01, gamma=1, lambda=1                          |
| Benchmark             | MATH, AIME, TheoremQA, MMLU-Pro-1k                           |
| Core Insights         | Reward shaping can be used to stabilize and control CoT length while improving accuracy. Cosine reward can be tuned to incentivize various length scaling behaviors, length rewards will be hacked with enough compute. But this can be mitigated using a repetition penalty. |
| Additional Notes      |                                                              |





# 2025.0210, DeepScaler

| Project or Paper      | [DeepScaleR: Surpassing O1-Preview with a 1.5B Model by Scaling RL](https://pretty-radio-b75.notion.site/DeepScaleR-Surpassing-O1-Preview-with-a-1-5B-Model-by-Scaling-RL-19681902c1468005bed8ca303013a4e2) |
| --------------------- | ------------------------------------------------------------ |
| GitHub                | [deepscaler](https://github.com/agentica-project/deepscaler) |
| Backbone Model        | deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B                    |
| RL Algorithm          | GRPO                                                         |
| Training Dataset      | [Omni-MATH](https://omni-math.github.io/) and [Still](https://github.com/RUCAIBox/Slow_Thinking_with_LLMs) |
| Rollout Configuration | 128 * 16 (bs*n);temperature=0.6; Context Length:8K->16K->24K |
| Reward Function       | 0/1 reward                                                   |
| Policy Optimization   | vanilla GRPO: (KL Loss; Length Penalty; Token-level loss)    |
| Benchmark             | AIME 2024/ MATH 500 /AMC 2023 / Minerva Math/ OlympiadBench  |
| Core Insights         | 1. RL scaling can manifest in small models as well. 2. Iterative lengthening enables more effective length scaling. |
| Additional Notes      | Iteratively increasing the max context for RL training.      |



# 2025.0210, Logic-RL

| Project or Paper      | [Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning](https://arxiv.org/abs/2502.14768) |
| --------------------- | ------------------------------------------------------------ |
| GitHub                | [Unakar/Logic-RL](https://github.com/Unakar/Logic-RL)        |
| Backbone Model        | Qwen2.5-Math-7B / Qwen2.5-7B-Instruct                        |
| RL Algorithm          | REINFORCE++                                                  |
| Training Dataset      | [Knights and Knaves (K&K) puzzles](https://huggingface.co/datasets/K-and-K/knights-and-knaves), 6.2k |
| Rollout Configuration | 8 prompts * 8 responses; Temperature = 0.7                   |
| Reward Function       | Rule-based Rewards                                           |
| Policy Optimization   | REINFORCE++ loss with 0.001 unbiased KL coefficient.         |
| Benchmark             | o3-mini-high level on K&K logic puzzle                       |
| Core Insights         | With simple REINFORCE++ with KL loss, 7B model develops advanced reasoning skills that are absent from the logic corpus and generates to other tasks like math. |
| Additional Notes      |  |


# 2025.0210, OREAL

| Project or Paper      | [Exploring the Limit of Outcome Reward for Learning Mathematical Reasoning](https://arxiv.org/abs/2502.06781) |
| --------------------- | ------------------------------------------------------------ |
| GitHub                | [InternLM/OREAL](https://github.com/InternLM/OREA)           |
| Backbone Model        | Qwen2.5-7B / Qwen2.5-32B                                     |
| RL Algorithm          |   |
| Training Dataset      | [OREAL-RL-Prompts](https://huggingface.co/datasets/internlm/OREAL-RL-Prompts), 4k |
| Rollout Configuration | 64 prompts * 16 responses; Temprature = 1.0; Online Accuracy Filtering; Retain only one correct and wrong solutions |
| Reward Function       | Outcome Reward Signal by rule-based verifier and Qwen2.5-72B-Instruct + Token level Reward |
| Policy Optimization   | OREAL loss with 0.01 KL coefficient                          |
| Benchmark             | R1-level on MATH500, AIME2024, AIME2025-I, LiveMath, Olympiad |
| Core Insights         | Behavior cloning on positive samples is sufficient for optimal learning and reward reshaping for negative samples is needed for consistent gradient estimation. A token-level reward model can be trained to addresses sparse rewards. |
| Additional Notes      | |



# 2025.0217, LIMR

| Project or Paper      | [LIMR: Less is More for RL Scaling](https://arxiv.org/abs/2502.11886) |
| --------------------- | ------------------------------------------------------------ |
| GitHub                | [GAIR-NLP/LIMR](https://github.com/GAIR-NLP/LIMR)            |
| Backbone Model        | Qwen2.5-Math-7B                                              |
| RL Algorithm          | PPO based on OpenRLHF                                        |
| Training Dataset      | [LIMR](https://huggingface.co/datasets/GAIR/LIMR), 1.4k      |
| Rollout Configuration | 1024 prompts * 8 responses; Temperature = 1.2                |
| Reward Function       | Rule-based Rewards                                           |
| Policy Optimization   | PPO loss with 0.01 KL coefficient                            |
| Benchmark             | GPT-4o level on AIME2024, MATH500, AMC2023                   |
| Core Insights         | Precisely selected data may be the key to unlocking the enhanced reasoning capabilities of LLMs. |
| Additional Notes      | The author uses the trained model's average reward curve as a reference for measuring sample effectiveness. |



# 2025.0217, Open-Reasoner-Zero

| Project or Paper      | [Open-Reasoner-Zero: An Open Source Approach to Scaling Up Reinforcement Learning on the Base Model](https://github.com/Open-Reasoner-Zero/Open-Reasoner-Zero/blob/main/ORZ_paper.pdf) |
| --------------------- | ------------------------------------------------------------ |
| GitHub                | [Open-Reasoner-Zero/Open-Reasoner-Zero](https://github.com/Open-Reasoner-Zero/Open-Reasoner-Zero) |
| Backbone Model        | Qwen2.5-7B, Qwen2.5-32B                                      |
| RL Algorithm          | PPO based on OpenRLHF                                        |
| Training Dataset      | [ORZ-MATH](https://github.com/Open-Reasoner-Zero/Open-Reasoner-Zero/tree/main/data), 57k |
| Rollout Configuration | 128 prompts * 64 responses; Temperature = 1.0                |
| Reward Function       | Rule-based Rewards                                           |
| Policy Optimization   | PPO loss without KL loss                                     |
| Benchmark             | GPT-4o level on GPQA-Diamond, MATH500, AIME2024              |
| Core Insights         | Vanilla PPO with GAE and rule-based rewards without KL loss is sufficient to sclae up response length and benchmark performance. |
| Additional Notes      |                                                              |



# 2025.0225, SWE-RL

| Project or Paper      | [SWE-RL: Advancing LLM Reasoning via Reinforcement Learning on Open Software Evolution](https://arxiv.org/abs/2502.18449) |
| --------------------- | ------------------------------------------------------------ |
| GitHub                | [facebookresearch/swe-rl](https://github.com/facebookresearch/swe-rl) |
| Backbone Model        | Llama-3.3-70B-Instruct                                       |
| RL Algorithm          | GRPO                                                         |
| Training Dataset      | Publicly available repositories                              |
| Rollout Configuration | 32 prompts * 16 rollouts                                     |
| Reward Function       | Similarity Function (`difflib.SequenceMatcher`)              |
| Policy Optimization   | Normalized Rewards for Advantage Calculation                 |
| Benchmark             | GPT-4o level on SWE-bench Verified (41%)                     |
| Core Insights         | SWE-RL enhances LLMs' code reasoning through RL using open-source software evolution data, achieving state-of-the-art results in software engineering tasks and demonstrating generalized reasoning capabilities beyond coding. |
| Additional Notes      |                                                              |



# 2025.0303, VC-PPO

| Project or Paper      | [What’s Behind PPO’s Collapse in Long-CoT? Value Optimization Holds the Secret](https://arxiv.org/pdf/2503.01491) |
| --------------------- | ------------------------------------------------------------ |
| GitHub                | N/A                                                          |
| Backbone Model        | Qwen2.5-32B-Base                                             |
| RL Algorithm          | VC-PPO                                                       |
| Training Dataset      | A compilation of questions from all past AIME competitions (excluding the last two years), supplemented with artificially constructed challenging mathematical problems. |
| Rollout Configuration | N/A                                                          |
| Reward Function       | Rule-based Rewards                                           |
| Policy Optimization   | PPO loss, Value Estimate with Decoupled-GAE                  |
| Benchmark             | AIME 2024, GPQA, CodeForces                                  |
| Core Insights         | VC-PPO addresses PPO’s failure in long CoT tasks by pretraining the value model to correct initialization bias and decoupling GAE between the actor and critic to mitigate reward signal decay. |
| Additional Notes      |                                                              |



# 2025.0306, LCPO-L1


| Project or Paper      | [L1: Controlling How Long A Reasoning Model Thinks With Reinforcement Learning ](https://www.arxiv.org/pdf/2503.04697) |
| --------------------- | ------------------------------------------------------------ |
| GitHub                | [cmu-l3/l1](https://github.com/cmu-l3/l1)                    |
| Backbone Model        | DeepScaleR-1.5B-Preview                                      |
| RL Algorithm          | GRPO                                                         |
| Training Dataset      | [DeepScaleR-Preview-Dataset](https://huggingface.co/datasets/agentica-org/DeepScaleR-Preview-Dataset), 40k |
| Rollout Configuration | 128 prompts                                                  |
| Reward Function       | correctness reward + length penalty                          |
| Policy Optimization   | GRPO loss + length penalty loss                              |
| Benchmark             | AIME 2025, MATH, AMC, Olympiad-Bench, GPQA, LSAT, MMLU       |
| Core Insights         | Address the uncontrolled reasoning length issue in language models. It uses reinforcement learning to optimize for both accuracy and adherence to user - specified length constraints. By training models with a reward function that combines correctness and length - related terms, LCPO enables precise length control, allowing for a better trade - off between computational cost and accuracy in various reasoning tasks. |
| Additional Notes      |                                                              |





# 2025.03.06, STILL-3rd



| Project or Paper      | [An Empirical Study on Eliciting and Improving R1-like Reasoning Models](https://arxiv.org/pdf/2503.04548) |
| --------------------- | ------------------------------------------------------------ |
| GitHub                | https://github.com/RUCAIBox/Slow_Thinking_with_LLMs          |
| Backbone Model        | Qwen2.5-1.5B/7B/32B,   Qwen2.5-7B-Instruct                   |
| RL Algorithm          |                                                              |
| Training Dataset      |                                                              |
| Rollout Configuration |                                                              |
| Reward Function       |                                                              |
| Policy Optimization   |                                                              |
| Benchmark             |                                                              |
| Core Insights         |                                                              |
| Additional Notes      |                                                              |





# 2025.0310, MetaRL

| Project or Paper      | [Optimizing Test-Time Compute via Meta Reinforcement Fine-Tuning](https://arxiv.org/pdf/2503.07572) |
| --------------------- | ------------------------------------------------------------ |
| GitHub                | [CMU-AIRe/MRT](https://github.com/CMU-AIRe/MRT)              |
| Backbone Model        | DeepSeek-R1-Distill-Qwen-32B/7B/1.5B / DeepScaleR-1.5B-Preview /  Llama-3.1-8B/3B-Instruct |
| RL Algorithm          | MRT                                                          |
| Training Dataset      | None                                                         |
| Rollout Configuration | 256 prompts * 4 responses, temperature = 0.7                 |
| Reward Function       | 0/1 reward + dense reward                                    |
| Policy Optimization   | SFT Loss + Dense Reward Bonus Loss                           |
| Benchmark             | AIME 2024, AIME 2025, AMC 2023, MinervaMATH, MATH500         |
| Core Insights         | Treating test - time computation of LLMs as a meta - RL problem. It uses a progress - based reward function to guide the model, and optimizes the policy to balance exploration and exploitation, aiming to improve the efficiency and performance of LLMs at test time. |
| Additional Notes      |                                                              |



# 2025.0318, TOPR

| Project or Paper      | [Tapered Off-Policy REINFORCE Stable and efficient reinforcement learning for LLMs](https://arxiv.org/pdf/2503.14286v2) |
| --------------------- | ------------------------------------------------------------ |
| GitHub                | [None](http://None)                                          |
| Backbone Model        | Llama 3 8B/70B                                               |
| RL Algorithm          | Tapered Off-Policy REINFORCE (TOPR)                          |
| Training Dataset      | GSM8K and MATH                                               |
| Rollout Configuration | 64/8 solutions each question for GSM8k/MATH, respectively    |
| Reward Function       | Implicit Reward as DPO (contrastive learning with preference data |
| Policy Optimization   | Optimization with off-policy samples and without KL penalty  |
| Benchmark             | The performance of 8B language models can match with 70B-parameter model's on GSM8K and MATH |
| Core Insights         | Properly leveraging positive and negative examples alike in the off-policy regime simultaneously increases test-time accuracy and training data efficiency, all the while avoiding the “wasted inference” that comes with discarding negative examples. |
| Additional Notes      | This method may speed up learning while maintaining stable learning dynamics, without the use of KL regularization and online sampling. |



# 2025.0318, DAPO

| Project or Paper      | [DAPO: An Open-Source LLM Reinforcement Learning System at Scale](https://arxiv.org/pdf/2503.14476) |
| --------------------- | ------------------------------------------------------------ |
| GitHub                | [BytedTsinghua-SIA/DAPO](https://github.com/BytedTsinghua-SIA/DAPO) |
| Backbone Model        | Qwen2.5-32B-Base                                             |
| RL Algorithm          | DAPO                                                         |
| Training Dataset      | [BytedTsinghua-SIA/DAPO-Math-17k](https://huggingface.co/datasets/BytedTsinghua-SIA/DAPO-Math-17k), 17K |
| Rollout Configuration | 512 prompts * 16 responses Dynamic Sampling                  |
| Reward Function       | Rule-based Rewards + Length-Aware Penalty Reward (Overlong Filtering strategy)           |
| Policy Optimization   | DAPO loss, without KL loss                                   |
| Benchmark             | DeepSeek-R1-Zero-Qwen-32B level on AIME 2024                 |
| Core Insights         | DAPO introduces four key techniques: Clip-Higher to promote diversity and prevent entropy collapse; Dynamic Sampling to enhance training efficiency and stability; Token-Level Policy Gradient Loss to refine long-chain reasoning; and Overlong Reward Shaping to reduce reward noise and stabilize training. |
| Additional Notes      |                                                              |

# 2025.0320, Open RS

| Project or Paper      | [Reinforcement Learning for Reasoning in Small LLMs: What Works and What Doesn’t](https://arxiv.org/pdf/2503.16219) |
| --------------------- | ------------------------------------------------------------ |
| GitHub                | [knoveleng/open-rs](https://github.com/knoveleng/open-rs) |
| Backbone Model        | DeepSeek-R1-Distill-Qwen-1.5B                                                 |
| RL Algorithm          | GRPO                 |
| Training Dataset      | [open-s1](https://huggingface.co/datasets/knoveleng/open-s1), 18.6k</br>[open-deepscalar](https://huggingface.co/datasets/knoveleng/open-deepscaler), 21k</br>[open-rs](https://huggingface.co/datasets/knoveleng/open-rs), 7k</br>                             |
| Rollout Configuration | 24 prompts * 6 responses, Temperature = 0.7                                                          |
| Reward Function       | Rule-based Rewards with Cosine Reward assigning higher rewards to shorter but correct response.                                           |
| Policy Optimization   | GRPO       |
| Benchmark             | AIME2024, AMC, MATH500, Minerva Math and OlympiadBench       |
| Core Insights         | 1. High-quality data can boost performance compared with large amount low-quality data. 2. The difficulty of training data influences the training results. 3. Consine rewards can stabilize completion lengths, improving training consistency, |
| Additional Notes      |                                                              |

# 2025.0321, Oat-Zero

| Project or Paper      | [Understanding R1-Zero-Like Training: A Critical Perspective](https://github.com/sail-sg/understand-r1-zero/blob/main/understand-r1-zero.pdf) |
| --------------------- | ------------------------------------------------------------ |
| GitHub                | [sail-sg/understand-r1-zero](https://github.com/sail-sg/understand-r1-zero) |
| Backbone Model        | Qwen2.5-1.5B                                                 |
| RL Algorithm          | Dr. GRPO (fixes GRPO’s bias in optimization)                 |
| Training Dataset      | Questions sampled from the MATH;                             |
| Rollout Configuration | N/A                                                          |
| Reward Function       | Rule-based Rewards                                           |
| Policy Optimization   | Dr. GRPO Loss (remove two normalization terms in GRPO)       |
| Benchmark             | AIME2024, AMC, MATH500, Minerva Math and OlympiadBench       |
| Core Insights         | 1. The DeepSeek-V3-Base model exhibits significant reasoning capabilities, termed an “aha moment,” even prior to reinforcement learning fine-tuning. 2. GRPO introduces an optimization bias that artificially increases response length during training, particularly affecting incorrect outputs. |
| Additional Notes      |                                                              |

# 2025.0407, VAPO

| Project or Paper       | [VAPO: Efficient and Reliable Reinforcement Learning for Advanced Reasoning Tasks](https://arxiv.org/pdf/2504.05118) |
| ---------------------- | ------------------------------------------------------------ |
| GitHub                 | --                                                           |
| Backbone Model         | Qwen-32B base model                                          |
| RL Algorithm           | Value-based Augmented PPO                                    |
| Training Dataset       | N/A                                                          |
| Rollout Configuration  | N/A                                                          |
| Reward Function        | Rule-based Rewards                                           |
| Policy Optimization    | PPO                                                          |
| Benchmark              | AIME 2024 avg@32                                             |
| Core Insights          | VAPO integrates clip-higher, token-level loss, value-pretraining, decoupled-GAE, self-imitation learning and group-sampling. |
| Additional Notes       | First value-based RL training framework to outperform value-free methods on long COT tasks significantly |
| Training params (PPO)  | AdamW, actor_learning_rate=1e-6, critic_learning_rate=2e-6, warmup_constant scheduler. batch_size=8192, mini_batch_size=512, value network initialized using reward model, GAE \lambda=0.95, \gamma=1.0, sample-level loss was used, clip \epsilon=0.2 |
| Training params (VAPO) | value model first warmup for 50 steps before policy training.<br /> |





主实验超参/超参结论

论文主要结论



数据+超参都用一组

找到算法改动的最优组合



# 2025.04.13 Skywork-OR1



| Project or Paper      | https://pretty-radio-b75.notion.site/DeepCoder-A-Fully-Open-Source-14B-Coder-at-O3-mini-Level-1cf81902c14680b3bee5eb349a512a51 |
| --------------------- | ------------------------------------------------------------ |
| GitHub                | https://github.com/SkyworkAI/Skywork-OR1?tab=readme-ov-file  |
| Backbone Model        |                                                              |
| RL Algorithm          |                                                              |
| Training Dataset      |                                                              |
| Rollout Configuration |                                                              |
| Reward Function       |                                                              |
| Policy Optimization   |                                                              |
| Benchmark             |                                                              |
| Core Insights         |                                                              |
| Additional Notes      |                                                              |







# template





[An Empirical Study on Eliciting and Improving R1-like Reasoning Models](https://arxiv.org/pdf/2503.04548)



| Project or Paper      |      |
| --------------------- | ---- |
| GitHub                |      |
| Backbone Model        |      |
| RL Algorithm          |      |
| Training Dataset      |      |
| Rollout Configuration |      |
| Reward Function       |      |
| Policy Optimization   |      |
| Benchmark             |      |
| Core Insights         |      |
| Additional Notes      |      |





