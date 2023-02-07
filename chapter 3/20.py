"""
Escreva um programa que pergunte a quantidade de km
percorridos por um carro alugado pelo usuário , assim como
a quantidade de dias pelos quais o carro foi alugado. Calcule
o preço a pagar, sabendo que o carro custa R$ 60 por dia e
R$ 0,15 por km rodado.
"""

def solve():
    Quantidade_km = float(input("Quantidade de km: "))

    Quantidade_dias = float(input("Quantidade_dias: "))

    Resultado = (Quantidade_km * 0.15) + (Quantidade_dias * 60)

solve()