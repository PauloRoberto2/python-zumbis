soma = 0
cont = 0 
while True:
    x = int(input('Número: '))
    if x == 0:
        break
    else:
        cont = cont + 1
    soma = soma + x
media = soma / cont
print(f'Soma: {soma}\nMédia: {media:.2f}')

