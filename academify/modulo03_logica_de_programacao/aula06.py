result = 0
value = 0

print(f"{"="*5} TABUADA {"="*5}")
number = int(input("DIGITE O NÚMERO: "))

for i in range(1, 10 + 1):
    value += 1
    result = number * value
    print(f"o valor de {number} x {value} = {result}")
