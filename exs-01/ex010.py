# Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o total de dias.

cigarros_fumados = int(input('Quantos cigarros fuma por dia? '))
fumante_anos = int(input('Por quantos anos você fumou? '))

total_cigarros = cigarros_fumados * fumante_anos * 365
minutos_perdidos = total_cigarros * 10

# Se perde 10 minutos a cada cigarro, há 1440m em um dia. 
dias_perdidos = total_cigarros / (60 * 24 / 10)

print(f'{dias_perdidos:.2f}')
