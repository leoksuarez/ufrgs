import numpy as np
from numpy import linalg
from numpy.polynomial.polynomial import polyval
import matplotlib.pyplot as plt

rng = np.random.default_rng()

n = 3
low_range = -9
high_range = 10
pontos = rng.integers(low=low_range, high=high_range, size=(n, 2)) # gera pontos (xi, yi) aleatorios num determinado range
xi = pontos[:, 0].astype(float)
yi = pontos[:, 1].astype(float)

potencias = np.arange(0, n, 1) # cria array com as potencias de x
A = np.array([xi**p for p in potencias]).transpose() # constroi a matriz com as potencias de x avaliadas em cada ponto (cada linha usa um dos pontos)
a = np.linalg.solve(A, yi) # resolve a equacao matricial para encontrar os coeficientes do polinomio interpolador

x = np.linspace(low_range-1, high_range+1)
y = polyval(x, a)

fig, ax = plt.subplots()
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

plt.plot(xi, yi, 'ro', label='Pontos')
plt.plot(x, y, 'b-', label='Polinômio interpolador')
plt.grid()
plt.legend()
plt.show()