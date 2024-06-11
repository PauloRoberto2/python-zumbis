# pais A tem uma população = 800.000
# taxa de crescimento anual de 3%
# pais B população 2.000.000
# taxa de crescimento 1.5%

populacao_a = 800000
crescimento_a = 3 / 100
populacao_b = 2000000
crescimento_b = 1.5 / 100

ano = 0
while populacao_a <= populacao_b:
    populacao_a = populacao_a + populacao_a * crescimento_a
    populacao_b = populacao_b + populacao_b * crescimento_b
    ano += 1

print(f'''Depois de {ano} anos
O pais A tem uma população maior ou igual ao pais B
Pais A = {populacao_a:.0f}
Pais B = {populacao_b:.0f}''')

