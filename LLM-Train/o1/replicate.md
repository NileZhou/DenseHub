O1 replication work collection:

https://huggingface.co/collections/onekq-ai/r1-reproduction-works-67a93f2fb8b21202c9eedf0b

必读论文track:
https://github.com/hijkzzz/Awesome-LLM-Strawberry


# experience
## my own experience

## verl && DAPO
正规军

要看到ray port

export RAY_PORT=6379
export DASHBOARD_PORT=8265
ray start --head --port=$RAY_PORT --dashboard-host=0.0.0.0 --dashboard-port=$DASHBOARD_PORT

### replicate r1
- 1.5B模型, 7B模型都会出现completion length先下降，再上升的过程   
因为模型弱，会去先拿format reward   
但是1.5B的经常拿不到accurary reward，7B的能拿到一些   
<=7B的模型loss常会有尖刺   
训练一开始由于输出差的不多，KL 与 loss都是0，后面会增加   

### distill r1

1e-5, 2e-5的大学习率训出来很可能LLM通用领域问答都不会说话了
Qwen2.5 distill的时候最好用1e-6的学习率
distill后会出现一定cot过长及复读现象，需要DPO之类的压制下


https://huggingface.co/blog/open-r1/update-1

# Open-r1
https://github.com/huggingface/open-r1


# Open-r1-multimodal
https://github.com/EvolvingLMMs-Lab/open-r1-multimodal
open-r1 多模态的fork

# DeepScaler
https://github.com/agentica-project/deepscaler
1.5B打败O1，效果真的好

# O1-Journey
上交团队一直在做的实验报告
https://github.com/GAIR-NLP/O1-Journey?tab=readme-ov-file#about-the-team

# open thoughts
openthinker效果很好，数据集也开源了
https://github.com/open-thoughts/open-thoughts

# Fin O1
https://huggingface.co/papers/2502.08127
金融领域实践

# tools
https://github.com/huggingface/Math-Verify

