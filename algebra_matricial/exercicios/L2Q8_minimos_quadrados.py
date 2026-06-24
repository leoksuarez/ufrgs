# %%
import sympy as sp
from sympy import Matrix, sin, pi, integrate, symbols
from IPython.display import display

sp.init_printing(use_latex='mathjax')
x = symbols('x')
# 1. Criar a Matriz de Hilbert 4x4
H = Matrix(4, 4, lambda i, j: integrate(x**(i+j), (x, 0, 1)))

# 2. Criar o vetor b (integrais de sin(pi*x) * x^j)
b = Matrix(4, 1, lambda j, i: integrate(sin(pi*x) * x**j, (x, 0, 1)))

# 3. Matriz Completa [H|b]
Ab = H.row_join(b)

# 4. Reduzir à forma escalonada (rref retorna a forma reduzida, 
# mas você pode ver os passos da eliminação)
Ab_triangular, pivots = Ab.rref()

print("Matriz completa [H|b] exata:")
display(Ab)
print("\nSolução dos coeficientes alpha:")
display(Ab_triangular[:, -1])
# %%
