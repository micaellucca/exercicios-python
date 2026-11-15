#forma dificil
lista = []
quantidade = int(input("quantos numeros deseja adicionar: "))

for i in range(quantidade):
    numero = int(input(f"digite o {i+1}° numero: "))
    lista.append(numero)
    i += 1

print(f"maior numero é {max(lista)}")
print(f"menor numero é {min(lista)}")