number_input = int(input('Fibonnaci do número: '))

a, b = 1, 1
counter = 0
while counter <= number_input - 2:
    a, b = b, a + b
    counter += 1
print(a)

