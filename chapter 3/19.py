"""
Escreva um programa que converta uma temperatura digitada
em C em F. A fórmula para essa conversão
"""
def solve():
    Celsius = float(input("Celsius: "))

    Fahrenheit = ((9 * Celsius) / 5) + 32

    print(f"Result {Fahrenheit}")

solve()

