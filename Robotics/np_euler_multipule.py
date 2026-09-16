import numpy as np

# 1. 定义三个欧拉角 (直接写度数，用 np.radians 转成弧度)
roll  = np.radians(30)  # 绕X轴旋转 30度
pitch = np.radians(45)  # 绕Y轴旋转 45度
yaw   = np.radians(60)  # 绕Z轴旋转 60度

# 2. 构造 Rx(roll) 矩阵
Rx = np.array([
    [1, 0, 0],
    [0, np.cos(roll), -np.sin(roll)],
    [0, np.sin(roll),  np.cos(roll)]
])

# 3. 构造 Ry(pitch) 矩阵
Ry = np.array([
    [ np.cos(pitch), 0, np.sin(pitch)],
    [0, 1, 0],
    [-np.sin(pitch), 0, np.cos(pitch)]
])

# 4. 构造 Rz(yaw) 矩阵
Rz = np.array([
    [np.cos(yaw), -np.sin(yaw), 0],
    [np.sin(yaw),  np.cos(yaw), 0],
    [0, 0, 1]
])

# 5. 矩阵相乘得到最终的旋转矩阵 R
R = Rz @ Ry @ Rx

print("最终的 3x3 旋转矩阵 R (NumPy版):")
print(R)