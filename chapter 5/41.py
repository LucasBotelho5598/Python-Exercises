"""
Modifique o programa anterior para que aceite respostas com letras maiúsculas e minúsculas  eme todas as questões
"""

pontos=0
questao=1

while questao <=3:
    resposta=input(questao)
    if questao ==1 and resposta=="b" or resposta=="B":
        pontos = pontos +1
    if questao ==2 and resposta=="a" or resposta=="A":
        pontos = pontos +1
    if questao ==2 and resposta=="d" or resposta=="D":
        pontos = pontos +1
    questao = questao + 1
    print(pontos)




