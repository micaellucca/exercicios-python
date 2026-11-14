saldo = 100

def depositar(valor):
    global saldo
    saldo = saldo + valor
    return saldo

valor_deposito = int(input("Digite o valor do deposito: "))
depositar(valor_deposito)
print(saldo)