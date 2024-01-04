depositoPoupanca = int(input("Qual foi o valor de depósito? "))
taxaJurosPoupanca = int(input("Qual a taxa de juros da poupança? "))
 
acumuloPoupanca = 0
i = 1
while (i <= 24):
    acumuloPoupanca += ((taxaJurosPoupanca * depositoPoupanca) / 100) + depositoPoupanca
    print("No mês %d teria %d" %(i, acumuloPoupanca))
    i += 1


