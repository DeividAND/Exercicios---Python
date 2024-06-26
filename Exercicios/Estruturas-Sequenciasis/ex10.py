'''
Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
'''

temp_graus_c = float(input('Informe a temperatura em Graus °C: '))
temp_graus_f = (temp_graus_c * 9/5) + 32 

print(f'A temperatura {temp_graus_c}° tranformada em Fahrenheit fica: {temp_graus_f} °F')