peso_peixe = float(input('Peso do peixe: '))

# Multa de R$4,00 para cada quilograma a mais que o limite; 50 quilos
multa = (peso_peixe - 50) * 4
print('~' * 30)
print(f'Peso excedente: {peso_peixe - 50:.2f}')
print(f'Valor da multa: R$ {multa:.2f}')
