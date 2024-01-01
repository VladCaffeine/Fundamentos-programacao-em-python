while (True):
    selectedNumber = int(input("Qual numero você quer saber se é primo? "))

    # 
    #     Abaixo verificamos se dentro das divisões possíveis ao dividendo,
    #     ocorre alguma com resto 0. Caso não tenha, temos então a certeza
    #     que nosso número selecionado é um número primo. Terminando então o
    #     loop, e prosseguindo.
    #

    if (selectedNumber > 1):
        numberIsPrime = True
        i = 2 
        while (i < selectedNumber):
            restDivision = selectedNumber % i
            if (restDivision == 0):
                print("O número %d não é primo" %(selectedNumber))
                numberIsPrime = False
                break
            i += 1
        if (numberIsPrime):
            print("O número %d é primo" %(selectedNumber))
    else:
        print("O número precisa ser maior que 1")
    
