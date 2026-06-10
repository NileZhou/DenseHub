LLM 是怎么工作的

输入一段文字 → Transformer → 预测下一个 token。
Fine-tune 时：给定 (prompt, target_response)，让模型学会生成 target。

---
PI05 本质上在做同一件事

只是把"生成文字"换成了"生成机器人动作序列"。

类比：
LLM:   (用户问题) → 模型 → (回答文字，一个token一个token)
PI05:  (任务描述 + 相机画面 + 当前手臂位置) → 模型 → (未来60步怎么动)

---
输入是什么

1. 任务描述（就是 prompt）

"Put it on the egg tray"
这就是 system prompt，告诉机器人现在要干什么。

2. 相机画面（等价于图片理解）

三个摄像头：头顶一个俯视，左右腕各一个。每帧图像 224×224。
这就是 vision token，和 GPT-4V 处理图片一模一样，SigLIP 把图像编成 patch embeddings。

3. 当前手臂位置（额外的 context）

机器人现在手在哪、转了多少度。这是 14 个浮点数（左臂 xyz + 旋转 + 夹爪，右臂同），被离散化成 0-255 的整数，直接塞进文字 prompt 里：

"Task: Put it on the egg tray, State: 128 134 127 129 133 131 200 129 131 127 130 134 180;\nAction: "

是不是很眼熟？这就是 in-context learning 的风格——把结构化数据序列化成文字喂给 LLM。

---
输出是什么

不是下一个 token，而是未来 60 帧的手臂动作。

每帧动作是 14 个浮点数，表示"相对于现在，手要移动多少"（delta，增量）：
[左手 Δx, Δy, Δz, Δrx, Δry, Δrz, 夹爪, 右手 Δx, Δy, Δz, Δrx, Δry, Δrz, 夹爪]

一次输出 60 帧，相当于 LLM 的 chunk decoding——不是 next token，而是一口气生成 60 个。30fps 的话就是未来 2 秒的动作。

---
训练目标是什么

LLM fine-tune 用交叉熵：预测的 token 概率分布 vs 真实 token。

PI05 用的是 Flow Matching，本质是：
- 训练数据里有真实动作序列（示范动作）
- 给模型一个带噪声的动作序列（噪声 + 真实动作的插值）
- 让模型预测"这个噪声应该怎么去掉"（速度场）
- 推理时，从纯噪声出发，按模型预测的方向迭代 10 步，得到干净的动作序列

类比 diffusion LLM，只是这里 diffusion 的对象是连续的动作向量而不是 token。

---
训练数据从哪来

人工遥操作：人控制机械臂完成任务，记录下所有传感器数据。

数据集里存的：
- 每一帧的相机画面（视频 mp4）
- 每一帧机器人的真实状态（手在哪）
- 每一帧人给的命令（手应该去哪）

训练时，(当前状态, 任务描述, 图像) → 预测 (未来60帧命令)。这就是 behavior cloning（行为克隆），模仿人的操作。

---
模型架构类比

PaliGemma (3B, VLM)       ← 等价于 GPT-4V，理解图像 + 语言
    +
Action Expert (300M Gemma) ← 专门生成动作的"解码头"

两个模型联合 attention：VLM 提供"理解"，Action Expert 提供"执行"。注意力是单向的——VLM 不能看 action token，但 action expert
可以看到图像和语言理解的结果。就像 encoder-decoder，但共享 KV cache。

---
一句话总结

PI05 = (PaliGemma 看图+读任务描述) + (Action Expert 生成未来2秒的机器人手臂轨迹)，训练数据是人遥操作的演示录像，用 Flow Matching
而不是交叉熵来优化连续的动作输出。
