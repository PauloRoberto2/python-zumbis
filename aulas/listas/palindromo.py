palavra = str(input('Que palavra quer verificar? '))

inverte_palavra = palavra[::-1]

if palavra == inverte_palavra:
    print(f'\'{palavra}\' é um palindromo, pois se escreve igual de trás para frente: {inverte_palavra}')
else:
    print(f'{palavra} não é um palindromo, {inverte_palavra}')
