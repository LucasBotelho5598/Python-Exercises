""""
Escreva um programa que leia dois números. Imprima o resultado da multiplicação do primeiro pelo segundo. Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de que podemos entender a multiplicação de dois números como somas sucessivas de um deles.
Assim, 4 x 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.
"""
n=int(input(""))

def solve():    
    x=1        
    while(x<=2):
        times="x"
        mult=x*n
        print(f"{n}{times}{x} = ",mult)
        x=x+1
        
        
    

solve()