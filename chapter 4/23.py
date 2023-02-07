"""
Escreva um programa que permite a velocidade do carro de
um usuário. Caso ultrapasse 80 km/h, exiba um mensagem
dizendo que o usuário foi multado. Neste caso, exiba o valor
da multa, cobrando R5$ por km acima de 80 km/h.
"""
def solve():
    Velocidade = float(input())

    if(Velocidade > 80):
        Multado = 5 * (Velocidade)
        print(f"Foi Multado: {Multado} reais")
    else:
        print("Não foi multado")


solve()    