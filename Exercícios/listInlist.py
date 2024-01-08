listOne = []
x = 1
while (len(listOne) < 5):
    addIndex = int(input("type index %d: " % (x)))
    listOne.append(addIndex)
    x += 1

listTwo = []
x = 1
while (len(listTwo) < 5):
    addIndex = int(input("type index %d: " % (x)))
    listTwo.append(addIndex)
    x += 1

listTree = []
listTree.extend(listOne)
listTree.extend(listTwo)


print(listTree)
