"""
Modifique o programa anteriore pra imprimir de 1 até o número digitado pelo usuário,mas,dessa vez,
apenas os números ímpares
"""
n=int(input(""))

def solve():
    x=0
    while(x<=n):
        if x % 3 == 1:
            print(x)
        x=x+1
    



solve()