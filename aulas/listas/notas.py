notas = []
counter = 0
soma = 0

while counter <= 3:
    notas.append(float(input('Nota: ')))
    soma += notas[counter]
    counter += 1
print(f'A média das notas: {notas}\n{soma/len(notas):.2f}')

