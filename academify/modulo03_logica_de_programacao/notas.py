note = []
note_quantity = int(input("quantas notas quer adicionar?: "))
new_note = 0
order = 1

for i in range(note_quantity):
    new_note = float(input(f"adicione a {order}º nota: "))
    note.append(new_note)
    order += 1

option = 0

while option != 7:
    print("\n")
    print("DESEJA REALIZAR MAIS ALGUMA OPERAÇÃO?")
    print("opção 0: ver maior e menor nota")
    print("opção 1: adicionar nota")
    print("opção 2: remover nota")
    print("opção 3: ordenar notas")
    print("opção 4: ver quantidade de notas")
    print("opção 5: calcular média")
    print("opção 6: checar notas")
    print("opção 7: sair do sistema")
    print("\n")
    option = int(input("ESCOLHA SUA OPÇÃO: "))

    match option:
        case 0:
            bigger_note = max(note)
            smaller_note = min(note)
            print(f"maior nota é: {bigger_note}")
            print(f"menor nota é: {smaller_note}")
        case 1:
            new_note = float(input("adicione nova nota: "))
            note.append(new_note)
            print(f"suas notas agora são: {note}")
        case 2:
            remove_note = int(input("escolha a posição da nota que quer remover: "))
            print(note)
            note.pop(remove_note - 1)
            print(note)
        case 3:
            note.sort()
            print("notas organizadas por ordem númerica")
            print(note)
        case 4:
            print("quantidade de notas: ", len(note))
        case 5:
            sum_note = sum(note)
            media_note = sum_note / len(note)
            print(f"a média das notas é: {media_note:.1f}")
        case 6:
            print(f"suas notas são: {note}")
        case 7:
            print("SISTEMA FINALIZADO")
        case _:
            print("insira um valor válido")
