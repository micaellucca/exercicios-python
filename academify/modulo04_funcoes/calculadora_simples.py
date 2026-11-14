soma = lambda a, b: a + b
subtracao = lambda a, b: a - b
multiplicacao = lambda a, b: a * b
divisao = lambda a, b: a / b


def escolha():
    while True:
        try:
            a = int(input("Digite o primeiro número: "))
            b = int(input("Digite o segundo número: "))
            break

        except ValueError:
            print("Erro! Digite apenas números inteiros.\n")

    print("\nEscolha uma operação:")
    print("[ + ] Soma")
    print("[ - ] Subtração")
    print("[ * ] Multiplicação")
    print("[ / ] Divisão")

    opcao = input("Escolha a operação: ").strip()

    match opcao:
        case "+":
            print(f"A soma de {a} + {b} é: {soma(a, b)}")

        case "-":
            print(f"A subtração de {a} - {b} é: {subtracao(a, b)}")

        case "*":
            print(f"A multiplicação de {a} * {b} é: {multiplicacao(a, b)}")

        case "/":
            if b == 0:
                print("Erro! Não é possível dividir por zero.")
            else:
                print(f"A divisão de {a} / {b} é: {divisao(a, b)}")

        case _:
            print("Operação inválida!")


escolha()