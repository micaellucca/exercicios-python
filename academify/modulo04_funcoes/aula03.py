'''def conta(numero):
    return numero * 2

number = int(input("digite o número que sera multiplicado por 2: "))
resultado = conta(number)
print(resultado)'''

'''def media_escolar(*valores):
    total = len(valores)
    media = sum(valores) / total
    maior = max(valores)
    menor = min(valores)
    return media, maior, menor

media, maior, menor = media_escolar(10, 8, 3, 9)
print(f"media {media}, maior {maior}, menor {menor}")'''

#------------------------------------------------------------------------------------------------

#versão errada do exercicio
'''def estatistica(*numeros):
    total = sum(numeros)
    media = total/len(numeros)
    maior = max(numeros)
    menor = min(numeros)
    return media, maior, menor

contador = 1

resposta = 0
while resposta == "s":
    quantidade = int(input("quantas notas deseja adicionar: "))
    for i in range(quantidade):
        nota = float(input(f"adicione a {contador}º nota: "))
        estatistica(nota)
        contador += 1
    resposta = input("deseja adicionar outra nota")'''

#versão correta
def estatistica(*numeros):
    total = sum(numeros)
    media = total/len(numeros)
    maior = max(numeros)
    menor = min(numeros)
    return media, maior, menor


resposta = "s"
while resposta == "s":

    # Validação da quantidade de notas
    while True:
        try:
            quantidade = int(input("quantas notas deseja adicionar: "))
            break
        except ValueError:
            print("Erro: digite um número inteiro válido.")

    notas = [] #lista criada para adicionar as notas
    for i in range(quantidade):
        # Validação de cada nota (aceita ponto ou vírgula)
        while True:
            entrada = input(f"adicione a {i + 1}º nota: ") #recebe qualquer tipo de dado
            entrada = entrada.replace(",", ".")  # troca vírgula por ponto
            try:
                nota = float(entrada) #converte o dado recebido para float
                notas.append(nota) #adiciona na lista
                break
            except ValueError:
                print("Erro: digite um número válido (ex: 7.5 ou 7,5).")

    media, maior, menor = estatistica(*notas)
    print(f"média: {media}, maior: {maior}, menor: {menor}")

    resposta = input("deseja adicionar outra nota? (s/n): ").lower()