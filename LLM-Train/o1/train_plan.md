1. 先得找一个能稳定长文本且性能不降的模型(或者自己训一个)
2. 高质量、范围广(math, coding, 通用推理都得有)、难度分梯度的数据集是RL稳定的关键。最好用另一个SFT LLM对数据集的domain、discipline、difficulty进行打标
3. 为了避免reward hacking，把容易猜出答案的题排除出去，如：多选、判断、证明题















