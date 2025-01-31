"""
Faça um programa que converta graus Co em graus Fo e vice-versa. Ou seja, se for lida uma temperatura em graus Celsius,
esta deverá ser convertida em graus Fahrenheit e se for lida em graus Fahrenheit,
deverá ser convertida em graus Celsius.
"""

print("Temperature Converter - This program will convert the temperature from graus Celsius to Fahrenheit and the other way around.")

print("1 - Convert celsius into Fahrenheit")
print("2 - Convert Fahrenheit into celsius")

def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = fahrenheit - 32
    return celsius

choice = int(input("Enter your choice: "))

if choice == 1:
    celsius_number = int(input("Enter a temperature in Celsius: "))
    print(f"The temperature in fahrenheit is: {celsius_to_fahrenheit(celsius_number)}")
elif choice == 2:
    fahrenheit_number = int(input("Enter a temperature in Fahrenheit: "))
    print(f"The temperature in Celsius is: {fahrenheit_to_celsius(fahrenheit_number)}")
else:
    print("Enter a valid choice. The number must only be 1 or 2.")
