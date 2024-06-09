number = int(input('Número: '))

if number >= 0:
    count = 0
    number_1 = 1
    while count <= number:
        if number == number_1 * (number_1 - 1) * (number_1 - 2):
            print(f'{number} é triangular, pois {number_1 - 2} x {number_1 - 1} x {number_1} = {number} ')
            break
        number_1 = number_1 + 1
        count = count + 1
else:
    print('Digite um número positivo')

