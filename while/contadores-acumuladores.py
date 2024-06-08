n = 1
soma = 0
while n <= 10:
    x = int(input(f'{n} número: '))
    soma = soma + x
    n = n + 1
print(soma)

# media
media = soma / n
print(f'{media:.2f}')

