"""
peça numeros e exiba
a soma entre eles
"""

list = []
quantity = int(input("quantos numeros voce quer adicionar: "))
for i in range(quantity):
    i += 1
    numbers = float(input(f"digite o {i}º número: "))
    list.append(numbers)
print(f"a soma dos numeros é {sum(list)}")
