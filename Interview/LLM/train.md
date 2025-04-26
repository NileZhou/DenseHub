这是多轮对话训练时，targets(即labels)的情况，只有assistant回复部分不是-100

![image-20250415200327458](/Users/zhouyi9/Projects/DenseHub/Interview/LLM/_imgs/multi_turn.png)



input_ids和target 一一对应，input_ids里有每个数的token id



最后计算loss: 只有不为-100的地方才算loss

![image-20250415201234110](/Users/zhouyi9/Projects/DenseHub/Interview/LLM/_imgs/multi_turn2.png)


一次训练，只需要forward一次


