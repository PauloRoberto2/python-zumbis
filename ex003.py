# Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.

d = int(input('Dias: '))
H = int(input('Horas: '))
m = int(input('minutos: '))
s = int(input('segundos: '))

calculo = d * 24 * 60 * 60 + H * 60 * 60 + m * 60 + s
print(calculo)