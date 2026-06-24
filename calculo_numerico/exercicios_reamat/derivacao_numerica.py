import sympy as sp 
import numpy as np
import matplotlib.pyplot as plt

x = sp.symbols('x')

f_sym = sp.sin(2*x) - x**2
df_sym = sp.diff(f_sym, x)

f = sp.lambdify(x, f_sym, 'numpy') # converte para funcao numerica (numpy)
df = sp.lambdify(x, df_sym, 'numpy')

# diferenca finita progressiva de ordem 1
def dp1(f, x0, h=0.1):
    return (f(x0+h)-f(x0))/h

# diferenca finita regressiva de ordem 1
def dr1(f, x0, h=0.1):
    return (f(x0)-f(x0-h))/h

# diferenca finita central de ordem 2
def dc2(f, x0, h=0.1):
    return (f(x0+h)-f(x0-h))/(2*h)

x0 = 2
h_vetor = np.logspace(-1, -9, 10)
erros_p = []
erros_r = []
erros_c = []

for h in h_vetor:
    erro_p = abs(dp1(f, x0, h) - df(x0))
    erro_r = abs(dr1(f, x0, h) - df(x0))
    erro_c = abs(dc2(f, x0, h) - df(x0))
    
    erros_p.append(erro_p)
    erros_r.append(erro_r)
    erros_c.append(erro_c)

erros_p = np.array(erros_p)
erros_r = np.array(erros_r)
erros_c = np.array(erros_c)

plt.figure(figsize=(10,6))
plt.loglog(h_vetor, erros_p, 'o-', label='Progressiva')
plt.loglog(h_vetor, erros_r, 's-', label='Regressiva')
plt.loglog(h_vetor, erros_c, '+-', label='Central')

plt.xlabel(r'$h$', fontsize=12)
plt.ylabel('Erro absoluto', fontsize=12)

plt.tight_layout()
plt.legend()
plt.show()
