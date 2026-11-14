"""
receba 3 notas e calcule a media aritmetica
"""

note_list = []
print("ADICIONE AS 3 NOTAS ABAIXO")
print("-" * 15)

for i in range(3):
    i += 1
    note = float(input(f"adicione a {i}º nota: "))
    note_list.append(note)

print(f"a sua média final é: {(sum(note_list) / 3):.1f}")
