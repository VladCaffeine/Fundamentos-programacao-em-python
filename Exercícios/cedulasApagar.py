retirada = int(input("Quanto você precisa? "))
divida = retirada

atual = 50
cedulas = 0

while (True):
    if (atual <= divida):
        divida -= atual
        cedulas += 1
    else:
        print("%d cedulas de R$ %d" %(cedulas, atual))

    if (divida == 0):
        break

    if (atual == 50):
        atual = 20
    elif (atual == 20):
        atual = 10
    elif (atual == 10):
        atual = 5
    elif (atual == 5):
        atual = 1
    cedulas = 0
