import random

numero = random.randint(0,5)

print("=" * 50)
print("eu pensei em um número...")
print("=" * 50)
print("\n")

try:
    palpite = int(input("qual número eu pensei? "))

    if 0 <= palpite <= 5:
        if palpite != numero:
            print("voce errou!!!")
        else:
            print("você acertou!!!")
    else:
        print("digite um numero entre 0 e 5")

except ValueError:
    print("digite um numero!!!")