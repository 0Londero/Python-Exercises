"""
Escreva um programa que leia dois números em ponto flutuante e imprima a soma desses números.
"""

def sum(first_number, second_number):
    return first_number + second_number

print("WRITE TWO NUMBERS FOR THE SUM")
n1 = float(input("The first number:"))
n2 = float(input("The second number:"))
print(f"The sum is:     ->    {sum(n1,n2):.2f} ")