"""
Faça um programa que calcule o aumento de um salário. Ele
deve solicitar o valor do salário e a porcentagem do aumento.
Exiba o valor do aumento e do novo salário    
"""

def solve():
    Salario = int(input("Salario "))
    Aumento = float(input("Aumento "))
    Salario = Salario * (Aumento / 100 + 1)

    print(f"Result: {Salario}")

solve()
