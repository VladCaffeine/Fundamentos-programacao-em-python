# Usando listas como duas filas.

rowOne = 0
rowTwo = 0

listRowOne = []
listRowTwo = []

# F = novo cliente, A = atender cliente, S = sair > fila 1
# G = Novo cliente, B = atender cliente, S = sair > fila 2
while True:
    print("Para operar a primeira fila escolha abaixo:\n")
    print("F = NOVO CLIENTE\nA = ATENDER CLIENTE\nS = SAIR\n")
    print("Para operar a segunda fila escolha abaixo:\n")
    print("G = NOVO CLIENTE\nB = ATENDER CLIENTE\nS = SAIR")

    operation = input("Opção: ")

    if operation == "F" or operation == "f":
        rowOne += 1
        listRowOne.append(rowOne)
    elif operation == "G" or operation == "g":
        rowTwo += 1
        listRowTwo.append(rowTwo)

    if operation == "A" or operation == "a":
        client = listRowOne.pop(0)
        print("Cliente %d atendido" % (client))
    elif operation == "B" or operation == "b":
        client = listRowTwo.pop(0)
        print("Cliente %d atendido" % (client))

    if operation == "S" or operation == "s":
        goOut = int(input("Tem certeza que quer sair?\n1)Sim\n2)Não"))

        if goOut == 1:
            break
        else:
            print("")
