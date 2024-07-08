# Count Parameters

```python

for name, parameter in copyHead.named_parameters():
    print(name, parameter.numel(), parameter.requires_grad)

```

Taking CopyHead as an example:

q_proj (A+B): embed_dim * r + out_dim * r = 4096 * 32 + 32 * 32 = 132096

k_proj (A_B):  132096

v_proj (A+B): 132096

o_proj: out_dim = 32

pre_norm.weight: out_dim = 32


cross_attn: out_dim * out_dim * 4 = 32 * 32 * 4 * 4 =



参数量约为: 4 * r * (embed_dim+out_dim) + 4 * out_dim**2
