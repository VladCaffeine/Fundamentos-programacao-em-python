valorCasa = int(input("Qual o valor da casa a ser comprada? "))
tempoPagar = int(input("Por quantos anos você quer pagar a casa? "))
salarioCliente = int(input("Qual o seu salario mensal? "))

## Tirando 30 % do salário do cliente para saber se aprovo ou não as parcelas
porcentagem30SalarioCliente = (30 * salarioCliente) / 100

parcelas = valorCasa / tempoPagar

if (parcelas < porcentagem30SalarioCliente):
    print("Parabéns seu empréstimo foi aprovado em parcelas de %d" %(parcelas))
elif (parcelas > porcentagem30SalarioCliente):
    print("As parcelas ultrapssam 30% do seu salário")
else:
    print("Não foi possível, verifique os valores")




