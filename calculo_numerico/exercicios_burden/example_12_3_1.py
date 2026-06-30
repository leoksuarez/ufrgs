import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'metodos_numericos')))
from bvp_pdes import wave
import numpy as np
import tabulate

# define step sizes and bounds
h = 0.1
k = 0.05

x_bounds = np.array([0, 1])
t_bounds = np.array([0, 1])

# define number of subintervals and grid points
m = int((x_bounds[1] - x_bounds[0]) / h)
N = int((t_bounds[1] - t_bounds[0]) / k)

x_nodes = np.linspace(x_bounds[0], x_bounds[1], m + 1)
t_nodes = np.linspace(t_bounds[0], t_bounds[1], N + 1)

# define boundary conditions and initial conditions
boundary = {
    'left': np.zeros(N + 1),
    'right': np.zeros(N + 1)
}

initial = {
    'u0': lambda x: np.sin(np.pi * x),
    'u1': lambda x: np.zeros_like(x)
}

alpha = 2.0

# compute the exact solution
w_exact = lambda x, t: np.sin(np.pi * x) * np.cos(2 * np.pi * t)

# compute the numerical solution
w = wave(m, N, x_bounds, t_bounds, alpha, boundary, initial)

# compute the error
error = np.abs(w - w_exact(*np.meshgrid(x_nodes, t_nodes, indexing='ij')))

# print the results in a table
table = []
for i in range(m):
    table.append([x_nodes[i], w[i, -1], w_exact(x_nodes[i], t_bounds[-1]), error[i, -1]])

print(tabulate.tabulate(table, headers=['x', 'Numerical Solution', 'Exact Solution', 'Error'], tablefmt='orgtbl', floatfmt=('.2f', '.8f', '.8f', '.4e')))