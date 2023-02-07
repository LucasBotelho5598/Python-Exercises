"""
Modifique o programa 2.2 de forma que ele calcule um aumento
de 15% para um salário de R$750   

"""

# Programa 2.2

def solve():
    salario = 1500
    aumento = 5
    print(salario + (salario * aumento / 100))

solve()    




#Modificação

def solve2():
    # aumento de 15% = 1,15
    salario2 = 750
    aumento2: float = 1.15
    Resultado = salario2 * aumento2
    print("{:.2f}".format(Resultado))

solve2()    




