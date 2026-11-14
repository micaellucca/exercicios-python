name = input("Digite seu nome: ").strip()
age = input("Digite sua idade: ").strip()

if not name or not age:
    print("ambos os campos precisam ser preenchidos.")
else:
    age = int(age)

    # imprimir o nome
    print(f"Seu nome é {name}")

    # escrever o nome ao inverso
    print(f"Seu nome invertido é {name[::-1]}")

    # verificar se o nome contém espaços
    if " " in name:
        print("Seu nome contém espaços")
    else:
        print("Seu nome não contém espaços")

    # ver quantas letras tem no nome
    print(f"Seu nome tem {len(name)} letras")

    # verificar a primeira letra do nome
    print(f"A primeira letra do seu nome é = {name.upper()[0]}")

    # verificar a última letra do nome
    print(f"A última letra do seu nome é = {name.upper()[-1]}")
