import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (x-1)**3

def g(x):
    return (x-2)**2

x = np.linspace(0, 3)
plt.plot(x, f(x), label=r'$f(x) = (x-1)^3$')
plt.plot(x, g(x), label=r'$g(x) = (x-3)^2$')

plt.grid(); plt.show()