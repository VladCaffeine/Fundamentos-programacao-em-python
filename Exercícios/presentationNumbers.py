# Programa que adiciona uma lista e depois o usuario pode escolher

list = [0, 0, 0, 0, 0]

x = 0

while (x < 5):
    list[x] = int(input("Escolha um numero: "))
    x += 1

while (True):
    lookingNumber = int(input("Qual número da lista você quer? "))

    if (lookingNumber == 0):
        break

    print("Esse número é igual a %d da lista" % (list[lookingNumber - 1]))
