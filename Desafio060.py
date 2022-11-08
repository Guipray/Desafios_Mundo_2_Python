# Forma Fácil
"""from math import factorial
num = 1
while num != 0:
    num = int(input('Digite um número qualquer: '))
    fatorial = factorial(num)
    print(fatorial)
print('Fim')"""
# Com While
"""num = int(input('Digite um número qualquer para descobrir seu fatorial: '))
c = num
f = 1
print(f'O cálculo de {num}! é :')
while c > 0:
    print(c, end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)"""
# Com For
num = int(input('Digite um número qualquer para saber o seu fatorial: '))
f = 1
print(f'O cálculo de {num}! é: ')
for c in range(num, 0, -1):
    f *= c
    print(c, end='')
    print(' x ' if c > 1 else ' = ', end='')
print(f)
