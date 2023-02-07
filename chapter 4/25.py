"""
escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. para salários superiores a R$ 1250,00, calcule um aumento de 10%. Para 
inferiores ou iguais, de R15%
"""

salary=int(input(""))

def solve():
    if (salary > 1250):
        increase=salary * 1.1
        print("{:.2f}".format(increase))
    elif (salary <= 1250):
        increase=salary * 1.5
        print("{:.2f}".format(increase))
        

solve()     