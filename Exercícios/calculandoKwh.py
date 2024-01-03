
tipoResidência = input("Qual o seu tipo de residência? \n1)Residêcia \n2)Comercial \n3)Industrial\n")
consumoKwh = int(input("Quanto kWh você consumiu desde então? "))

if (tipoResidência == "1") and (consumoKwh <=  500):
    totalPagarConsumo = 0.40 * consumoKwh
    print("Você terá que pagar o valor de R$ %d" %(totalPagarConsumo))
elif (tipoResidência == "1") and (consumoKwh > 500):
    totalPagarConsumo = 0.65 * consumoKwh
    print("Você terá que pagar o valor de R$ %d" %(totalPagarConsumo))
elif (tipoResidência == "2") and (consumoKwh <= 1000):
    totalPagarConsumo = 0.55 * consumoKwh
    print("Você terá que pagar o valor de R$ %d" %(totalPagarConsumo))
elif (tipoResidência == "2") and (consumoKwh > 1000):
    totalPagarConsumo = 0.60 * consumoKwh
    print("Você terá que pagar o valor de R$ %d" %(totalPagarConsumo))
elif (tipoResidência == "3") and (consumoKwh <= 5000):
    totalPagarConsumo = 0.55 * consumoKwh
    print("Você terá que pagar o valor de R$ %d" %(totalPagarConsumo))
elif (tipoResidência == "3") and (consumoKwh > 5000):
    totalPagarConsumo = 0.60 * consumoKwh
    print("Você terá que pagar o valor de R$ %d" %(totalPagarConsumo))
else:
    print("Não foi possível calcular, tente novamente.")

