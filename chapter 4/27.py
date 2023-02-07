"""
Escreva um programa que pergunte a distância que um passageiro deseja pecorrer em km. Calcule o preço da
passagem, cobrando R$ 0,50 por km para viagens de até 200 km, R$ 0,45 para viagens mais longas
"""

def solve():
    distance = float(input())

    if(distance <= 200):
        Multado = 0.5 * (distance)
        print(f"Foi Multado: {Multado} reais")
    elif(distance >200):       
        Multado = 0.45 * (distance) 
        print(f"Foi Multado: {Multado} reais")
        
solve()    