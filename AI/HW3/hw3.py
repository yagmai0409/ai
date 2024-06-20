import numpy as np
from scipy.optimize import linprog

# 目標函數的係數 (注意: linprog 進行的是最小化, 因此需要對係數取負)
c = [-3, -2, -5]

# 不等式約束矩陣和約束向量
A = [
    [1, 1, 0],
    [2, 0, 1],
    [0, 1, 2]
]
b = [10, 9, 11]

# 變數的上下界
x_bounds = (0, None)
y_bounds = (0, None)
z_bounds = (0, None)

# 呼叫 linprog 函數求解線性規劃問題
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds, z_bounds], method='highs')

# 輸出結果
if result.success:
    print(f"最優值: {-result.fun}")
    print(f"x: {result.x[0]}")
    print(f"y: {result.x[1]}")
    print(f"z: {result.x[2]}")
else:
    print("未找到解。")

