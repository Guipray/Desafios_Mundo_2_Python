num = int(input('Digite um número: '))
print('Esta é a tabuada no número que você pediu!')
for c in range(1, 11):
    print(num, 'x', f'{c:2}', '=', num * c)
