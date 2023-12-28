pontos = 0
questoes = 1

while (questoes <= 3):
    resposta = int(input("Qual a sua resposta da questão %d" %(questoes)))

    if (questoes == 1 and (resposta == "b" or resposta == "B")):
        pontos += 1
    elif (questoes == 2 and (resposta == "a" or resposta == "A")):
        pontos += 1
    elif (questoes == 3 and (resposta == "d" or resposta == "D")):
        pontos += 1
    
    questoes += 1

print("O aluno fez %d ponto(s)" %(pontos))
