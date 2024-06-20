import numpy as np
from scipy.optimize import linprog


c = [-2, -3]


A = [
    [1, 2],
    [3, 1]
]
b = [20, 30]


x0_bounds = (0, None)
x1_bounds = (0, None)


result = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds], method='highs')


if result.success:
    print(f"Optimal value: {-result.fun}")
    print(f"x1: {result.x[0]}")
    print(f"x2: {result.x[1]}")
else:
    print("No solution found.")
