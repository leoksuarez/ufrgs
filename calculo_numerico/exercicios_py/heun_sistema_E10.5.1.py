import numpy as np
from tabulate import tabulate
from heun_sistema import euler_melhorado_sistema

def f(t, u):
    x, y = u
    dx = -2*x + np.sqrt(y)
    dy = x - y
    return np.array([dx, dy])

u0 = np.array([0, 2])
h_vector = np.array([2*10**-1, 2*10**-2, 2*10**-3, 2*10**-4])
data = []

for h in h_vector:
    t, u = euler_melhorado_sistema(f, u0, 0, 2, h)
    data.append([h, u[-1, 0], u[-1, 1]])

print(tabulate(data, headers=['step size (h)', 'approximate x(tf)', 'approximate y(tf)'], tablefmt='orgtbl', floatfmt=('.1e', '.10f', '.10f')))