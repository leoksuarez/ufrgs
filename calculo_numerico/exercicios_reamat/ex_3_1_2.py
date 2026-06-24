import numpy as np 
import matplotlib.pyplot as plt

def f_1(x):
    return np.cos(x)

def f_2(x):
    return x

xx = np.linspace(0, np.pi/2) # creates [0, pi/2] domain

# we search for the zeros of f(x) = cos(x) - x over [0, pi/2]
plt.plot(xx, f_1(xx) - f_2(xx), label=r'$f(x) = \cos(x) - x$') # plot f(x) = cos(x) - x

def fp(x):
    return -np.sin(x) - 1

# verify if f' is monotone over the interval [0, pi/2]. if it is, then there is a unique solution to cos(x) - x = 0 on [0, pi/2]
plt.plot(xx, fp(xx), label=r"$f'(x) = -\sin(x) - 1$") # plot f'(x) = -sin(x) - 1
plt.grid(); plt.legend(); plt.show()