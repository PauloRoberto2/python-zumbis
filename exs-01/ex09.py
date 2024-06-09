# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

km = float(input('Km pecorridos: '))
dias_alugados = int(input('Quantos dias ficou com o carro? '))

diaria = 60.00
km_rodado = 0.15

total = (km * km_rodado) + (dias_alugados * diaria)

print(f'Total a pagar: R$ {total:.2f}')
