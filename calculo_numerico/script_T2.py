from metodos_numericos.bvp_pdes import wave
import numpy as np
import tabulate
import matplotlib.pyplot as plt

# define os tamanhos dos passos de espaço e tempo
h = 0.1
k = 0.12

x_bounds = np.array([0, 1])
t_bounds = np.array([0, 5])    

# define o numero de nos espaciais e temporais
m = int((x_bounds[1] - x_bounds[0]) / h)
N = int((t_bounds[1] - t_bounds[0]) / k)

x_nodes = np.linspace(x_bounds[0], x_bounds[1], m + 1)
t_nodes = np.linspace(t_bounds[0], t_bounds[1], N + 1)

# define as condicoes de contorno e iniciais
boundary = {
    'left': np.zeros(N + 1),
    'right': np.zeros(N + 1)
}

initial = {
    'u0': lambda x: np.sin(np.pi * x),
    'u1': lambda x: np.zeros_like(x)
}

alpha = 1.0
lmbda = alpha * k / h
print(f"lambda = {lmbda:.4f}")

# computa a solucao exata
w_exact = lambda x, t: np.sin(np.pi * x) * np.cos(np.pi * t)

# computa a solucao numerica
w = wave(m, N, x_bounds, t_bounds, alpha, boundary, initial)

# computa o erro absoluto entre a solucao numerica e a solucao exata
error = np.abs(w - w_exact(*np.meshgrid(x_nodes, t_nodes, indexing='ij')))

# imprime a tabela de resultados
table = []
for i in range(m):
    table.append([x_nodes[i], w[i, -1], w_exact(x_nodes[i], t_bounds[-1]), error[i, -1]])
print(tabulate.tabulate(table, headers=['x', 'numérica', 'exata', 'erro'], tablefmt='orgtbl', floatfmt=('.2f', '.8f', '.8f', '.4e')))

# gera os graficos da evolucao temporal da solucao numerica e exata
time_steps = np.arange(t_bounds[0], t_bounds[1] + 0.1, 0.5)

for t in time_steps:
    # encontra o indice do passo de tempo mais proximo do tempo atual
    idx = np.abs(t_nodes - t).argmin()
    t_idx = t_nodes[idx]
    
    # cria a figura e o eixo
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.set_xlim(x_bounds[0], x_bounds[1])
    ax.set_ylim(-1.2, 1.2)
    
    # plota a solucao numerica e a solucao exata
    ax.plot(x_nodes, w[:, idx], 'b-', lw=2, label='numérica')
    ax.plot(x_nodes, w_exact(x_nodes, t_idx), 'r--', lw=1.5, label='exata')
    
    # adiciona titulo, legendas e grade
    ax.set_title(r'Evolução temporal ($\lambda = {:.2f}$): $t = {:.2f}$ s'.format(lmbda, t_idx), fontsize=12)
    ax.set_xlabel(r'$x$')
    ax.set_ylabel(r'$u(x,t)$')
    ax.legend(loc='upper right')
    ax.grid(True)
    
    # salva o grafico em arquivo
    name = f'wave_3_t_{t_idx:.2f}.png'
    plt.savefig(name, facecolor='white', transparent=False, bbox_inches='tight')
    print(f'plot saved as {name}')
    
    plt.close(fig) # fecha a figura para liberar memoria