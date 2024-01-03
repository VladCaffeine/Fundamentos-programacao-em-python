valorDivida = float(input("Qual o valor da dívida? "))
jurosMensais = float(input("Qual o valor de juros mensais? "))
valorPagoMensal = float(input("Quanto está disposto a pagar mensalmente? \n"))

if (valorPagoMensal < (jurosMensais / 100 * valorDivida)):
    print("Erro, valor pago mensal menor que os juros")

periodoPago = 1
acumuloDivida = valorDivida

while (valorDivida > 0):
    valorDividaJuros = (jurosMensais / 100 * valorDivida) + valorDivida
    valorRestante = valorDividaJuros - valorPagoMensal
    valorDivida = valorRestante
    if (valorDivida > 0):
        print("Valor pago de %d, restando %d" %(valorPagoMensal, valorDivida))
    else:
        convertendoSaldoNegativo = abs(valorDivida) 
        print("Divida paga, você ficou com saldo de %d" %(convertendoSaldoNegativo))
    periodoPago += 1
    acumuloDivida += valorDivida


