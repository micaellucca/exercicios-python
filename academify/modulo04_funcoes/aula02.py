#*args permite passar quantos argumentos quiser
'''def soma(*numeros):
    total = sum(numeros)
    print(f"soma total é: {total}")

soma(1,2,3,4,5,6)'''

"""
crie uma função chamada resumo_pedido que receba 
    nome do cliente
    um ou mais itens
    e informações extras como forma_pagamento ou endereço(usando **kwargs)
"""

def resumo_pedido(nome, *itens, **informacoes_extras):
    print(f"Cliente: {nome}")
    print("Itens:")
    for item in itens:
        print(f"- {item}")
    
    if informacoes_extras:
        print("Informações extras:")
        for chave, valor in informacoes_extras.items():
            print(f"- {chave}: {valor}")


nome = input("Digite seu nome: ")
itens_texto = input("O que você deseja comprar (separado por vírgula): ")
lista_itens = itens_texto.split(",")   # transforma "pizza, suco" em ["pizza", " suco"]

forma_pagamento = input("Forma de pagamento: ")
endereco = input("Endereço: ")

resumo_pedido(nome, *lista_itens, forma_pagamento=forma_pagamento, endereco=endereco)