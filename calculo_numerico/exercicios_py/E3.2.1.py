import numpy as np
import matplotlib.pyplot as plt

def bisection_iteration(f, a, b, n):
    i = 0
    while i <= n:
        p = (b+a) / 2
        if np.sign(f(a)) * np.sign(f(p)) < 0:
            b = p
        else:
            a = p
        i += 1
    return p

f = lambda x: np.cos(x) - np.sqrt(x)
n = 5
p = bisection_iteration(f, 0, 1, n)

print(f'x^({n}) = {p}')

def f(x):
    return np.cos(x) - np.sqrt(x)

x = np.linspace(0, 1)
plt.plot(x, f(x))
plt.ylabel(r'$f(x) = \cos(x)-\sqrt{x}$')
plt.xlabel(r'$x$')

plt.grid(); plt.show()