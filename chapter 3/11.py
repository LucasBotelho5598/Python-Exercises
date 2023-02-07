"""

Calcule o resultado da expressão A>B and C or D. utilizando os valores da tabela a seguir

And Tabela

---------
|V V |V 
|F V |F
|V F |F
|F F |F
--------

"""
A=10
B=3
C=True
D=False

def solve():
    if(A>B and (C or D)):
        print("True")
    else:
        print("False")
    

solve()