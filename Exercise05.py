"""
Uma firma contrata um encanador a R$ 20,00 por dia.
Escreva um programa que leia o número de dias trabalhados pelo encanador e imprima a quantia liquida que deverá ser paga,
sabendo-se que são descontados 8% para o imposto de renda.
"""

wage = 20.00

def tax_calculation (wage,days):
    gross_value = (wage*days)
    tax = gross_value*(8/100)
    net_value = gross_value-tax
    print(f"The Gross wage is: {gross_value}")
    print(f"The Tax is: {tax}")
    print(f"The wage after tax is: {net_value:.2f}")


print("How much days the worker have worked?")
days = int(input("Days = "))

tax_calculation(wage,days)
