"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
"""

valor_por_hora = float(input('Informe o valor recebido por hora R$ '))
num_horas_trabalhadas = float(input('Quantas horas mensais foram trabalhadas: '))

sálario = valor_por_hora * num_horas_trabalhadas

print(f'Você receberá um total de R$ {sálario:.2f}')