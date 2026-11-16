nome = input("digite seu nome: ").strip().lower()
letra_a = nome.count("a")
primeiro_a = nome.find("a")
ultimo_a = nome.rfind("a")

print(f"quantidade de A que aparece: {letra_a}")
if letra_a:
    print(f"posição do primeiro A está em: {primeiro_a + 1}")
    print(f"posição do último A está em: {ultimo_a + 1}")
else:
    print("A letra A não aparece no nome.")