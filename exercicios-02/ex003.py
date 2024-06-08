peso_peixe = float(input('Peso do peixe: '))
print('~' * 30)

# Multa de R$4,00 para cada quilograma a mais que o limite; 50 quilos

if peso_peixe > 50:
    multa = (peso_peixe - 50) * 4
    print(f'Peso excedente: {peso_peixe - 50:.2f}')
    print(f'Valor da multa: R$ {multa:.2f}')
else:
    multa = excesso = 0
    print('Peso ok.\nNada a pagar.')

