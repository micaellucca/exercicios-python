"""
peça um número e diga se ele é
impar ou par
"""

number = int(input("digite qualquer número inteiro: "))
if (number % 2) != 0:
    print(f"o número {number} é impar")
else:
    print(f"o número {number} é par")
