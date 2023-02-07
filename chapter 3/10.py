"""
Escreva uma expressão para determinar se uma pessoa deve ou nao pagar imposto. Considere que pagam imposto pessoas cujo salário
é menor que R$ 1200,00
"""


def solve():
    salario=1500
    if(salario>1200):
        print("Pagar imposto")
    else:
        print("Não pagar imposto")

solve()        