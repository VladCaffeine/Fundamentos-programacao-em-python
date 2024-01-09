# Para remover indices de uma lista no python podemos usar o 'del'
# cheguei a usar também o metodo pop.

# listTest = [1, 2, 3, 4, 5]
# print(listTest)
#
# del listTest[0]
#
# print(listTest)

# usando pop

# listTest02 = [5, 4, 3, 2, 1]
#
# listTest02.pop(0)
#
# print(listTest02)

# Usando a função del também conseguimos apagar fatias
# inteiras junto com slice.

lista = list(range(100))

print(lista)

del lista[1:99]

print(lista)
