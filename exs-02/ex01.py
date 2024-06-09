# Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

a = int(input('A: '))
b = int(input('B: '))
c = int(input('C: '))
print('~~~~~~~~~~Calculando~~~~~~~~~~')

if a > b + c or b > a + c or c > a + b:
    print('Esse triangulo não pode exisitir')
elif a == b == c:
    print('Equilatero')
elif a == b or b == c or a == c:
    print('Isosceles')
else:
    print('Escaleno')
