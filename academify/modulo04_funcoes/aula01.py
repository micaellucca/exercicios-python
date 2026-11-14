'''def saudacao():
    print("aprendendo funções")
    print("hello, word")

saudacao()'''


'''def saudacao(nome):
    print(f"seja bem vindo, {nome}")

saudacao("micael")
saudacao("cyssa")'''

#==========================
"""
crie uma função chamada imc, que vai receber peso e altura e retornar
o resultado do imc

IMC = peso / (altura * altura)

exibir resultado formatado com duas casas decimais
"""


def imc(peso, altura):
    indice = peso / (altura ** 2 )   
    return indice

peso = float(input("digite seu peso: "))
altura = float(input("digite sua altura: "))
valor_imc = imc(peso, altura)

print(f"seu IMC é {valor_imc:.2f}")