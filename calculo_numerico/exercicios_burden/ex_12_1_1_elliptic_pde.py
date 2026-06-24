import sys
import os
import numpy as np
from tabulate import tabulate

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'metodos_numericos')))
from pvc_edps import poissonsor

x_bounds = np.array([0, 1])
y_bounds = np.array([0, 2])

h = 1/2
k = 1/2

n = int((x_bounds[1] - x_bounds[0]) / h)
m = int((y_bounds[1] - y_bounds[0]) / k)

x_nodes = np.linspace(x_bounds[0], x_bounds[1], n + 1)
y_nodes = np.linspace(y_bounds[0], y_bounds[1], m + 1)

f = lambda x, y: 4

boundary = {'left': y_nodes**2, 'right': 2 * (y_nodes - 1)**2, 'top': (x_nodes - 2)**2, 'bottom': x_nodes**2}

u_exact = lambda x, y: (x - y)**2
solution = poissonsor(n, m, x_bounds, y_bounds, f, boundary, omega=1.04)
error = np.abs(solution - u_exact(*np.meshgrid(x_nodes, y_nodes, indexing='ij')))

# print the results in a table
table = []
for i in range(n + 1):
    for j in range(m + 1):
        table.append([x_nodes[i], y_nodes[j], solution[i, j], u_exact(x_nodes[i], y_nodes[j]), error[i, j]])
print(tabulate(table, headers=['x', 'y', 'Numerical Solution', 'Exact Solution', 'Absolute Error'], tablefmt='orgtbl', floatfmt=('.2f', '.2f', '.6f', '.6f', '.2e')))