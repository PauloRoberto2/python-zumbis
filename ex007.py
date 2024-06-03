#  Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32

temperatura = int(input('Temperatuda em Celsius: '))
calc_fahrenheit = temperatura * 9 / 5 + 32

print(f'{calc_fahrenheit:.2f}')
