try:
    numero = int(input("digite seu numero: "))

    if numero == 0:
        print("digite algum numero diferente de 0")
    elif numero % 2 == 0:
        print(f"o numero {numero} é par")
    else:
        print(f"o numero {numero} é impar")
except ValueError:
    print("VOCE PRECISA DIGITAR UM NUMERO INTEIRO")