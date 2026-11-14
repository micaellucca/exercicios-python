"""criar um programa para verificar se existe silva no nome de uma pessoa"""

nome = input("digite seu nome: ").lower().strip()
verificador_nome = nome.split()

print("lucca" in verificador_nome)