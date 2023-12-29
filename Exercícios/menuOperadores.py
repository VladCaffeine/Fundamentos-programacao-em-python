while (True):
    operacao = int(input("Qual operador você deseja usar?\n 1)Adição\
            \n2)Subtração\n3)Multiplicação\n0 para sair\nEscolha: "))
    
    if (operacao == 0):
        break

    print("")

    produto = 1
    while (produto <= 10):
        print("")
        tabuada = 1
        while (tabuada <= 10):
            resultado = 0
            if (operacao == 1):
                resultado = produto + tabuada
                print("%d + %d = %d\n" %(produto, tabuada, resultado))
            elif (operacao == 2):
                resultado = produto - tabuada
                print("%d - %d = %d\n" %(produto, tabuada, resultado))
            elif (operacao == 3):
                resultado = produto * tabuada
                print("%d x %d = %d\n" %(produto, tabuada, resultado))

            tabuada += 1
        produto += 1
    
