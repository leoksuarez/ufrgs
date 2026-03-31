import sympy as sp 
import numpy as np
import matplotlib.pyplot as plt

# define e calcula a derivada da funcao simbolicamente
x = sp.symbols('x')
f_sym = x/2 + x**2 * sp.sin(1/x)
df_sym = sp.diff(f_sym, x)

f = sp.lambdify(x, f_sym, 'numpy') # converte funcao do sympy para numpy
df = sp.lambdify(x, df_sym, 'numpy')
x = np.linspace(-.5,.5,2000) 
x = x[x!=0] # aplica o operador != em cada elemento do np.array e mantem apenas os elementos nas posicoes True (exclui o zero)

plt.figure(figsize=(10,6))
plt.plot(x, df(x), label=r"$f'(x) = \frac{1}{2} + 2x \sin(\frac{1}{x}) - \cos(\frac{1}{x})$", color='blue')

# plota o ponto f'(0) = 0.5
plt.scatter([0], [0.5], color='red', zorder=5, label=r"$f'(0) = 0.5$")
plt.axhline(0.5, color='red', linestyle='--', alpha=0.3)

# formatacao do grafico
plt.xlabel("x")
plt.ylabel("f'(x)")
plt.legend()
plt.grid(True)
plt.savefig('contraexemplo_crescimento_local.pdf')
plt.show()