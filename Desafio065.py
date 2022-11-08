# Primeiro Modo de fazer. Eu fiz.
num = cont = s = 0
num = int(input('Digite um número (-1 para o programa): '))
while num != -1:
    s += num
    cont += 1
    média = s / cont
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    num = int(input('Digite um número (-1 para o programa): '))
print(f'Você digitou {cont} números!')
print(f'A média entre eles é {média:.2f}! O maior número é {maior}, e o menor é {menor}!')
print('FIM!')

#  Segundo Modo de fazer. Da aula.

"""resp = 'S'
cont = s = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    s += num
    cont += 1
    média = s / cont
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
print(f'Você digitou {cont} números!')
print(f'A média entre eles é {média}! O maior número é {maior}, e o menor é {menor}!')
print('Acabou')"""
