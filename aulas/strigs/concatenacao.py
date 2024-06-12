word = input('Palavra: ')
counter = 0
substituir = ''
while counter < len(word):
    if word[counter] in 'aeiou':
        substituir += '*'
    else:
        substituir += word[counter]
    counter += 1
print(substituir)

