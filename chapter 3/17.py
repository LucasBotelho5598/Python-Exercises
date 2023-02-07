"""
Faça um programa que solicite o preço de umas mercadorias
e o percentual de desconto. Exiba o valor do desconto e o
preço a pagar
"""

def solve():
    Mercadoria = int(input("Mercadoria: "))
    Desconto = float(input("Desconto: "))

    Desconto_da_Mercadoria = (Desconto / 100) * Mercadoria

    Mercadoria = Mercadoria - Mercadoria * (Desconto / 100 )

    print(f"O desconto é R${Desconto_da_Mercadoria} reais e o valor da mercadoria é R${Mercadoria}")
    
solve()
