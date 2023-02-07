"""
Escreva um programa que leia dois números. Imprima a divisão inteira do primeiro pelo segundo, 
assim como o resto da divisão. Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de que podemos entender o quociente da divisão de dois números como a quantidade de vezes que podemos retirar o divisor do dividendo. Logo, 20 ÷ 4 = 5, 
uma vez que podemos subtrair 4 cinco vezes de 20.
"""

dividendo = int(input("Dividendo: "))
divisor = int(input("Divisor: "))
quotient = 0
x = dividendo
def solve(x,quotient):
    """
    Example: 
    Dividend=20
    division=4
    quotient=5

    Fisrt step:
    20>=4 -> Correct

    Second step:
    


    """   
    while x >= divisor:
        x = x - divisor
        quotient = quotient + 1
    resto = x
    return print(f"{dividendo} / {divisor} = {quotient} (quociente) {resto} (resto)") 

solve(x,quotient)
