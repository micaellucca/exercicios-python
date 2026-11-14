# métodos de interpolação de strings

name = "micael"
idade = 20

# f-strings
print(f"meu nome é {name} e eu tenho {idade} anos")

# método antigo - %
print("meu nome é %s e eu tenho %d anos" % (name, idade))

# .format()
print("meu nome é {} e eu tenho {} anos".format(name, idade))

# concatenação
print("meu nome é " + name + " e eu tenho " + str(idade) + " anos")
