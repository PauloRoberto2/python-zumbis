# Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.

salario = float(input('Salario atual: '))
aumento = float(input('Percentagem de aumento: '))

resultado = salario + salario * aumento / 100

print(f'Novo salario: {resultado:.2f}')