média = 0
maior = 0
mulh = 0
hmaisvelho = ''
for c in range(1, 5):
    print('-'*5, f'{c}ª PESSOA', '-'*5)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    média += idade / 4
    if c == 1 and sexo == 'M':  # sexo in 'Mm' tbm funciona.
        maior = idade
        hmaisvelho = nome
    else:
        if idade > maior and sexo == 'M':
            maior = idade
            hmaisvelho = nome
    if sexo == 'F' and idade < 20:  # sexo in 'Ff' tbm funciona
        mulh += 1
print('')
print(f'A média de idade das 4 pessoas é de {média} anos!')
print(f'O homem mais velho tem {maior} anos, e se chama {hmaisvelho}!')
print(f'Ao todo {mulh} mulheres tem menos de 20 anos!')
