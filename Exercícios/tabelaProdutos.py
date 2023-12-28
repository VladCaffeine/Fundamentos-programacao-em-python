valorTotalCompra = 0
while True:
    codigoProduto = int(input(
        "Qual o código do produto?\n1)0,50\n2)1,00\n3)4,00\n5)7,00\n9)8,00\n0(zero) para cancelar\nEscolha: "))

    quantidadeProduto = 0

    if (codigoProduto == 0):
        break
    elif (codigoProduto == 1 or codigoProduto == 2 or codigoProduto == 3 or codigoProduto == 5 or codigoProduto == 9):
        quantidadeProduto = int(input("Qual a quantidade de produto? \n"))
    else:
        print("Código Invalido")
    
    valorTotalProduto = 0

    if (codigoProduto == 1):
        valorTotalProduto = float(0.50 * quantidadeProduto)
    elif (codigoProduto == 2):
        valorTotalProduto = float(1.00 * quantidadeProduto)
    elif (codigoProduto == 3):
        valorTotalProduto = float(4.00 * quantidadeProduto)
    elif (codigoProduto == 5):
        valorTotalProduto = float(7.00 * quantidadeProduto)
    elif (codigoProduto == 9):
        valorTotalProduto = float(8.00 * quantidadeProduto)
    
    valorTotalCompra += valorTotalProduto

print("O valor total da compra ficou igual a: R$ %0.2f" %(valorTotalCompra))
