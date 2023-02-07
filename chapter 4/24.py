"""
Escreva um programa que leia três números e que imprima o
maior e o menor.
"""


x=int(input(""))
y=int(input(""))
z=int(input(""))

def solve(x,y,z):
    if(x>=y and x>=z):
        print(f"Largest: {x}")
    elif(y>=x and y>=z):
        print(f"Largest: {y}")
    elif(z>=x and z>=y):
        print(f"largest: {z}")

solve(x,y,z)
