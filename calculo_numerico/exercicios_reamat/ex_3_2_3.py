import numpy as np
import matplotlib.pyplot as plt
from metodo_bissecao import bisection

def f(x):
    return -4 + 8*x - 5*x**2 + x**3

p, i = bisection(f, 1/2, 3, 1e-3, 20)
print(f'p = {p}, i = {i}')

x = np.linspace(0, 3)
plt.plot(x, f(x))
plt.grid(); plt.show()