"""
escreva um programa para aprovas o empréstimo bancário para compra de uma casa. O progarma deve perguntas o valor da casa
 comprar, o salário e a quantidade de anos a pagar. O valor da prestação mensal não pode ser superior a 30% do salário
 Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.
"""



casa=int(input(""))
salario=int(input(""))
quantidade_de_anos=int(input(""))

def solve():
    prestacao=casa/quantidade_de_anos
    if(prestacao>prestacao*0,3):
        print("Pode comprar")
    else:
        print("Nao pode comprar")
    

solve()    