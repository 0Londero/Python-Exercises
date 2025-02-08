"""
Uma companhia telefônica opera com a seguinte tarifa: uma chamada telefônica com duração de 3 minutos custa R$ 1.15,
cada minuto adicional custa R$ 0.26.
Escreva um programa que leia a duração total de uma chamada (em minutos) e calcule o total a ser pago.
"""

calling = float(input("Write the call duration in minutes:"))

def call_value (call_duration):
    call = 1.15
    bonus_time = 0.26
    if call_duration > 3:
        value = (call_duration * bonus_time) + call
        print(f"The call cost was: ${value:.2f}")
    else:
        print(f"The call cost was: ${call:.2f}")

call_value(calling)