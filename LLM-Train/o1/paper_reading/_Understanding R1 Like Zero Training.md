1. aha moment(解题过程中的self reflection类语句)对accuracy提升没用，且早就在deepseek-v3-base里了，别一惊一乍的
2. 作者认为因为GRPO场景用的是rule based verifier，完全可以不需要KL惩罚项，省显存，而且可能性能提升天花板更高
3. GRPO的bias
- Response level bias: 在优势<0时，除以长度会导致：模型如果生成错误的回答的话，长度越长惩罚越小，所以模型在回答错误的时候会倾向生成更长的CoT
- Question level bias: 相对优势不应该除以标准差，这会导致组不同，对奖励的weight也不同 （**这里我和作者观点不一致**）

