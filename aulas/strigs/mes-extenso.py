date = input('data dd/mm/aaaa: ')
date_splited = date.split('/')

months = [
    'janeiro',
    'fevereiro',
    'março',
    'abril',
    'maio',
    'junho',
    'julho',
    'agosto',
    'setembro',
    'outubro',
    'novembro',
    'dezembro',
] 

print(f'{date_splited[0]} de {months[int(date_splited[1])-1]} de {date_splited[2]}')

