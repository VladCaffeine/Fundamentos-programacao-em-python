# Para metodos associados a um objeto utilizamos um objeto.função( ), veja
# com o metodo append

# list = [2, 6, 8, 5, 3]
#
# list.append(19)
#
# print(list)

# Com o metodo append() podemos então adicionar quantos indices quisermos sem
# precisar determinar de forma breve antes tinhamos que determinar ja de cara a
# quantidade de indice e depois modificar um por um para adicionar os valores
# que assim queriamos, algo que com o append não é necessário, podemos usar
# ele para ir adicionando valores na lista.

# loop basico usando o append

# list = []
#
# while (len(list) < 5):
#     newIndex = int(input("Qual novo valor da lista? "))
#     list.append(newIndex)
#
# x = 0
# while (x < len(list)):
#     print(list[x])
#     x += 1
#
# print(len(list))

# Outra forma de adicionar elementos a uma lista é usando o operador de soma,
# também é possível adicionar uma lista a outra, nesse momento o
# interpretador vai chamar um metodo chamado extend que realiza tal feito.

# list = []
#
# while (len(list) < 5):
#     list += [int(input("type: "))]
#
# print(list)

# usar o operador de soma a uma lista, faz com que adicione elementos,
# ao contrário de somar de fato seus atributos.

# O metodo .extend() vai pegar elementos de uma lista e estender em outra,
# enquanto se adicionamos uma lista com o metodo .append(), vamos colocar
# listas dentro de listas e não seus valores de fato.

# usando extend

# listOne = [1, 2, 3, 4]
#
# listTwo = [5, 6, 7, 8]
#
# listOne.extend(listTwo)
#
# print(listOne)

# usando append

# listOne = [1, 2, 3, 4]
# listTwo = [5, 6, 7, 8]
#
# listTree = []
#
# listTree.append(listOne)
# listTree.append(listOne)
#
# print(listOne)

# é possível adicionar listas dentro de uma lista vazia e criar conjuntos de
# listas mas não adicionar uma lista solta dentro de uma lista
