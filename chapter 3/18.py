"""
Escreva um programa que calcule o tempo de uma viagem de
carro. Pergunte a distância a percorrer a velocidade média
esperada para a viagem
"""

def solve():
    Distancia = float(input("Distancia: "))
    Tempo = float(input("Tempo: "))

    Velocidade_Media = (Distancia / Tempo)
    print(f"A velocidade {Velocidade_Media}")

solve()
