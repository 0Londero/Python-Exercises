"""
Faça um programa que converta um valor fornecido pelo usuário para o correspondente em octal
"""

print("Write down any value to be converted to octal")
number = int(input("The chosen number is:"))
number_octal = oct(number)
print(f"The number in Octal is: {number_octal}")