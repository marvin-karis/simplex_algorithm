import numpy as np
from scipy.optimize import linprog

# Define the objective function and constraints
# For simplicity, this problem assumes a single resource to be allocated
c = [-1, -2, -3]  # minimize resource allocation cost
A = [[1, 1, 1], [10, 4, 5], [2, 2, 6]]  # resource constraints
b = [100, 600, 200]  # resource availability

# Solve the linear programming problem using the simplex method
result = linprog(c, A_ub=A, b_ub=b, method='simplex')

# Print the optimal resource allocation
print('Optimal resource allocation: ', result.x)

# Print the minimum resource allocation cost
print('Minimum resource allocation cost: ', -result.fun)
