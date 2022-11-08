from random import randint
cont = 0
print('=-' * 30)
print('Vamos Jogar Par ou Ímpar!')
while True:
    print('=-' * 30)
    player = int(input('Digite um Valor: '))
    comp = randint(0, 10)
    escolha = ' '
    escolha = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    while escolha not in 'PI':
        escolha = str(input('Comando Inválido! Tente novamente.\nPar ou Ímpar? [P/I] ')).strip().upper()[0]
    soma = player+comp
    print('-' * 30)
    if soma % 2 == 0:
        print(f'Você jogou {player} e o computador {comp}.\nO total deu {soma}, ou seja, par.')
        vencedor = 'P'
    else:
        print(f'Você jogou {player} e o computador {comp}.\nO total deu {soma}, ou seja, ímpar.')
        vencedor = 'I'
    print('-' * 30)
    if escolha == vencedor:
        print('Você venceu!\nVamos jogar novamente!')
        cont += 1
    else:
        print('Você perdeu!')
        break
print(f'Game Over! Você venceu {cont} vezes.')
