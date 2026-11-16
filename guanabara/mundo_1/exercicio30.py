vel_min = 0
vel_max = 80


try:
    velocidade = int(input("digite sua velocidade: "))

    if velocidade >= vel_min:
        if velocidade <= vel_max:
            print("você estava na velocidade correta!!!")
        else:
            multa = (velocidade - vel_max)*2

            print(f"voce foi multado, terá que pagar {multa:.2f}")
    else:
        print("velocidade precisa ser maior que 0")

except ValueError:
    print("velocidade precisa ser um número")