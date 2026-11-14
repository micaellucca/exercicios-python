numero = int(input("digite seu numero: "))

unidade = numero % 10
dezena = numero // 10
centena = numero // 100
milhar = numero // 1000

print(f"unidade: {unidade}")
print(f"dezena: {dezena % 10}")
print(f"centena: {centena % 10}")
print(f"milhar: {milhar}")