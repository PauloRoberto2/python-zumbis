num_1 = int(input('Primeiro número: '))
num_2 = int(input('Segundo número: '))
num_3 = int(input('Terceiro número: '))

if num_1 >= num_2 and num_1 >= num_3:
    print(f'{num_1} é o maior')
elif num_2 >= num_1 and num_2 >= num_3:
    print(f'{num_2} é o maior')
else:
    print(f'{num_3} é o maior')
