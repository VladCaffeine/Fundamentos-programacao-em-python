# # a função len é capaz de ler para mim o tamanho de uma lista
#
# list = [5, 6, 2, 9]
#
# print(len(list))
#
# # A função retorna sempre um valor com base decimal,
# # ou seja, contando a partir do 1
# # uma função feita para entregar valores ao usuário.
#
# txt = "ola"
#
# print(len(txt))

# Usando len para uma estrutura de repetição.

list = [3, 5, 6, 3]

x = 0

while (x < len(list)):
    print(list[x])
    x += 1
