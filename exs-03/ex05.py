# algoritmo de euclides
# Maximo divisor comum

# a, b = 135, 28

a = int(input('N1: '))
b = int(input('N2: '))

# coloque print(a) dentro do while para ver o passo a passo
while b != 0:  
    a, b = b, a % b

print(f'MDC {a}')

