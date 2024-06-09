grade = float(input('Nota: '))
if grade < 0 or grade > 10:
    while True:
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('ERRO! Digite um número entre 0 e 10')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        grade = float(input('Nota: '))
        if grade >= 0 and grade <= 10:
            print('Tudo certo')
            break
else:
    print('Tudo certo')

# outra resolução
# grade = float(input('Nota: '))
# while grade < 0 or grade > 10:
#     print('Notas entre 0 e 10!')
#     grade = float(input('Nota: '))
# print('Tudo certo')

