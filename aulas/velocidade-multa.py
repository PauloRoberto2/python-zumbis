velocidade = int(input('Velocidade: '))
multa = (velocidade - 110) * 5

if velocidade > 110:
    print('~~~~~~~~~~~~~~~~~~~~')
    print('MULTADO!')
    print(f'Valor: R$ {multa:.2f}')
    print('~~~~~~~~~~~~~~~~~~~~')
else:
    print('~~~~~~~~~~~~~~~~~~~~')
    print('Não foi multado.')
    print('~~~~~~~~~~~~~~~~~~~~')

