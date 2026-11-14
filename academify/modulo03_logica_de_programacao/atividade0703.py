"""
digitar uma palavra e verificar
quantas vogais tem
"""

word = input("digite uma palavra: ").lower()
vogais = 0
letters = ["a", "e", "i", "o", "u"]

for letter in word:
    if letter in letters:
        vogais += 1

print(f"a palavra tem {vogais} vogais")
"""
(for letter in word) vai percorrer cada letra da palavra digitada, após 
percorrer, ele vai verificar se a letra está na variavel letters que 
foi criada, se estiver, o contador aumenta em +1
"""
