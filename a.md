| 算子 | 对应症状 | 占比 | 阈值 | 视觉特征 |
|---|---|---:|---|---|
| `high_impact_grasp` | 夹飞 | 5.4% | >0.04 m/s | eef 侧移中关爪，胶囊被推飞 |
| `hesitant_grasp` | 偏慢 | 3.0% | >25 frames | eef 在胶囊上方停顿/微调很久 |
| `slow_close` | 慢关爪 | 15.3% | >13 frames | 夹爪从开到闭拖很长 |
| `late_wrist_correction` | 对准差 | 9.3% | >0.2 rad | 临门前腕部突然扭转调角度 |
| `grasp_retry` | 失败重试 | 0.47% | ≤60 frames | 关爪→张开→又关爪 |



