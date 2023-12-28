taxaJurosPoupanca = int(input("Qual a taxa de juros? "))

acumuladorPoupanca = int(input("Qual deposito inicial? "))
acumuladorPoupanca += (taxaJurosPoupanca * acumuladorPoupanca) / 100
print("No primeiro mês você terá %d" %(acumuladorPoupanca))

i = 1
while (i <= 23):
    depositoPoupanca = int(input("Quanto vai depositar? "))
    totalPoupanca = depositoPoupanca + acumuladorPoupanca

    jurosAplicado = ((taxaJurosPoupanca * totalPoupanca) / 100) + totalPoupanca
    acumuladorPoupanca += jurosAplicado
    print("No mês %d você terá %d" %(i, acumuladorPoupanca))
    i += 1
