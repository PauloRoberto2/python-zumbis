tamanho_metros = int(input('m²: '))

"""
cobertuda da tinta 1L para 3 m²
lata de tinta tem 18L e custa R$ 80,00
"""
# litros necessário
litros_pintar = tamanho_metros / 3

capacidade_lata = 18
# calculo
if litros_pintar % capacidade_lata == 0:
    numero_latas = int(litros_pintar // capacidade_lata)
else:
    numero_latas = int(litros_pintar // capacidade_lata + 1)

preco_lata = 80
valor_pagar = preco_lata * numero_latas

print('~' * 40)
print(f'Serão usados {litros_pintar:.2f} litros')
print(f'Você precisa de {numero_latas} latas')
print(f'Valor: R$ {valor_pagar:.2f}')
print('~' * 40)
