while (True):
    rooting = float(input("Qual número você quer saber a raiz quadrada? "))

    b = 2.0
    while (True):
        p = (b + (rooting/b))/2

        squareP = p * p

        if abs(squareP - rooting) < 0.0001:
            break

        b = p

    print(p)
