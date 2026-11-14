"""
fazer algum produto receber 10%
de desconto
"""

porcentagem = 0.1
produto = int(input("digite o preço do produto que quer cadastrar: "))
desconto = produto * porcentagem
print(f"seu produto com desconto é: {produto - desconto}")
