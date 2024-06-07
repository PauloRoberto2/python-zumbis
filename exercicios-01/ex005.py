# Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.

preco = float(input('Valor do item: '))
desconto = float(input('Porcentagem de desconto: '))

preco = preco - (preco * desconto) / 100

print(f'{preco:.2f}')
