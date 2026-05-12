import numpy as np 
import matplotlib.pyplot as plt
from metodo_bissecao import bisection

def f(x):
    return 5 * np.sin(x**2) - np.exp(x/10)

x = np.linspace(0, 4)

tol = 1e-5
nmax = 20

p1, i1 = bisection(f, 0.4, 0.5, tol, nmax)
p2, i2 = bisection(f, 1.65, 1.75, tol, nmax)
p3, i3 = bisection(f, 2.5, 2.6, tol, nmax)

print(f'p1 = {p1}, i1 = {i1}\np2 = {p2}, i2 = {i2}\np3 = {p3}, i3 = {i3}')

plt.plot(x, f(x), color='r')
plt.grid(); plt.show()