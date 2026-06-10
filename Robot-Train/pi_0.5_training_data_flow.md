# PI05 训练数据流完全指南

都在 /mnt/vepfs01/output/nickzhou/mozbrain 这个项目下
> 入口：`.gitlab/scripts/nick_ci_train_pi05.sh`

## 一、整体流程图

```
原始 moz1 数据集 (parquet + mp4)
        │
        ▼
StandardizedLeRobotDataset  ← ObservationStandardizer
        │ (use_raw_dataset: true)
        │  - 拼 observation.state (14D)
        │  - 计算 delta action (14D, chunk=60步)
        │  - resize 图像到 224×224
        ▼
PI05Policy.forward()
        │
        ├── prepare_images()     → 3 cameras [B, 3, 224, 224]
        ├── prepare_language()   → "Task: ..., State: ...;\nAction: " tokenized (80 tokens)
        ├── prepare_state()      → 14D → zero-pad → 32D
        └── prepare_action()     → 14D×60 → zero-pad → 32D×60
        │
        ▼
PaliGemma (2B) + Action Expert (300M Gemma)
        │ flow matching loss
        ▼
输出：预测 v_t = noise - action  (MSE loss)
推理时：60步 delta action chunk → unnormalize → 发给机器人
```

---

## 二、关键文件索引（阅读顺序）

### Step 1: 入口和配置
| 文件 | 作用 |
|------|------|
| `.gitlab/scripts/nick_ci_train_pi05.sh` | 训练启动脚本，CUDA 设备、端口 |
| `lerobot/scripts/configs/tasks/ci_train_pi05.yaml` | **最重要的配置文件**，控制所有训练参数 |
| `lerobot/common/policies/pi05/configuration_pi05.py` | PI05Config 数据类定义 |

**在 `ci_train_pi05.yaml` 里重点关注**：
```yaml
use_raw_dataset: true        # 启用标准化转换层
policy:
  type: "pi05"
  chunk_size: 60             # 预测未来60步
  n_action_steps: 60
  use_delta_joint_actions_aloha: true  # 注意：这里有点误导性名字，实际是 delta EEF
```

### Step 2: 原始数据结构
| 文件 | 作用 |
|------|------|
| `/mnt/vepfs01/output/qhj/ci_train_dataset/visualprompt/20250909_visualprompt_pickplace_370_ori/meta/info.json` | 所有原始 feature 的 shape/dtype 定义 |
| `meta/tasks.jsonl` | 任务描述（53个），如 "Put it on the egg tray" |
| `data/chunk-xxx/episode_xxxxxx.parquet` | 每个 episode 的逐帧数据 |
| `videos/chunk-xxx/{cam_name}/episode_xxxxxx.mp4` | 三个相机的视频 |

**原始数据的关键 features**（info.json 里可以看到完整列表）：
- `leftarm_state_cart_pos` (6D): 左臂末端笛卡尔位置 [x, y, z, rx, ry, rz]
- `leftarm_gripper_state_pos` (1D): 左夹爪状态
- `leftarm_cmd_cart_pos` (6D): 左臂末端命令位置（训练目标来源）
- `leftarm_gripper_cmd_pos` (1D): 左夹爪命令
- 右臂同上
- `cam_high`, `cam_left_wrist`, `cam_right_wrist`: 三个相机 240×320×3

### Step 3: 标准化转换层（关键！）
| 文件 | 作用 |
|------|------|
| `lerobot/common/robot_devices/transform_utils.py` | **最核心**，定义 ObservationConfig、IndexConfig、ObservationStandardizer |
| `lerobot/common/datasets/transformed_dataset.py` | StandardizedLeRobotDataset 实现 |

**在 `transform_utils.py` 里重点读**：

