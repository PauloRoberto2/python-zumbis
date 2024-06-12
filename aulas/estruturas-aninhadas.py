minutos = int(input('Minutos: '))

"""
if minutos < 200:
    valor = minutos * 0.20
if minutos >= 200 and minutos <= 400:
    valor = minutos * 0.18
if minutos > 400:
    valor = minutos * 0.15

print(f'Total a pagar: R$ {valor:.2f}')
"""

if minutos < 200:
    valor = 0.20
elif minutos <= 400:
    valor = 0.18
elif minutos <= 800:
    valor = 0.15
# Promoção
else:
    valor = 0.08

print(f'R$ {minutos * valor:.2f}')
