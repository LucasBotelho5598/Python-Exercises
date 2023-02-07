"""
Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. Você pode calcular soma(+), 
subtração(-),multiplicação(*) e divisão(/). Exiba o resultado da operação solicitada
"""

a=int(input(""))
b=int(input(""))
operacao=int(input(""))

def solve():
    if operacao==1:
        return print(a+b)
    elif operacao==2:
        return print(a-b)
    elif operacao==3:
        return print(a*b)
    elif operacao==4:
        return print(a/b)

solve()        

    

