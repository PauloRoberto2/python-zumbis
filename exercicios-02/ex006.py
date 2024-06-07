salario_hora = float(input('Quando você ganha por hora: '))
horas_trabalhadas = int(input('Horas trabalhadas no mês: '))

# valor ganho no mês
salario = salario_hora * horas_trabalhadas

# descontos no salario
imposto_renda = salario * 11 / 100
inss = salario * 8  / 100
sindicato = salario * 5 / 100
descontos = imposto_renda + inss + sindicato
# liquido
salario_liquido = salario - descontos

# output
print('~' * 40)
print(f'Salário bruto: R$ {salario:.2f}')
print(f'Imposto de renda(11%): - R$ {imposto_renda:.2f}')
print(f'INSS(8%): - R$ {inss:.2f}')
print(f'Sindicato(5%): - R$ {sindicato:.2f}')
print(f'Salário liquido: R$ {salario_liquido:.2f}')
