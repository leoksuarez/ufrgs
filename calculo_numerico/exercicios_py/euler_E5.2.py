import numpy as np
import matplotlib.pyplot as plt
from calculo_numerico.exercicios_py.metodo_euler import euler

# define IVP
def f(t, u):
    return (t**2) / (1 - u**2)
u0, t0, tf = 0, 0, 20

#----------------------------------------------------
# plot results
#----------------------------------------------------
h_vector = np.array([0.5, 0.25, 0.125, 0.0675])
fig = plt.figure(figsize=(10,6))

for h in h_vector:
    t, u = euler(f, u0, t0, tf, h)
    plt.plot(t, u, label=f'$h={h}$')


plt.xlabel(r'$t$')
plt.ylabel(r'$u(t)$')

plt.tight_layout()
plt.legend()
plt.show()