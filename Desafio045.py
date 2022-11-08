from random import randint
from time import sleep
print(f'\033[1:31m{" Vamos jogar Jokenpô? ":=^40}\033[m')
itens = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0, 2)
jogador = int(input("""Jogadas disponíveis:
[ 0 ] Pedra.
[ 1 ] Papel.
[ 2 ] Tesoura.
Qual você escolhe? """))
print('\033[1:31mJO\033[m', end='')
sleep(1)
print('\033[1:32mKEN\033[m', end='')
sleep(1)
print('\033[34mPO!!!\033[m')
sleep(0.5)
print(f'O computador jogou {itens[comp]}!')
print(f'Você jogou {itens[jogador]}!')
print('')
if comp == 0:  # Jogou PEDRA
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('VOCÊ GANHOU!')
    elif jogador == 2:
        print('VOCÊ PERDEU!')
    else:
        print('Jogada Inválida! Tente novamente!')
elif comp == 1:  # Jogou PAPEL
    if jogador == 0:
        print('VOCÊ PERDEU!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('VOCÊ GANHOU!')
    else:
        print('Jogada Inválida! Tente novamente!')
elif comp == 2:  # Jogou TESOURA
    if jogador == 0:
        print('VOCÊ GANHOU')
    elif jogador == 1:
        print('VOCÊ PERDEU!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('Jogada Inválida! Tente novamente!')
