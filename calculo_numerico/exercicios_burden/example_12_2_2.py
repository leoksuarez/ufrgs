import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'metodos_numericos')))
from bvp_pdes import heat_backward_sor, heat_backward_crout, heat_cn_crout
import numpy as np
import tabulate

# define step sizes and bounds
h = 0.1
k = 0.01

x_bounds = np.array([0, 1])
t_bounds = np.array([0, 0.5])

# define number of subintervals and grid points
m = int((x_bounds[1] - x_bounds[0]) / h)
N = int((t_bounds[1] - t_bounds[0]) / k)

x_nodes = np.linspace(x_bounds[0], x_bounds[1], m + 1)
t_nodes = np.linspace(t_bounds[0], t_bounds[1], N + 1)

# define boundary conditions and initial condition
boundary = {
    'left': np.zeros(N + 1),
    'right': np.zeros(N + 1)
}

initial = lambda x: np.sin(np.pi * x)
alpha = 1.0

# compute the numerical solution
w_sor = heat_backward_sor(m, N, x_bounds, t_bounds, alpha, boundary, initial)
w_crout = heat_backward_crout(m, N, x_bounds, t_bounds, alpha, boundary, initial)
w_cn = heat_cn_crout(m, N, x_bounds, t_bounds, alpha, boundary, initial)


# compute the exact solution and error
w_exact = lambda x, t: np.exp(- np.pi**2 * t) * np.sin(np.pi * x)
error_sor = np.abs(w_sor - w_exact(*np.meshgrid(x_nodes, t_nodes, indexing='ij')))
error_crout = np.abs(w_crout - w_exact(x_nodes, t_bounds[-1]))
error_cn = np.abs(w_cn - w_exact(x_nodes, t_bounds[-1]))

# print the results in a table
table = []
for i in range(m):
    table.append([x_nodes[i], w_sor[i, -1], w_crout[i], w_cn[i], w_exact(x_nodes[i], t_bounds[1]), error_sor[i, -1], error_crout[i], error_cn[i]])

print(tabulate.tabulate(table, headers=['x', 'Numerical Solution (SOR)', 'Numerical Solution (Crout)', 'Numerical Solution (CN)', 'Exact Solution', 'Error (SOR)', 'Error (Crout)', 'Error (CN)'], tablefmt='orgtbl', floatfmt=('.2f', '.8f', '.8f', '.8f', '.8f', '.4e', '.4e', '.4e')))