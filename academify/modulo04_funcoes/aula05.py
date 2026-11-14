'''
pseudocódigo:
    criar lista
    perguntar quantos numeros serão adicionados
    repetir a lista na quantidade n escolhida
    perguntar se vai querer adicionar algum numero
    somar todos os elementos da lista
'''

soma_lista = []
i = 0
resposta = "0"

def coleta(lista, i):
    n = int(input("quantos numeros você deseja adicionar: "))

    for _ in range(n):
        numero = int(input(f"digite o {i+1}° número de sua lista: "))
        lista.append(numero)
        i += 1

    print("deseja adicionar mais algum número: ")
    print("[0] -> sim")
    print("[1] -> não")
    resposta = input("digite sua resposta: ")

    if resposta == "0":
        return coleta(lista, i)
    return lista

soma_lista = coleta([], 0)
print(sum(soma_lista))
