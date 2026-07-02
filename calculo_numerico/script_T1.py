import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate
from exercicios_py.metodos_edo import euler, heun, rk4

#------------------------------------------
# define o problema de valor inicial
#------------------------------------------
def f(t, v):
    return 0.5 * (10 - v)
v0, t0, tf = 0, 0, 10

def exata_v(t):
    return 10 * (1 - np.exp(-0.5 * t))

#------------------------------------------------------
# imprime tabela com resultados e plota os gráficos
#------------------------------------------------------
h_vetor = np.array([1, 0.2, 0.05])
cores = ['red', 'green', 'blue']

# cria primeira figura com 3 subplots para comparar os metodos numericos
fig1, (ax1, ax2, ax3) = plt.subplots(1, 3, sharex=True, sharey=True)
fig1.supxlabel(r'$t$ (s)')
fig1.supylabel(r'$\tilde{V}(t)$ (V)')
ax1.set_title('Euler')
ax2.set_title('Heun')
ax3.set_title('RK4')
axs = [ax1, ax2, ax3]

# plota a solucao exata em todos os subplots da figura 1
t_plot = np.linspace(t0, tf, 100)
for ax in axs:
    ax.plot(t_plot, exata_v(t_plot), label='exata', color='black', linestyle='--')

# cria segunda figura para analisar o erro (em escala logaritmica) em funcao do passo h
fig2, ax4 = plt.subplots()
ax4.set_xlabel(r'$h$')
ax4.set_ylabel(r'$\vert V(t)-\tilde{V}(t) \vert$')
ax4.loglog() 
ax4.xaxis.set_inverted(True)

# plota curvas de referencia para O(h), O(h^2) e O(h^4) na figura 2
href = np.linspace(h_vetor.min(), h_vetor.max(), 100)
ax4.plot(href, href, label=r'O(h)', color='gray', linestyle='--')
ax4.plot(href, href**2, label=r'O($h^2$)', color='gray', linestyle=':')
ax4.plot(href, href**4, label=r'O($h^4$)', color='gray', linestyle='-.')

# cria lista para armazenar os erros maximos e os erros em tf de cada metodo numerico para imprimir na tabela de dados
dados = []
# cria listas para armazenar os erros maximos de cada metodo numerico para plotar na figura 2
erros_euler = []
erros_heun = []
erros_rk4 = []

for h, cor in zip(h_vetor, cores):
    t_euler, v_euler = euler(f, v0, t0, tf, h) # calcula solucao numerica com metodo de Euler
    t_heun, v_heun = heun(f, v0, t0, tf, h) # calcula solucao numerica com metodo de Heun
    t_rk4, v_rk4 = rk4(f, v0, t0, tf, h) # calcula solucao numerica com metodo de RK4
    
    ax1.plot(t_euler, v_euler, label=f'$h={h}$', color=cor)
    ax2.plot(t_heun, v_heun, label=f'$h={h}$', color=cor)
    ax3.plot(t_rk4, v_rk4, label=f'$h={h}$', color=cor)
    
    # funcao para calcular o erro maximo e o erro em tf de uma solucao numerica em relacao a solucao exata
    def calc_erros(t, v):
        erros = np.fabs(exata_v(t) - v)
        return np.max(erros), erros[-1]

    # calcula os erros maximo e em tf para cada metodo numerico e armazena os resultados na tabela de dados
    e_max, e_tf = calc_erros(t_euler, v_euler)
    erros_euler.append(e_max)
    dados.append(['Euler', h, e_max, e_tf])
    
    e_max, e_tf = calc_erros(t_heun, v_heun)
    erros_heun.append(e_max)
    dados.append(['Heun', h, e_max, e_tf])

    e_max, e_tf = calc_erros(t_rk4, v_rk4)
    erros_rk4.append(e_max)
    dados.append(['RK4', h, e_max, e_tf])

# plota os erros em tf de cada metodo numerico na figura 2
ax4.plot(h_vetor, erros_euler, '-o', color='red', label='Euler')
ax4.plot(h_vetor, erros_heun, '-s', color='green', label='Heun')
ax4.plot(h_vetor, erros_rk4, '-^', color='blue', label='RK4')

# configura legendas e grades para os graficos e imprime a tabela de dados
for ax in axs:
    ax.legend(fontsize='small')
    ax.grid(True, alpha=0.3)
ax4.legend(fontsize='small'); ax4.grid(True, alpha=0.3)

print(tabulate(dados, headers=['metodo', 'passo (h)', 'erro maximo', 'erro em T_max'], tablefmt='orgtbl', floatfmt=('g', 'g', '.15e', '.15e')))

plt.tight_layout()
fig1.savefig('calculo_numerico/comparacao_metodos.pdf', dpi=300, bbox_inches='tight')
fig2.savefig('calculo_numerico/analise_erro.pdf', dpi=300, bbox_inches='tight')
plt.show()