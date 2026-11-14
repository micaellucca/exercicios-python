"""
tuplas são listas que não podem ser modificadas, depois de criado, seus
elementos não podem ser alterados
"""

meses = (
    "Janeiro",
    "Fevereiro",
    "Março",
    "Abril",
    "Maio",
    "Junho",
    "Julho",
    "Agosto",
    "Setembro",
    "Outubro",
    "Novembro",
    "Dezembro",
)

print(f"primeiro mês: {meses[0]}")
print(f"ultimo mês: {meses[-1]}")
print(f"quantidade de meses: {len(meses)}")
for mes in meses:
    print(mes)
