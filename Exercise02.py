"""
Faça um programa que converta um valor fornecido pelo usuário para o correspondente em hexadecimal
"""

print("Write down any value to be converted to hexadecimal.")
number = int(input("Enter a number: "))
number_hex = hex(number)
print(f"The number in hexadecimal form is: {number_hex}")
