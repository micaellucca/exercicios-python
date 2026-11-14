"""
isso sao dicionarios, eles servem para organizar itens. igual as listas
a unica diferença é que eles auxiliam na busca por {chaves}, diferente
das listas onde a busca é realizada por numeros
"""

"""movie = {}

movie["titulo"] = input("digite o titulo do filme: ")
movie["genero"] = input("digite o genero do filme: ")
movie["ano"] = input("digite o ano do filme: ")
movie["nota"] = input("digite a nota do filme: ")

for mov in movie:
    if mov != "nota":
        print(f"o {mov} do filme é {movie[mov]}")
    else:
        print(f"a {mov} do filme é {movie[mov]}")"""


"""
MÉTODOS
"""

pessoa = {}
pessoa["nome"] = "micael"
pessoa["idade"] = 22
pessoa["altura"] = 1.83
pessoa["saude"] = True

# imprimir somente as chaves
print(pessoa.keys())

# imprimir somente os valores
print(pessoa.values())

# imprimir tanto os valores como as chaves
print(pessoa.items())

# pegar algo isolado
print(pessoa.get("nome"))

# mostrar mensagem para algo não encontrado
print(pessoa.get("cidade", "cidade não informada"))

# alterar informações
pessoa.update({"nome": "lucca"})
print(pessoa["nome"])  # serve para pegar algo isolado também

pessoa.pop("saude")
print(pessoa)

"""
pessoa.clear() para limpar todo o dicionario
"""
