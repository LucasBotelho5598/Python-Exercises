"""
Analise o Programa 4.1.Responda o que acontece se o primeiro
e o segundo valores forem iguais ? Explique
"""

def solve():
    # Programa 4.1

    NumberOne = int(input(""))
    NumberTwo = int(input(""))

    if NumberOne > NumberTwo:
        print("Maior")
    else:
        print("Menor")

"""
 Dois valores iguais resultará em "Menor".Como a primeira condição não foi
 atendida, teremos a segunda como a correta.
"""
