cont = homens = mulher = 0
print('-' * 30)
print(' ' * 4, 'CADASTRE UMA PESSOA')
print('-' * 30)
while True:
    idade = int(input('Idade: '))
    if idade >= 18:
        cont += 1
    sexo = str(input('Sexo? [M/F] ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Comando Inválido! Tente novamente!\nQual o seu sexo? [M/F] ')).strip().upper()[0]
    print('='*30)
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    escolha = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    print('=' * 30)
    while escolha not in 'SN':
        escolha = str(input('Comando Inválido! Tente novamente!\nVocê quer continuar? [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break
print('-'*12, f'DADOS', '-'*11,
      f'\n{cont} pessoas tem mais de 18 anos.'
      f'\n{homens} homens foram cadastrados.'
      f'\n{mulher} mulheres tem menos de 20 anos.'
      f'\nFim!')
