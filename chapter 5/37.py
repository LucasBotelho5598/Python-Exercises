"""
Altere o programa anteriore para exibir os resultados no mesmo formato de uma tabuada:
2x1=2,2x2=4
"""
n=int(input(""))

def solve():    
    x=1        
    while(x<=10):
        times="x"
        mult=n*x
        print(f"{n}{times}{x} = ",mult)
        x=x+1
        
    

solve()