1. **`IndexConfig.STRUCTURE_CONFIG`（第 34 行）**：
   定义了各机器人结构在不同 space 下的维度分解：
   ```python
   'moz1_dualarm': {
       'eef_vec': {
           'components': ['leftarm_cmd_cart_pos', 'leftarm_gripper_cmd_pos',
                          'rightarm_cmd_cart_pos', 'rightarm_gripper_cmd_pos'],
           'sizes': [6, 1, 6, 1],  # 总共 14D
       }
   }
   ```

2. **`ObservationConfig`（第 287 行）**：
   注意默认值，当前训练**没有在 yaml 里覆盖** `observation_config`，所以用默认值：
   ```python
   robot_type: "arx_r5"   # ← 这里有个小问题！默认是 arx_r5 不是 moz1
                            #   但 arx_r5 eef_vec 也是 14D，维度碰巧相同
   state_space: "eef_vec"
   action_space: "eef_vec"
   use_delta_pos: True      # ← action 存的是增量！
   delta_space: "rotary"    # ← 旋转用 SO(3) 群乘法，不是简单相减
   ```

3. **`ObservationStandardizer._pack_vector`（第 727 行）**：
   把 dict of raw arrays → 单个向量：
   - state: 直接拼接各 state 字段
   - action: 计算 delta（cmd - state），旋转部分用 `R_cmd * R_state^{-1}`

4. **`StandardizedLeRobotDataset.__getitem__`（transformed_dataset.py 第 791 行）**：
   每个样本返回：
   ```python
   {
       "observation.state": Tensor([14]),          # 当前帧 state
       "action": Tensor([60, 14]),                 # 未来60帧 delta action
       "observation.images.cam_high": Tensor([3, 224, 224]),
       "observation.images.cam_left_wrist": Tensor([3, 224, 224]),
       "observation.images.cam_right_wrist": Tensor([3, 224, 224]),
       "task": "Put it on the egg tray",           # 自然语言任务
   }
   ```

### Step 4: Policy 模型
| 文件 | 作用 |
|------|------|
| `lerobot/common/policies/pi05/modeling_pi05.py` | PI05Policy（训练/推理入口），prepare_* 方法，forward |
| `lerobot/common/policies/pi05/paligemma_with_expert.py` | 双流 transformer（PaliGemma + Action Expert） |
| `lerobot/common/policies/pi05/models/paligemma.py` | PaliGemma 视觉语言模型 |
| `lerobot/common/policies/pi05/models/gemma.py` | Gemma LM（action expert 用的） |
| `lerobot/common/policies/pi05/models/siglip.py` | SigLIP 视觉编码器 |

**在 `modeling_pi05.py` 里重点读**：

1. **`prepare_images`（第 756 行）**：图像归一化 `img * 2.0 - 1.0`，即 [0,1] → [-1,1]

2. **`prepare_language`（第 789 行）**：**这是理解输入的关键！**
   ```python
   # state 被离散化成 0-255 的整数（每个维度一个 token）
   discretized_state = np.digitize(state, bins=np.linspace(-1, 1, 257)[:-1]) - 1
   # 最终 prompt 格式：
   full_prompt = f"Task: {task_text}, State: {state_str};\nAction: "
   # 例如：
   # "Task: Put it on the egg tray, State: 128 130 127 133 ...; \nAction: "
   ```

3. **`prepare_state`（第 835 行）**：
   ```python
   state = pad_vector(state, self.config.max_state_dim)  # 14D → 32D（补零）
   ```

4. **`forward`（第 670 行）**：flow matching 训练：
   ```python
   x_t = t * noise + (1 - t) * actions  # 在 noise 和 action 之间插值
   # 模型预测 v_t = noise - action（速度场）
   loss = MSE(u_t=noise-action, v_t=model_output)
   ```

---

## 三、输入/输出精确定义

