distance = float(input("digite a distancia percorrida: ").replace(",", "."))
distance = int(distance)

dist_longa = distance * 0.45
dist_curta = distance * 0.50

if distance <= 0:
    print("a distancia precisa ser maior que 0")
elif distance > 200:
    print(f"a distancia sairá por {dist_longa:.2f}R$")
else:
    print(f"a distancia sairá por {dist_curta:.2f}R$")