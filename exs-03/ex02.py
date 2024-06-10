# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao
# nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

name = input('Nome: ')
password = input('Senha: ')

while name == password:
    print('''\
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ERROR ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
|        Digite senha diferente de nome       |
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
    ''')
    name = input('Nome: ')
    password = input('Senha: ')

