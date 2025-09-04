

# 常用方法


- num_parameters : 输出总参数量

```python
# 计算并打印模型的总参数量
total_params = model.num_parameters()
print(f'Total number of parameters: {total_params}')
```

- \<model\>.parameters(): 得到parameters的generator()

```python
model_parameters = list(filter(lambda p: p.requires_grad, model.parameters()))
```


- half() : 将模型的参数转换为FP16格式

- from_pretrained():从预训练模型加载模型权重

- save_pretrained(): 将模型权重和配置保存到指定目录

- eval(): 将模型设置为评估模式。这在评估或推理时很重要，以禁用某些层（如 dropout）

- train(): 将模型设置为训练模式。这在训练期间很重要，以启用某些层（如 dropout）

- to(): 将模型移动到指定设备（如 CPU 或 GPU）


- transformers.dynamic_module_utils.get_class_from_dynamic_module  
动态加载外部代码并执行。加载外部vocabulary.py   实现根本的解耦  安全性有影响
底层原理是python的 importlib.import_module(module_path)  能把这个外部python文件加载进来变成一个类
然后调用这个类的方法



# Trainer


## lifecycle

- on_init
- on_


```text
_inner_training_loop:
  on_
```


### training_step

inputs: Dict[str, Union[torch.Tensor, Any]]
- input_ids
    - shape: (bsz, longest length in this batch)
    - Tips: if some sample not long enough, append pad_token(default 0) to its tail
- labels
   - shape: (bsz, longest length in this batch)
   - Tips: if some token should be ignored, the label in that position will been set to -100. 
- attention_mask
- position_ids
- pixel_values
- image_flags


labels被设置为-100: 避免计算loss时将这一部分token算进去:
- padding token
- 在autoregressive model中，计算输出时，避免模型在计算loss时“看到”未来的信息



## key methods

1. num_tokens

@staticmethod    
def num_tokens(train_dl: DataLoader, max_steps: Optional[int] = None) -> int:


num_steps_per_epoch = ceil(num_examples // bsz) / gradient_accumulation_steps 

## key classes
- trainer_callback#TrainerCallback

- trainer_callback#TrainerControl   
一个dataclass，主要包含这些属性:
  -  should_training_stop: bool = False
  -  should_epoch_stop: bool = False
  -  should_save: bool = False
  -  should_evaluate: bool = False
  -  should_log: bool = False

- trainer_callback#TrainerState
保存断点续跑/监控/记录所需的状态数据
一个dataclass,部分属性:  
  -  epoch: Optional[float] = None
  -  global_step: int = 0
  -  max_steps: int = 0
  -  logging_steps: int = 500
  -  eval_steps: int = 500
  -  save_steps: int = 500
  -  train_batch_size: int = None
  -  num_train_epochs: int = 0
  -  num_input_tokens_seen: int = 0
  -  total_flos: float = 0
  -  best_metric: Optional[float] = None
  -  best_model_checkpoint: Optional[str] = None
  -  trial_name: str = None
  -  trial_params: Dict[str, Union[str, float, int, bool]] = None
  -  stateful_callbacks: List["TrainerCallback"] = None

