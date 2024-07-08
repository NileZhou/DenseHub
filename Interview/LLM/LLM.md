reference:

- https://github.com/liguodongiot/llm-action  (大模型原理与实战，大而全)
- 

# Train中常见问题

## Loss问题汇总

1. loss不收敛： 一种是一直在震荡, 一种是loss下降一点后不再下降

解决：

- 查看是否有梯度回传,查看代码如下

反正无非打印传回梯度向量的mean 和 varance

```python
for name, parms in model.named_parameters():
	print('-->name:', name, '-->grad_requirs:', parms.requires_grad, '--weight', torch.mean(parms.data), ' -->grad_value:', torch.mean(parms.grad))
```

- 查看数据是否有问题 如标签错乱等现象
- 调节学习率，从大向小调，建议每次除以5
- 如果学习率调好后，需要调节batchsize大小，如调大2倍,则将学习率对应调大2-3倍;反之,学习率对应调小

1. loss变nan

排查顺序:

- 训练数据(包括label)中有无异常值(nan, inf等)
- 网络中有无除法,确保分母不会出现0, 分母可以加一个eps=1e-8
- 网络中有无开根号(torch.sqrt), 保证根号下>=0 解决也是加一个eps=1e-8
- 如果在迭代的100轮以内，出现NaN，可能是因为学习率过高，需要降低学习率
- 可能0或者负数作为自然对数
- 需要计算loss的数组越界（尤其是自己，自定义了一个新的网络，可能出现这种情况）
- 在某些涉及指数计算，可能最后算得值为INF（无穷）（比如不做其他处理的softmax中分子分母需要计算exp（x），值过大，最后可能为INF/INF，得到NaN，此时你要确认你使用的softmax中在计算exp（x）做了相关处理（比如减去最大值等等））
- 对于层数较多的情况，各层都做batch_nomorlization
- 梯度爆炸导致，gradient_clipping解决
- 有时候损失层中loss的计算可能导致NaN的出现。比如，给InfogainLoss层（信息熵损失）输入没有归一化的值，使用带有bug的自定义损失层等等

## 输出重复问题

简单的方法：增大batch size

比较俗套的解决方案：[https://zhuanlan.zhihu.com/p/659961396](https://zhuanlan.zhihu.com/p/659961396)

深入一点的原理分析：[https://arxiv.org/pdf/2206.02369](https://arxiv.org/pdf/2206.02369)

reddit上相关讨论：

[https://www.reddit.com/r/LocalLLaMA/comments/1ap8mxh/what_causes_llms_to_fall_into_repetitions_while/](https://www.reddit.com/r/LocalLLaMA/comments/1ap8mxh/what_causes_llms_to_fall_into_repetitions_while/)

NeuralFlow方案：[https://www.reddit.com/r/LocalLLaMA/comments/1apz94o/neuralflow_visualize_the_intermediate_output_of/](https://www.reddit.com/r/LocalLLaMA/comments/1apz94o/neuralflow_visualize_the_intermediate_output_of/)

Transformer Debugger:

[https://www.reddit.com/r/singularity/comments/1bco2aj/openai_releases_transformer_debugger/](https://www.reddit.com/r/singularity/comments/1bco2aj/openai_releases_transformer_debugger/)

github上大家的讨论:

[https://github.com/hiyouga/LLaMA-Factory/issues/1347](https://github.com/hiyouga/LLaMA-Factory/issues/1347)

代码错误导致的eos_id没有，导致输出重复：

[https://github.com/THUDM/ChatGLM2-6B/issues/270](https://github.com/THUDM/ChatGLM2-6B/issues/270)

具体来说，我们可以调整以下超参数：

1. 学习率：学习率控制了模型在每次更新时的步长大小。过大的学习率可能导致模型在优化过程中跳出局部最优解，过小的学习率则可能导致训练过程过于缓慢。适当的学习率可以减少模型重复内容生成的频率。
2. 批量大小：批量大小是指每次训练时使用的样本数量。过小的批量大小可能导致模型在训练数据中过度拟合，过大的批量大小则可能增加计算负担。合适的批量大小可以使模型更好地学习数据中的模式，并减少重复内容的生成。
3. 迭代次数：迭代次数是指训练模型的总次数。过少的迭代次数可能导致模型训练不充分，过多的迭代次数则可能使模型过度拟合训练数据。适当的的选择迭代次数可以使模型更好地学习数据，并减少重复内容的生成。

## 灾难性遗忘

**Catastrophic Forgetting**:

解决方案

1. 参数冻结，块扩张:

- 腾讯的LLaMA Pro  https://github.com/TencentARC/LLaMA-Pro
- LoRAMoE: 两组LoRA，一组学老任务，一组学新任务

[https://github.com/Ablustrund/LoRAMoE](https://github.com/Ablustrund/LoRAMoE)

1. 数据混合：拿一部分老数据

## 位置编码

有大坑：[https://zhuanlan.zhihu.com/p/651588659](https://zhuanlan.zhihu.com/p/651588659)



# Positional Encoding
