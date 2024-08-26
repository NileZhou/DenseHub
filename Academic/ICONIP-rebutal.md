Submission Number: 6739

Article Title: “Masker: Speculative Decoding for Long-Text QA with CopyHead”

Authors: Yi Zhou, Haixia Pan, Ruijun Liu, Lingzhi Zhang

# Reviwer1

## Concern1

The paper seems to resemble Pointer Networks by Oriol Vinyals et al at Google Brain.

### Author response

Thank you sincerely for your insightful feedback and detailed guidance. We greatly appreciate your time and effort in evaluating our work.

We acknowledge the significance of Pointer Networks, which represent a notable contribution to the field. While drafting our paper, we carefully considered this work, particularly noting that Pointer Networks utilize an autoregressive approach, where each vector is generated sequentially by retrieving corresponding input vectors. However, our approach, CopyHead, introduces a fundamental difference: it operates in a non-autoregressive manner. Unlike Pointer Networks, which copy context vectors, CopyHead generates a mask of the context. This mask enables the generation of entire segments in a single iteration, thereby significantly improving the efficiency of the decoding process.

Furthermore, our research specifically focuses on accelerating text generation. Unlike Pointer Networks, which do not inherently offer acceleration benefits, CopyHead is designed to enhance speed. It achieves this by acting as a lightweight decoding head, where the computational cost of generating the output is significantly lower than that of generating a single token using the large model’s forward pass. To maintain the coherence of the output mask vector and address potential sparsity, we also made targeted adjustments to the loss function.

We hope this clarifies the distinct focus of our work and its contributions to the acceleration of text generation.

### Author action

We updated the manuscript by including a reference to the significant contribution of Pointer Networks in the Introduction section.

## Concern2

Consider adding standalone captions that concisely describe the figure at a high level.

### Author response

Dear Reviewer,

Thank you for your constructive suggestion. We understand the importance of providing clear and concise figure captions that effectively communicate the key points without relying on lengthy text in the body of the paper.

### Author action

We will revise the figure captions, including a clear definition of "prefix input embedding" in Figure 1, and ensure that all figures have standalone captions that describe their content at a high level.


## Concern3


### Author response


### Author action




# Reviewer2

## Concern1

# Reviewer3

## Concern1

Author response:
Author action: We updated the manuscript by ….
