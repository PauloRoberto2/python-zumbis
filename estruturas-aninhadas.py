minutos = int(input('Quantos minutos usou o telefone: '))

if minutos < 200:
    valor = minutos * 0.20
if minutos >= 200 and minutos <= 400:
    valor = minutos * 0.18
if minutos > 400:
    valor = minutos * 0.15

print(f'Total a pagar: R$ {valor:.2f}')


"""
# resolução professor:

if minutos < 200:
    valor = 0.20
else:
    if minutos <= 400:
        valor = 0.18
    else:
        valor = 0.15

"""
