ano = int(input('Ano: '))

if ano % 100 == 0 and ano % 400 == 0:
    print('Ano bissexto!')
elif ano % 4 == 0 and ano % 100 != 0:
    print('Ano bissexto!')
else:
    print('Não é bissexto!')

"""
trexo da lib calendar.py:
def isleap(year):
    # Return True for leap years, False for non-leap years.
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
"""
