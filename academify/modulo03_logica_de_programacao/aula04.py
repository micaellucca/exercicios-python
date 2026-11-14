# try/except
number = input("digite o número para multiplicar por 2: ")

try:
    number = float(number)
    print(f"o valor de {number} multiplicado por 2 é {number * 2.0:.1f} ")
except:
    print("isso não é um número")
