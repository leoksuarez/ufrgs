# dados iniciais
historico_vendas = ("carlos", "ana", "carlos", "bruno", "ana", "diego")

# eliminar duplicados
clientes = set(historico_vendas)

# cria dicionario com nome do cliente e quantidade de compras (inicialmente 0)
dict_clientes = {cliente: 0 for cliente in clientes}
print(dict_clientes)

# exibe clientes com um numero de cadastro
cadastro = {cliente: i+1 for i, cliente in enumerate(dict_clientes.keys())}
print(cadastro)