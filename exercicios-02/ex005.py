num_1 = int(input('Primeiro número: '))
num_2 = int(input('Segundo número: '))
num_3 = int(input('Terceiro número: '))

# menor número
if num_1 <= num_2 and num_1 <= num_3:
    menor = num_1
elif num_2 <= num_1 and num_2 <= num_3:
    menor = num_2
else:
    menor = num_3

# maior número

if num_1 >= num_2 and num_1 >= num_3:
    maior = num_1
elif num_2 >= num_1 and num_2 >= num_3:
    maior = num_2
else:
    maior = num_3

# exibindo resultado
print(f'Maior: {maior}')
print(f'Menor: {menor}')
