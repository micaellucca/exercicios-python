fruits = ["banana", "uva", "maça"]

# acrescentar na ultima posição
fruits.append("laranja")
print(fruits)

# acrescentar em posição especifica
fruits.insert(1, "laranja")
print(fruits)

# remover algum item
fruits.remove("uva")
print(fruits)

# remover frutas por posição
fruits.pop(0)
print(fruits)

"""
fruits.clear()
--- apagar toda a lista
"""

# saber posição de determinada fruta
print(fruits.index("maça"))

# saber quantas vezes um item aparece
print(fruits.count("laranja"))

# ordenar lista em ordem
fruits.sort()  # para ordem reversa, so adicionar reverse = True
print(fruits)

# copiar lista
fruits_2 = fruits.copy()
fruits_2.append("limão")
print(fruits_2)
"""
o motivo de não poder fazer fruits_2 = fruits é pq eles iriam ocupar o mesmo lugar
na memoria, então a modificação de um iria modificar no outro também
"""
