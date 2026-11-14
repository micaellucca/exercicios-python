"""
peça um numero e exiba a tabuada de 0 a 10
"""

number = int(input("escolha um numero: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number*i}")
