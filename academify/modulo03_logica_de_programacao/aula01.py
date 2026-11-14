enter = input("[E]ntrar / [S]air: ")
enter_password = int(input("Digite sua senha: "))

correct_password = 1234

if enter == "E" or enter == "e" and enter_password == correct_password:
    print("bem-vindo!")
else:
    print("tente novamente!")
