import sys
import os
import numpy as np
import tabulate
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'metodos_numericos')))
from bvp_pdes import poisson_sor

# define step sizes and bounds
h = np.pi/5
k = np.pi/10

x_bounds = np.array([0, np.pi])
y_bounds = np.array([0, np.pi/2])

# define number of grid points
n = int((x_bounds[1] - x_bounds[0]) / h) + 1
m = int((y_bounds[1] - y_bounds[0]) / k) + 1

x_nodes = np.linspace(x_bounds[0], x_bounds[1], n)
y_nodes = np.linspace(y_bounds[0], y_bounds[1], m)

# define boundary conditions and source term
boundary = {
    'left': np.cos(y_nodes),
    'right': -np.cos(y_nodes),
    'bottom': np.cos(x_nodes),
    'top': np.zeros(n)
}

f = lambda x, y: - (np.cos(x + y) * np.cos(x - y))

# compute the numerical solution
w = poisson_sor(n, m, x_bounds, y_bounds, f, boundary)

# compute the exact solution and error
w_exact = lambda x, y: np.cos(x) * np.cos(y)
error = np.abs(w - w_exact(*np.meshgrid(x_nodes, y_nodes, indexing='ij')))

# use optimal omega for Poisson equation
opt_omega = 4 / (2 + np.sqrt(4 - (np.cos(np.pi/n) + np.cos(np.pi/m))**2))
w_opt = poisson_sor(n, m, x_bounds, y_bounds, f, boundary, omega=opt_omega)
error_opt = np.abs(w_opt - w_exact(*np.meshgrid(x_nodes, y_nodes, indexing='ij')))


# print the results in a table
table = []
for i in range(n):
    for j in range(m):
        table.append([x_nodes[i], y_nodes[j], w[i, j], w_opt[i, j], w_exact(x_nodes[i], y_nodes[j]), error[i, j], error_opt[i, j]])

print(tabulate.tabulate(table, headers=['x', 'y', 'SOR Solution', 'SOR Opt Solution', 'Exact Solution', 'SOR Error', 'SOR Opt Error'], tablefmt='orgtbl', floatfmt=('.2f', '.2f', '.6f', '.6f', '.6f', '.2e', '.2e')))