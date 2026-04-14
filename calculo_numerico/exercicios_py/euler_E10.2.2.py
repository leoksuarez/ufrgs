import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate
from calculo_numerico.exercicios_py.metodo_euler import euler

#----------------------------------------------------
# define the initial problem value (IVP)
#----------------------------------------------------
def f(t, u):
    return -u/2 + 2 + t
u0, t0, tf = 8, 0, 1

def exact_u(t):
    return 2*t + 8*np.exp(-t/2)

#----------------------------------------------------
# print table with results and plot curves for different step sizes
#----------------------------------------------------
plt.figure(figsize=(10,6))
h_vector = np.zeros(5)
data = []

for k in range(0, 5, 1):
    h_vector[k] = 10**(-k-1)

for h in h_vector:
    t, u = euler(f, u0, t0, tf, h)
    plt.plot(t, u, label=f'$h={h}$')
    rel_error = np.fabs(exact_u(t)[-1] - u[-1])/np.fabs(exact_u(t)[-1])
    data.append([h, u[-1], rel_error])

print(tabulate(data, headers=['step size (h)', 'approx solution (u(tf))', 'rel_error'], tablefmt='orgtbl', floatfmt=('g', '.10f', '.10e')))

plt.xlabel(r'$t$', fontsize=12)
plt.ylabel(r'$u(t)$', fontsize=12)
plt.tight_layout()
plt.legend()
plt.show()