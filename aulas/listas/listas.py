# moradores_predio = [
#     'Paulo',
#     'Maria',
#     'João',
#     'Lucas',
#     'Mario',
#     'Leticia',
#     'Gabriel',
#     'Roberto',
#     'Ligia',
#     'Torres',
#     'Cesar',
# ]
# 
# print(moradores_predio[0:])
# 

soma = 0 
counter = 0
notas = [10, 5, 6, 4, 9, 7, 6, 2, 5, 4, 10, 9, 7, 3, 4, 7, 8]
while counter < len(notas):
    soma += notas[counter]
    counter += 1
print(f'{soma/len(notas):.2f}')

