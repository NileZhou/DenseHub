# Retrive-Read RAG

naive RAG

## steps

Indexing -> Retrieval -> LLM Generation



### 1. Indexing (**offline**)



a.  Extract information from humonous data sources (PDF, HTML, Markdown, Word. etc.)

b.  Split chunks

c.  Generate embeddings for the chunks using the embedding model

d.  Build an index as a connection between the embedding and the chunk



### 2. Retrieval (**online**)



a.  Convert the user query into a query embedding

b.  Find the nearest k chunk embeddings corresponding to the query embedding

c.  Extract the information from those k chunks

### 3. Generation (**online**)

a.  Combine the information from chunks and the user query, then send it to the LLM.

## challenges

- Retrieval Challenges

  a.  **Low precision**: Irrelevant or misaligned chunks leading to hallucinations responses

  b.  **Low recall**: Failure to retrieve relevant information, which can lead to incomplete or insufficient responses. Addressing complex queries often requires multiple retrievals or rewriting user query to gather sufficient context

- Generate based on relevant chunks

  The LLM fail to generate answers based on the retrieved chunks, or it utilize irrelevant chunks, resulting in discrepancies in the output.

- Coherent Challenges
  Integrating retrieved information can lead to incoherent outputs and redundancy from similar sources.

- Over-reliance on augmented information

  The output may simply summarize or repeat the augmented chunks, disregarding the LLM's knowledge, resulting in responses that lack insight or synthesis.

  

# RAG with Pre/Post Retrieval 

  

User Query -> Pre-Retrieval -> Retrieval -> Post-Retrieval -> LLM Generation

## Pre-retrieval



### Optimize data structure of source (offline)



#### unstructured data

unstructured data: text, audio, video, image

##### text



##### audio



##### video



##### image



#### semi-structured data

semi-structured data: PDF, Word, etc...

##### PDF

meet-table challenges:

- Text splitting processes may separate tables, leading to data corruption
- Incorporating tables into retrieval source data complicate semantic similarity search process

meet-table solution (not optimal):

- Leveraging code capabilities of LLMs to execute Text-2-SQL queries on tables within databases
- Transforming tables into text format using text-based methods

#### structured data

##### Knowledge Graph

- KnowlegeGPT / GraphRAG generates KB search queries and stores knowledge in a personalized base
- G-Retriever integrates Graph Neural Networks (GNNs) to enhance graph comprehension and question-answering 

##### Database

Text-2-SQL



#### Exploiting LLM's internal Knowledge

 

- Judger

**SKR** (Self-Knowledge guided Retrieval augmentation) classifies questions as known or unknown, applying retrieval enhancement selectively.

[Self-Knowledge Guided Retrieval Augmentation for Large Language Models](https://arxiv.org/abs/2310.05002)

- Replace retriever with LLM generator

[Generate rather than Retrieve: Large Language Models are Strong Context Generators](https://arxiv.org/abs/2209.10063)

- 





- Optimize indexing (**offline**)

  a.  Choose appropriate granularity(数据粒度)

  b.  Refine index structures

  c.  Add metadata

  d.  Optimize alignment

  e.  Implement mixed retrieval

- Optimize user query (**online**)

  Clarify the user's original question to enhance its suitability for retrieval

  a.  Rewrite the query

  b.  Expand the query



## Post-retrieval



### Re-Ranking



考虑到Lost in the middle, put the best docs 

### Prompt Compression

Compress the unrelated context prompt, decrease the noise in context



#  RAG Optimization



## Loading optimization



越来越多的工作把知识图谱 (Knowledge Graph) Introduce到RAG中，如:

- KnowledGPT 用于推理阶段
- SUGRE 用于微调阶段

## Indexing optimization



index optimization:

- add meta data for chunk content (time, type, title, subtitle, part of doc)
- chunk optimization 
- structrure corpus

## Embedding optimization





## Query Optimization





## Retrieve Optimization





# Evaluation



frameworks:

- RAGAS
- RAGChecker



## retrieval evaluation



Retrieval **complete** context, and these context are **relevant**, and ranked by relevant score.

### Context Relevance

relevance = 召回docs中与query相关的doc数 / 总召回doc数

实际场景用的次多，recall不好算数据库中总相关doc数



类似context relevance的有HitRate@K:

评估LLM给出的topk个doc中，有多少是实际有用的，分母是总召回doc的topk



### Context Recall

该指标常用于bootstrap阶段，后续提升几乎不可用

recall = 召回docs中与query相关的doc数 / 数据库中总相关doc数



Context Relevance和Context Recall可组成F1 score:

F1 = 2 * relevance * recall / (relevance + recall)



### Context Precision and MAP

first, choose a subset(topk) of retrieved docs

precision = topk docs中与query相关的doc数 / k

expansion: Mean Average Precision （MAP）
$$
MAP@K = \frac{1}{K}\sum_{k=1}^K \text{precision}_k
$$
实际场景用的最多



假设一个具体例子： 用户查询："公司的休假制度" 相关文档总共3个: doc1, doc2, doc4 系统返回排序结果: [doc1, doc3, doc2, doc4, doc5]

在每个位置计算precision:

```shell
# 在每个位置计算Precision:
position1 (doc1): 1/1    (找到1个相关/已返回1个)
position2 (doc3): 1/2    (找到1个相关/已返回2个)
position3 (doc2): 2/3    (找到2个相关/已返回3个)
position4 (doc4): 3/4    (找到3个相关/已返回4个)
position5 (doc5): 3/5    (找到3个相关/已返回5个)
```

MAP@5就是上面分数的平均



### MRR (Mean Reciprocal Rank)


$$
MRR = \frac{1}{Q} \sum_{q=1}^Q\frac{1}{rank_q}
$$
Q is the number of queries, rank_q 是第q个查询的**第一个**相关文档的排名

> MRR评估的是“平均来说，系统多快能够在响应用户查询时检索到第一个相关文档？”  其对排序质量相当敏感



与MAP比较:

- MAP考虑所有相关文档的位置，MRR只考虑第一个
- MAP能更全面地评估系统性能，MRR更关注快速找到首个相关文档





### NDCG

Normalized Discounted Cumulative Gain: 归一化折扣累积增益

缺点:需要详细的相关性标注（多级相关性）

它的特点是考虑到文档的相关程度（可以是多级相关性）以及排序位置的重要性



计算组成部分:

- DCG (Discounted Cumulative Gain)：考虑位置折扣的累积增益

- IDCG (Ideal DCG)：理想情况下的DCG（相关文档按相关性排序）

- NDCG = DCG / IDCG：归一化，使得不同查询可比



计算过程:

假设我们对文档相关性进行0-3的评分：

- 3分：非常相关
- 2分：相关
- 1分：一般相关
- 0分：不相关

例如查询"公司休假制度"：

系统返回序列: [doc1, doc3, doc2, doc4, doc5] 

相关性评分: [3, 0, 2, 2, 0]





相比MAP和MRR：

- MAP：只考虑二元相关性（相关/不相关）
- MRR：只关注第一个相关文档
- NDCG：同时考虑多级相关性和位置权重

## generation evalutation



### BLEU



### ROUGE





latency of online pipeline



cost of offline pipeline



