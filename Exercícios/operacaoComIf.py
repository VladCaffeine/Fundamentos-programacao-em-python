operador = input("Qual operador você quer usar? ")
produtoA = int(input("Qual o primeiro produto? "))
produtoB = int(input("Qual o segundo produto? "))

if (operador == "+") :
    resultado = produtoA + produtoB
    print("A soma é igual a %d" %(resultado))
elif (operador == "-"):
    resultado = produtoA + produtoB
    print("A subtração é igual a %d" %(resultado))
elif (operador == "*"):
    resultado = produtoA * produtoB
    print("A multiplicação é igual a %d" %(resultado))
else:
    print("Verifique o operador e tente novamente")
