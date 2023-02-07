"""
Modifique o programa anteriores de forma que o usuário também digite o inicío e o fim da tabuada,em vez de começar com 1 e 10.
"""

n=int(input(""))
end=int(input(""))

mult="x"
def solve():
    x=1    
    while(x<=end):
        print(f"{n}{mult}{x} = ",x)
        x=x+1        
    
solve()