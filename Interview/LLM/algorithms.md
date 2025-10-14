
# log_probs_from_logits

**经典实现**: log softmax -> gather，但是耗显存+数值不稳定

**高效实现**：负的cross entropy



## 一、交叉熵到底是什么？

### 1️⃣ 场景
假设模型要预测下一个词（或类别），它输出一堆 **logits**（未归一化分数）：

\[
z = [z_1, z_2, ..., z_K]
\]

其中：
- \(K\)：类别数量（在 LLM 中，就是词表大小）
- \(z_j\)：模型对第 \(j\) 个词的“原始分数”

我们通过 **softmax** 把这些分数转成概率：

\[
p(j) = \frac{e^{z_j}}{\sum_{k=1}^K e^{z_k}}
\]

表示模型认为“下一个词是第 \(j\) 个词”的概率。

---

### 2️⃣ 真实答案
假设真实下一个词的类别编号是 \(y\)。

交叉熵损失定义为：

\[
\text{CE}(z, y) = -\log p(y)
\]

也就是说：
> 惩罚模型对“真实词”的概率太低。  
> 概率越小，惩罚越大（因为 \(-\log p(y)\) 越大）。

---

## 二、代入 softmax，得到常见公式

代入 \(p(y) = e^{z_y} / \sum_j e^{z_j}\)：

\[
\text{CE}(z, y) = -\log \frac{e^{z_y}}{\sum_j e^{z_j}} = -z_y + \log \sum_j e^{z_j}
\]

解释：
- \(z_y\)：模型给“正确词”打的分数  
- \(\log \sum_j e^{z_j}\)：所有词的“总热度”  

➡️ 我们希望让 \(z_y\) 尽量大，而其他 \(z_j\) 尽量小。

---

## 三、在 LLM 预测下一个 token 的例子

假设词表里只有 4 个词：

\[
[\text{the}, \text{cat}, \text{sat}, \text{dog}]
\]

模型看到前文 `"the"` 后，输出 logits：

\[
z = [1.2, 0.3, 2.1, -0.5]
\]

---

### Step 1️⃣：softmax 转概率

\[
p(j) = \frac{e^{z_j}}{\sum_k e^{z_k}}
\]

计算结果（近似）：

| 词 | logit \(z_j\) | 概率 \(p(j)\) |
|----|----------------|----------------|
| the | 1.2 | 0.23 |
| cat | 0.3 | 0.10 |
| sat | 2.1 | 0.62 |
| dog | -0.5 | 0.05 |

---

### Step 2️⃣：真实词
假设真实下一个词是 `"sat"`，对应索引 \(y=2\)。

交叉熵损失：

\[
\text{CE}(z, y) = -\log p(y) = -\log 0.62 = 0.478
\]

模型越接近正确答案（概率越高），loss 越小。

---

## 四、为什么“log-softmax”和“cross-entropy”等价？

从上式可得：

\[
\text{CE}(z, y) = -z_y + \log \sum_j e^{z_j} = -\text{log-softmax}(z)_y
\]

因此：

\[
\log p(y) = \text{log-softmax}(z)_y = -\text{CE}(z, y)
\]

✅ “取真实类的 log-softmax” = “负的交叉熵”  
也就是说，训练时我们其实是在**最大化真实 token 的 log-prob**。







