dividendo = int(input("Qual o dividendo? "))
divisor = int(input("Qual o divisor? "))

quociente = 0
subtraindo = dividendo
while (subtraindo > 1 ):
    subtraindo -= divisor
    quociente += 1

print(subtraindo)
print(quociente)

