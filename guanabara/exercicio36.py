salario = float(input("digite seu salario: ").replace(",","."))

if salario <= 0:
    print("salário precisa ser maior que 0")
elif salario > 1250:
    aumento = salario * 0.1
    salario = (salario + aumento)
    print(f"seu novo salário é {salario:.2f}")
else:
    aumento = salario * 0.15
    salario = (salario + aumento)
    print(f"seu novo salário é {salario:.2f}")