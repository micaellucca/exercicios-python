import random

quantidade = int(input("quantos alunos deseja adicionar: "))
alunos = []

for i in range(quantidade):
    alunos_nome = input(f"digite o nome do {i+1}° aluno: ")
    alunos.append(alunos_nome)

random.shuffle(alunos)
print(alunos)