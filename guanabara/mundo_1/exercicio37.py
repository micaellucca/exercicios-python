a = float(input("digite a medida do lado A(esquerda): ").replace(",",'.'))
b = float(input("digite a medida do lado B(direita): ").replace(",",'.'))
c = float(input("digite a medida do lado c(base): ").replace(",",'.'))

if a+b>c and a+c>b and b+c>a:
    print("pode formar um triangulo")
else:
    print("não pode formar um triangulo")