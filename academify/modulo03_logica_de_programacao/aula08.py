# frutas = ["maça", "banana", "laranja"]

# pegar elemento especifico da lista
"""print(frutas[1])"""

# substituir elemento da lista
""" frutas[2] = "uva"""

# imprimir todos os elementos da lista
"""for lista in frutas:
    print(lista)"""


# EXERCICIO

"""
mostre todos os numeros
mostre quantos numeros tem
mostre se o numero 10 está na lista
"""

list = [1, 2, 3, 4, 5]

for numbers in list:
    print(numbers)

print("=" * 10)

print(len(list))

print("=" * 10)

verify_number = input("digite qual numero quer checar: ")
try:
    verify_number = float(verify_number)
    if verify_number in list:
        print(f"{verify_number} está na lista")
    else:
        print(f"{verify_number} não está na lista")
except:
    print("formato invalido, digite um numero")
