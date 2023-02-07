"""
Escreva um programa que calcule o preço a pagar pelo fornecimento de enrgia elétrica. Pergunte a quantidade de kWh consumida e o tipo
de instalação: R para residências, I para indústrias e C para comércios.Calcule o preço a pagar de acordo com a tabela a seguir
"""


preço=int(input(""))
categoria=input("")

def solve():    
    if preço<=500 and categoria=='R':
        print(preço*0.4)                                                                    
    if preço>500 and categoria=='R':
        print(preço*0.65)
    if preço<=1000 and categoria=='C':
        print(preço*0.55)                                                                    
    if preço>1000 and categoria=='C':
        print(preço*0.60)
    if preço<=5000 and categoria=='I':
        print(preço*0.55)                                                                    
    if preço>5000 and categoria=='I':
        print(preço*0.60)

solve()