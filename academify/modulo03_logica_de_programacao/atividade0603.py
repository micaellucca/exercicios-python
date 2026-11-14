"""
Receba o preço de um produto e
aplique 10% de desconto
"""

print("o produto que deseja é uma TV")

price = int(input("quanto custa o produto: "))
discount = int(input("digite o desconto que deseja: "))

porcent = discount / 100

print(
    f"seu produto custa {price} , com o desconto de {discount}% ficara {(price * porcent)}"
)
