tamanho_metros = int(input('m²: '))

"""
cobertuda da tinta 1L para 3 m²
lata de tinta tem 18L e custa R$ 80,00
"""
# litros necessário
litros_pintar = tamanho_metros / 3
print(f'Você precisa de: {litros_pintar:.2f}L de tinta')

capacidade_lata = 18
# calculo
if litros_pintar % capacidade_lata == 0:
    numero_latas = litros_pintar // capacidade_lata
else:
    numero_latas = litros_pintar // capacidade_lata + 1

preco_lata = 80
valor_pagar = preco_lata * numero_latas

print('~' * 40)
print(f'Você precisa de int({numero_latas}) latas')
print(f'Valor: {valor_pagar}')
print('~' * 40)
