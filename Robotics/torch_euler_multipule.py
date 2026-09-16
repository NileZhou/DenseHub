import torch
import math

# 1. 定义三个欧拉角 (注意：PyTorch 中的三角函数需要用 弧度制 radians)
roll  = torch.tensor(math.pi / 6)  # 绕X轴旋转 30度
pitch = torch.tensor(math.pi / 4)  # 绕Y轴旋转 45度
yaw   = torch.tensor(math.pi / 3)  # 绕Z轴旋转 60度

# 2. 构造 Rx(roll) 矩阵
Rx = torch.tensor([
    [1., 0., 0.],
    [0., torch.cos(roll), -torch.sin(roll)],
    [0., torch.sin(roll),  torch.cos(roll)]
])

# 3. 构造 Ry(pitch) 矩阵
Ry = torch.tensor([
    [ torch.cos(pitch), 0., torch.sin(pitch)],
    [0., 1., 0.],
    [-torch.sin(pitch), 0., torch.cos(pitch)]
])

# 4. 构造 Rz(yaw) 矩阵
Rz = torch.tensor([
    [torch.cos(yaw), -torch.sin(yaw), 0.],
    [torch.sin(yaw),  torch.cos(yaw), 0.],
    [0., 0., 1.]
])

# 5. 矩阵相乘得到最终的旋转矩阵 R
R = Rz @ Ry @ Rx

print("最终的 3x3 旋转矩阵 R:")
print(R)