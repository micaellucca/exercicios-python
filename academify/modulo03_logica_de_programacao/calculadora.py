number_1 = float(input("primeiro número: "))
number_2 = float(input("segundo número: "))

print(
    "operações para escolher:\n"
    "adição( digite 1 )\n"
    "subtração ( digite 2 )\n"
    "multiplicação ( digite 3 )\n"
    "divisão ( digite 4 )\n"
)

operation = input(f"digite a operação da conta {number_1} _ {number_2}: ")

if operation == "1":
    resultado = number_1 + number_2
    print(f"o resultado de {number_1} + {number_2} é: {resultado:.2f}")
elif operation == "2":
    resultado = number_1 - number_2
    print(f"o resultado de {number_1} - {number_2} é: {resultado:.2f}")
elif operation == "3":
    resultado = number_1 * number_2
    print(f"o resultado de {number_1} * {number_2} é: {resultado:.2f}")
elif operation == "4":
    resultado = number_1 / number_2
    print(f"o resultado de {number_1} / {number_2} é: {resultado:.2f}")
else:
    print("digite uma operação válida")
