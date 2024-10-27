more complete: [quchangle/LLM-Tool-Survey](https://github.com/quchangle1/LLM-Tool-Survey?tab=readme-ov-file#tuning-free-methods-1)， corresponding paper: [paper](https://arxiv.org/pdf/2405.17935)

# Task Programming

| paper | code | main authors | date | description |
| ----- | ---- | ------------ | ---- | ----------- |
|       |      |              |      |             |
|       |      |              |      |             |

# Tool Selection (All-tools mode)

| paper                                                        | code                                                         | main authors                                                 | date       | description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ---------- | ------------------------------------------------------------ |
| [AnyTool: Self-Reflective, Hierarchical Agents for Large-Scale API Calls](https://arxiv.org/abs/2402.04253) | [code](https://github.com/dyabel/AnyTool?tab=readme-ov-file) | *[Yu Du](https://arxiv.org/search/cs?searchtype=author&query=Du,+Y), [Fangyun Wei](https://arxiv.org/search/cs?searchtype=author&query=Wei,+F)* | 2024-02-06 | Massive API Selection, tools are organized as hierarchy tree |
| [ToolNet: Connecting Large Language Models with Massive Tools via Tool Graph](https://arxiv.org/abs/2403.00839) |                                                              | *[Xukun Liu](https://arxiv.org/search/cs?searchtype=author&query=Liu,+X), [Zhiyuan Peng](https://arxiv.org/search/cs?searchtype=author&query=Peng,+Z)* | 2024-02-29 | Massive API Selection, tools are organized as graph          |
| [ToolGen: Unified Tool Retrieval and Calling via Generation](https://arxiv.org/pdf/2410.03439) | [code](https://github.com/Reason-Wang/ToolGen)               | [Renxi Wang](https://scholar.google.com/citations?user=7FnyQbsAAAAJ&hl=en), [Xudong Han](https://scholar.google.com.au/citations?hl=en&user=snUr8n8AAAAJ&view_op=list_works&sortby=pubdate) | 2024-10-08 | Over 47,000 tools, one token by one too                      |
|                                                              |                                                              |                                                              |            |                                                              |

# Tool Calling

| paper | code | main authors | date | description |
| ----- | ---- | ------------ | ---- | ----------- |
|       |      |              |      |             |
|       |      |              |      |             |

# Response Generation

# Advanced topics

# Tools in programmatic contexts

- Domain-specific logical forms to query structured data

  **Semantic parsing on freebase from question-answer pairs** *Berant, Jonathan, et al.* 2013 [[Paper]](https://aclanthology.org/D13-1160/)

  **Spider: A large-scale human-labeled dataset for complex and cross-domain semantic parsing and text-to-sql task** *Yu, Tao, et al.* 2018.09 [[Paper]](https://aclanthology.org/D18-1425/)

  **Break It Down: A Question Understanding Benchmark** *Wolfson, Tomer, et al.* 2020 [[Paper]](https://aclanthology.org/2020.tacl-1.13/)
- Domain-specific actions for agentic tasks such as web navigation

  **Reinforcement Learning on Web Interfaces using Workflow-Guided Exploration** *Liu, Evan Zheran, et al.* 2018.02 [[Paper]](https://openreview.net/forum?id=ryTp3f-0-)

  **WebShop: Towards Scalable Real-World Web Interaction with Grounded Language Agents** *Yao, Shunyu, et al.* 2022.07 [[Paper]](https://arxiv.org/abs/2207.01206)

  **Webarena: A realistic web environment for building autonomous agents** *Zhou, Shuyan, et al.* 2023.07 [[Paper]](https://arxiv.org/abs/2307.13854)
- Using external Python libraries as tools

  **ToolCoder: Teach Code Generation Models to use API search tools** *Zhang, Kechi, et al.* 2023.05 [[Paper]](https://arxiv.org/abs/2305.04032)
- Using expert designed functions as tools to answer questions about images

  **Visual Programming: Compositional visual reasoning without training** *Gupta, Tanmay, and Aniruddha Kembhavi.* 2023 [[Paper]](https://openaccess.thecvf.com/content/CVPR2023/papers/Gupta_Visual_Programming_Compositional_Visual_Reasoning_Without_Training_CVPR_2023_paper.pdf)

  **Vipergpt: Visual inference via python execution for reasoning** *Surís, Dídac, Sachit Menon, and Carl Vondrick.* 2023 [[Paper]](https://openaccess.thecvf.com/content/ICCV2023/papers/Suris_ViperGPT_Visual_Inference_via_Python_Execution_for_Reasoning_ICCV_2023_paper.pdf)
- Using GPT as a tool to query external Wikipedia knowledge for table-based question answering

  **Binding Language Models in Symbolic Languages** *Cheng, Zhoujun, et al.* 2022.10 [[Paper]](https://openreview.net/forum?id=lH1PV42cbF)
- Incorporate QA API and operation APIs to assist table-based question answering

  **API-Assisted Code Generation for Question Answering on Varied Table Structures** *Cao, Yihan, et al.* 2023.12 [[Paper]](https://aclanthology.org/2023.emnlp-main.897)

# Tool creation and reuse

- Approaches to abstract libraries for domain-specific logical forms from a large corpus

  **DreamCoder: growing generalizable, interpretable knowledge with wake--sleep Bayesian program learning** *Ellis, Kevin, et al.* 2020.06 [[Paper]](https://arxiv.org/abs/2006.08381)

  **Leveraging Language to Learn Program Abstractions and Search Heuristics]** *Wong, Catherine, et al.* 2021 [[Paper]](https://proceedings.mlr.press/v139/wong21a.html)

  **Top-Down Synthesis for Library Learning** *Bowers, Matthew, et al.* 2023 [[Paper]](https://doi.org/10.1145/3571234)

  **LILO: Learning Interpretable Libraries by Compressing and Documenting Code** *Grand, Gabriel, et al.* 2023.10 [[Paper]](https://openreview.net/forum?id=TqYbAWKMIe)
- Make and learn skills (Java programs) in the embodied Minecraft world

  **Voyager: An Open-Ended Embodied Agent with Large Language Models** *Wang, Guanzhi, et al.* 2023.05 [[Paper]](https://arxiv.org/abs/2305.16291)
- Leverage LMs as tool makers on BigBench tasks

  **Large Language Models as Tool Makers** *Cai, Tianle, et al.* 2023.05 [[Preprint]](https://arxiv.org/pdf/2305.17126)
- Create tools for math and table QA tasks by example-wise tool making

  **CREATOR: Disentangling Abstract and Concrete Reasonings of Large Language Models through Tool Creation** *Qian, Cheng, et al.* 2023.05 [[Paper]](https://arxiv.org/pdf/2305.14318)
- Make tools via heuristic-based training and tool deduplication

  **CRAFT: Customizing LLMs by Creating and Retrieving from Specialized Toolsets** *Yuan, Lifan, et al.* 2023.09 [[Paper]](https://arxiv.org/abs/2309.17428)
- Learning tools by refactoring a small amount of programs

  **ReGAL: Refactoring Programs to Discover Generalizable Abstractions** *Stengel-Eskin, Elias, Archiki Prasad, and Mohit Bansal.* 2024.01 [[Preprint]](https://arxiv.org/abs/2401.16467)
- A training-free approach to make tools via execution consistency

  **TroVE: Inducing Verifiable and Efficient Toolboxes for Solving Programmatic Tasks** *Wang, Zhiruo, Daniel Fried, and Graham Neubig.* 2024.01 [[Preprint]](https://arxiv.org/abs/2401.12869)

# Evaluation

## Repurposed existing datasets

- Datasets that require reasoning over texts

  **Measuring Mathematical Problem Solving With the MATH Dataset** *Hendrycks, Dan, et al.* 2021.03 [[Paper]](https://arxiv.org/pdf/2103.03874)

  **Beyond the Imitation Game: Quantifying and extrapolating the capabilities of language models** *Srivastava, Aarohi, et al.* 2022.06 [[Paper]](https://openreview.net/forum?id=uyTL5Bvosj)
- Datasets that require reasoning over structured data, e.g., tables

  **Dynamic Prompt Learning via Policy Gradient for Semi-structured Mathematical Reasoning** *Lu, Pan, et al.* 2022.09 [[Paper]](https://arxiv.org/pdf/2209.14610)

  **Compositional Semantic Parsing on Semi-Structured Tables** *Pasupat, Panupong, and Percy Liang.* 2015 [[Paper]](https://aclanthology.org/P15-1142)

  **HiTab: A Hierarchical Table Dataset for Question Answering and Natural Language Generation** *Cheng, Zhoujun, et al.* 2022 [[Paper]](https://aclanthology.org/2022.acl-long.78/)
- Datasets that require reasoning over other modalities, e.g., images and image pairs

  **Gqa: A new dataset for real-world visual reasoning and compositional question answering** *Hudson, Drew A., and Christopher D. Manning.* 2019.02 [[Paper]](https://arxiv.org/abs/1902.09506)

  **A Corpus for Reasoning about Natural Language Grounded in Photographs** *Suhr, Alane, et al.* 2019 [[Paper]](https://aclanthology.org/P19-1644)
- Example datasets that require retriever model (tool) to solve

  **Natural Questions: A Benchmark for Question Answering Research** *Kwiatkowski, Tom, et al.* 2019 [[Paper]](https://aclanthology.org/Q19-1026)

  **TriviaQA: A Large Scale Distantly Supervised Challenge Dataset for Reading Comprehension** *Joshi, Mandar, et al.* 2017 [[Paper]](https://aclanthology.org/P17-1147)

## Aggregated API benchmarks

- Collect RapidAPIs and use models to synthesize examples for evaluation

  **ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs** *Qin, Yujia, et al.* 2023.07 [[Paper]](https://openreview.net/forum?id=dHng2O0Jjr)
- Collect APIs from PublicAPIs and use models to synthesize examples

  **ToolAlpaca: Generalized Tool Learning for Language Models with 3000 Simulated Cases** *Tang, Qiaoyu, et al.* 2023.06 [[Preprint]](https://arxiv.org/abs/2306.05301)
- Collect APIs from PublicAPIs and manually annotate examples for evaluation

  **API-Bank: A Comprehensive Benchmark for Tool-Augmented LLMs** *Li, Minghao, et al.* 2023.12 [[Paper]](https://aclanthology.org/2023.emnlp-main.187/)
- Collect APIs from OpenAI plugin list and use models to synthesize examples

  **MetaTool Benchmark for Large Language Models: Deciding Whether to Use Tools and Which to Use** *Huang, Yue, et al.* 2023.10 [[Paper]](https://openreview.net/forum?id=R0c2qtalgG&referrer=%5Bthe%20profile%20of%20Neil%20Zhenqiang%20Gong%5D(%2Fprofile%3Fid%3D~Neil_Zhenqiang_Gong1))
- Collect neural model tools from Huggingface hub, TorchHub, and TensorHub

  **Gorilla: Large language model connected with massive apis** *Patil, Shishir G., et al.* 2023.05 [[Paper]](https://arxiv.org/abs/2305.15334)
- Collect neural model tools from Huggingface

  **HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in Hugging Face** *Shen, Yongliang, et al.* 2024 [[Paper]](https://openreview.net/forum?id=yHdTscY6Ci)
- Collect tools from Huggingface and PublicAPIs

  **Taskbench: Benchmarking large language models for task automation** *Shen, Yongliang, et al.* 2023.11 [[Paper]](https://openreview.net/forum?id=70xhiS0AQS&referrer=%5Bthe%20profile%20of%20Xu%20Tan%5D(%2Fprofile%3Fid%3D~Xu_Tan1))

  **StableToolBench: Towards Stable Large-Scale Benchmarking on Tool Learning of Large Language Models** `<br />`
  *Zhicheng Guo, Sijie Cheng, etc.* [[pdf](https://arxiv.org/abs/2403.07714)]

# Benchmark & Metrics

data:

| DataseName                                                                                  | language | ToolRetrieval | Tool Filler | Tool Parser |
| :------------------------------------------------------------------------------------------ | :------- | :------------ | :---------- | :---------- |
| ToolBench-g1                                                                                | en       | 423734/484    | -           | -           |
| [ToolBench](https://github.com/OpenBMB/ToolBench)                                              | en       | 423734/484    | 44939/484   | 19354/215   |
| [APIBank](https://github.com/AlibabaResearch/DAMO-ConvAI/blob/main/api-bank/data/all_apis.csv) | en       | 429/79        | 429/79      | 429/79      |
| [ToolAlpaca](https://github.com/tangqiaoyu/ToolAlpaca/blob/main/data/train_data.json)          | en       | 5911/198      | 5911/198    | 5803/198    |
| ToolLuban                                                                                   | zh       | 10239/234     | 10239/234   | 5605/185    |
| [MetaTool](https://github.com/HowieHwong/MetaTool?tab=readme-ov-file)                          | en       |               |             |             |

- Tool Retrieval：
  - data structure：<query, api_name, api_desc>
- Tool Filler：
  - data structure：<query, api_spec, api_param>
- Tool Parser：
  - data structure：<query, api_spec, response, select_keys

metrics:

- Tool Retrieval：
  - metric：Recall Top@1、Top@3、Top@5, to assess the retrieval effectiveness of the tool dataset
- Tool Filler
  - metric：Accuracy, to assess the ability of tool filler.
- Tool Parser
  - metric：Accuracy, to assess the ability of tool parser.

ToolBenchOn [papersWithCode](https://paperswithcode.com/sota/trajectory-planning-on-toolbench)