### 模型输入
| 输入 | 形状 | 内容 |
|------|------|------|
| images | `[B, 3, 224, 224]` × 3 | cam_high + cam_left_wrist + cam_right_wrist，值域 [-1, 1] |
| lang_tokens | `[B, 80]` | "Task: {text}, State: {14个整数};\nAction: " 的 tokenid |
| lang_masks | `[B, 80]` | padding 位置为 False |
| state | `[B, 1, 32]` | 14D EEF state zero-pad 到 32D，min-max 归一化 |
| actions (训练时) | `[B, 60, 32]` | 60步 14D delta action zero-pad 到 32D |
| noise (训练时) | `[B, 60, 32]` | 高斯噪声，用于 flow matching |
| time (训练时) | `[B]` | t ∈ [0,1]，flow matching 时间步 |

### 模型输出（训练）
| 输出 | 形状 | 内容 |
|------|------|------|
| loss | scalar | MSE(noise - action, predicted_velocity_field) |

### 模型输出（推理）
| 输出 | 形状 | 内容 |
|------|------|------|
| actions | `[B, 60, 14]` | 60步 delta EEF action（unnormalize 后） |

**推理时输出的 14D action 含义**（eef_vec 空间）：
```
[0:3]   左臂 delta xyz (m)
[3:6]   左臂 delta 旋转向量 (rad，相对当前姿态的 SO(3) delta)
[6]     左夹爪绝对位置
[7:10]  右臂 delta xyz
[10:13] 右臂 delta 旋转向量
[13]    右夹爪绝对位置
```

---

## 四、容易踩的坑

### 坑1：observation_config 默认 robot_type 是 arx_r5
`ObservationConfig.robot_type` 默认是 `"arx_r5"` 不是 `"moz1"`，但当前 yaml 没有覆盖。
这不影响结果是因为：`arx_r5` 的 eef_vec 也是 [6,1,6,1]=14D，和 `moz1_dualarm` 相同。
但 **如果要 debug 或扩展，注意这个默认值陷阱**。

### 坑2：action 是 delta，不是绝对值
dataset 里存的 `leftarm_cmd_cart_pos` 是绝对命令，但经过 `_pack_vector` 后 action 变成了相对于当前 state 的增量。位置是线性差，旋转是 `R_cmd * R_state^{-1}`（SO3 群操作）。

### 坑3：state 既进入语言 prompt，也作为独立向量
state 同时被：
1. 离散化成 0-255 整数，嵌入到文本 prompt 里（语言理解路径）
2. 连续值 zero-pad 到 32D，作为 suffix embedding（运动控制路径）

### 坑4：max_action_dim=32 但实际有效维度只有 14
`action_out_proj` 输出 32D，但训练时 loss 只取前 `max_action_dim` 维（代码里 `losses[:, :, :self.config.max_action_dim]`），推理时 `unnormalize` 只处理真实维度。

---

## 五、快速 Fact-check 方法

**验证 state/action 维度**：
```bash
cd /mnt/vepfs01/output/nickzhou/mozbrain
python3 -c "
from lerobot.common.robot_devices.transform_utils import IndexConfig
print(IndexConfig.get_total_dim('arx_r5', None, 'eef_vec'))      # state_space
print(IndexConfig.get_total_dim('moz1', 'dualarm', 'eef_vec'))   # 和上面应该都是 14
"
```

**查看实际一条数据的 shape**：
```bash
python3 -c "
import pandas as pd
df = pd.read_parquet('/mnt/vepfs01/output/qhj/ci_train_dataset/visualprompt/20250909_visualprompt_pickplace_370_ori/data/chunk-000/episode_000058.parquet')
print(df.columns.tolist())
print(df.dtypes)
print(df.shape)
"
```

**查看 tasks**：
```bash
head -5 /mnt/vepfs01/output/qhj/ci_train_dataset/visualprompt/20250909_visualprompt_pickplace_370_ori/meta/tasks.jsonl
```

---

## 六、wandb 训练曲线在哪看

```
https://app.bandw.top/my-robot/lerobot/runs/xpt5mmic
```

---
