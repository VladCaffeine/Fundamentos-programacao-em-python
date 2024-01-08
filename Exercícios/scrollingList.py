listOne = []
listTwo = []

while len(listOne) < 5:
    addIndexListOne = int(input("Type index list one:\n "))
    listOne.append(addIndexListOne)


while len(listTwo) < 5:
    addIndexListTwo = int(input("Type index list two:\n "))
    listTwo.append(addIndexListTwo)

listTree = []

copyListTwo = listTwo[::]
x = 0
while True:
    egual = True
    y = 0
    while True:
        if listOne[x] == listTwo[y]:
            egual = False
            copyListTwo.pop(y)
            y = 0
            break
        else:
            y += 1

        if y > 4:
            y = 0
            break

    if egual:
        listTree.append(listOne[x])

    x += 1

    if x > 4:
        listTree.extend(copyListTwo)
        break


print(listOne)
print(listTwo)
print(listTree)
