"""
Reescreva o programa anterior para escrever os 10 primeiros múltiplos de 3
"""

n=int(input(""))

def solve():
    """
    Mútiplos de 3 são números que
    deixam resto 0 !

    Exemplo: Tabuada    
    """
    x=0
    while(x<=n):
        if x % 3 == 0:
            print(x)
        x=x+1
    



solve()