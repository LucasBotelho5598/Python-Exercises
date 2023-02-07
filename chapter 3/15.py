"""
Escreva um programa que leia a quantidade de dias horas, minutos e
segundos do usuário. Calcule o total em segundos
"""

Days = int(input("Days in Seconds: "))
Minutes = int(input("Minutes in Seconds: "))
Hours = int(input("Hours in Seconds: "))

def solve():    
    Days_for_Seconds = Days * 60 * 60 * 24
    Minutes_for_Seconds = Minutes * 60
    Hours_Seconds = Hours * 60 * 60
    Sum = Days_for_Seconds + Minutes_for_Seconds + Hours_Seconds

    #end

    print(f"{Days_for_Seconds}+{Minutes_for_Seconds}+{Hours_Seconds}={Sum}")

solve()    

