# dict é uma coleção de objetos em que cada elemento está associado a uma chave única.
# podemos usar qualquer dado imutável como chave, como strings, números ou tuplas.
# os valores podem ser de qualquer tipo, incluindo outros dicionários.

# criando um dicionário
pessoa1 = {
    "nome": "paulo",
    "idade": 65,
    "cidade": "porto alegre"
}
print(pessoa1)  # saída: {'nome': 'paulo', 'idade': 65, 'cidade': 'porto alegre'}

# acessando valores
print(pessoa1["nome"])  # saída: paulo
print(pessoa1.get("idade"))  # saída: 65
print(pessoa1.get("pais", "brasil"))  # saída: brasil (valor padrão)
print(pessoa1.get("pais"))  # saída: None (chave não existe)
print(pessoa1)  # saída: {'nome': 'paulo', 'idade': 65, 'cidade': 'porto alegre'}

# adicionando ou atualizando valores
pessoa1["profissao"] = "matematico"  # adiciona nova chave-valor
pessoa1["idade"] = 66  # atualiza valor existente
print(pessoa1)  # saída: {'nome': 'paulo', 'idade': 66, 'cidade': 'porto alegre', 'profissao': 'matematico'}

# removendo valores
del pessoa1["cidade"]  # remove chave-valor
idade_removida = pessoa1.pop("idade")  # remove e retorna o valor
print(idade_removida)  # saída: 66
print(pessoa1)  # saída: {'nome': 'paulo', 'profissao': 'matematico'}

# iterando sobre um dicionário
for chave, valor in pessoa1.items():
    print(f"{chave}: {valor}")
# saída:
# nome: paulo
# profissao: matematico
for chave in pessoa1.keys():
    print(chave)
# saída:
# nome
# profissao

for valor in pessoa1.values():
    print(valor)
# saída:
# paulo
# matematico

# verificando se uma chave existe
if "nome" in pessoa1:
    print("A chave 'nome' existe no dicionário.")
# saída: A chave 'nome' existe no dicionário.
if "idade" not in pessoa1:
    print("A chave 'idade' não existe no dicionário.")
# saída: A chave 'idade' não existe no dicionário.

# limpando o dicionário
pessoa1.clear()
print(pessoa1)  # saída: {}

# dicionários aninhados
pessoa2 = {
    "nome": "josue",
    "idade": 33,
    "endereco": {
        "rua": "av. bento goncalves",
        "numero": 6000,
        "cidade": "porto alegre"
    }
}
print(pessoa2["endereco"]["cidade"])  # saída: porto alegre

# método para atualizar dicionários
pessoa2.update({"idade": 34, "profissao": "engenheiro de software"})
print(pessoa2) # saída: {'nome': 'josue', 'idade': 34, 'endereco': {'rua': 'av. bento goncalves', 'numero': 6000, 'cidade': 'porto alegre'}, 'profissao': 'engenheiro de software'}

# criando dicionário a partir de listas de tuplas
chaves = ["nome", "idade", "cidade"]
valores = ["ana", 28, "são paulo"]
pessoa3 = dict(zip(chaves, valores)) # zip combina as listas em tuplas
print(pessoa3)  # saída: {'nome': 'ana', 'idade': 28, 'cidade': 'são paulo'}

