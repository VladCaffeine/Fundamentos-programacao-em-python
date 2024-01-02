while (True):
    dividend = int(input("Quanto você quer dividir? "))
    divider = int(input("Para quantos? "))

    rest = dividend 
    quotient = 0
    while (True):
        rest = rest - divider

        if (rest < divider):
            break

        quotient += 1

    print("Resto igual a %d" %(rest))
    print("%d divido por %d é igual a %d" %(dividend, divider, quotient))

