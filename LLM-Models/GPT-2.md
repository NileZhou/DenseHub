# GPT2模型细节

Owner: Jock Nile

```
vocab_size = 50257 # openai's model vocabulary
block_size = 1024  # openai's model block_size
```

# Causal SelfAttention

忘记什么下三角为1还是0吧，为0为1都可以，关键看怎么实现。

应该记住：下三角（包括对角线）是活跃的元素，即可以和注意力矩阵进行计算的元素，这样序列中的一个元素可以“看到”它自己以及它之前的元素。

# 详解temperature

[https://ai.stackexchange.com/questions/32477/what-is-the-temperature-in-the-gpt-models](https://ai.stackexchange.com/questions/32477/what-is-the-temperature-in-the-gpt-models)

# 参考

自己从头预训练llama，与MinGPT相得益彰

[https://github.com/DLLXW/baby-llama2-chinese](https://github.com/DLLXW/baby-llama2-chinese)
