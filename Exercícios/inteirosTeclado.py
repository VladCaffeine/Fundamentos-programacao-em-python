
acumuloNumerosInteiros = 0
contadorLoop = 0
while True:
    numerosInteiros = int(input("Digite um número inteiro(0 para interromper): "))
    if (numerosInteiros == 0):
        break
    acumuloNumerosInteiros += numerosInteiros
    print(acumuloNumerosInteiros)
    contadorLoop += 1

mediaNumerosInteiros = acumuloNumerosInteiros / contadorLoop
print("A média dos números digitados é igual a %d" %(mediaNumerosInteiros))

