import numpy as np
import matplotlib.pyplot as plt
from calculo_numerico.exercicios_py.metodo_euler import euler
from tabulate import tabulate

# define the initial problem value (IVP)
def f(t, u):
    return np.sin(t)
u0, t0, tf = 1, 0, 10

# define exact solution (if there is one)
def u_exact(t):
    return -np.cos(t) + 2

#----------------------------------------------------
# print table and plot results
#----------------------------------------------------
h_vector = np.array([0.16, 0.08, 0.04, 0.02, 0.01])
rel_error = []
fig, (ax1, ax2) = plt.subplots(2, 1)
data = []

for h in h_vector:
    t, u = euler(f, u0, t0, tf, h)
    rel_error_max = np.max(np.fabs(u_exact(t) - u)/np.fabs(u_exact(t)))
    rel_error.append(rel_error_max)
    rel_error_tf = np.fabs(u_exact(t[-1]) - u[-1])/np.fabs(u_exact(t[-1]))
    data.append([h, u[-1], rel_error_tf])
    ax1.plot(t, u, label=f'$h={h}$')

print(tabulate(data, headers=['step size (h)', 'approximate solution u(10)', 'relative error'], tablefmt='orgtbl', floatfmt=('g', '.8f', '.8f')))

ax1.set_xlabel(r'$t$')
ax1.set_ylabel(r'$u(t)$')
ax1.plot(t, u_exact(t), label='Exact solution')

ax2.set_xlabel(r'$h$')
ax2.set_ylabel('Relative error')
ax2.set_yscale('log')
ax2.invert_xaxis()
ax2.loglog(h_vector, rel_error)
ax2.plot(h_vector, h_vector, label=r'O(h)')

plt.tight_layout()
ax1.legend()
ax2.legend()
plt.show()