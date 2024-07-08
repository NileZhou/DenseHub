聊天消息分话题聚类后再做RAG，然后构建history会比较好

开源项目:

- quivr(most popular) [link](https://github.com/QuivrHQ/quivr)

* LLaMA Index [https://github.com/run-llama/llama_index?tab=readme-ov-file](https://github.com/run-llama/llama_index?tab=readme-ov-file)
* RAGFlow [https://github.com/infiniflow/ragflow](https://github.com/infiniflow/ragflow)
* Cognita [https://github.com/truefoundry/cognita](https://github.com/truefoundry/cognita)

SELFRAG: 用特殊token

RAG目前存在的问题：

1. 切分破坏语义块连贯性，导致召回broken段
2. 召回的信息不加过滤，在上下文中引入无关信息
3. 数据更新不及时，怎么做到大量的情况下在线召回与更新
4. RAG质量如何评估：如ragas微调轻量级LLM裁判






# Graph-based (recommend)

[GraphRAG](https://github.com/microsoft/graphrag)
