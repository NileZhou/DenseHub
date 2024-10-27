

[TOC]



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









# Evaluation



latency of online pipeline



cost of offline pipeline





