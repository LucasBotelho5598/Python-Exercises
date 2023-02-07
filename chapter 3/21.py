"""
Escreva um programa para calcular a redução do tempo de
vida de um fumante. Pergunte a quantidade de cigarros
fumados por dia e quantos anos ele já fumou. Considere que
um fumante perde 10 minutos de vida para cigarro, e calcule
quantos dias de vida de um fumante perde 10 minutos de vida
a cada cigarro, e calcule quantos dias de vida de um fumante    
"""

def solve():
    Cigarros_por_dia = float(input("Cigarros por dia: "))

    Anos_fumados = float(input("Anos fumados: "))

    Resultado = (Anos_fumados * 365) - ((Cigarros_por_dia * 10 / 60) / 24)

    print(f"Result: {Resultado}")
    
solve()