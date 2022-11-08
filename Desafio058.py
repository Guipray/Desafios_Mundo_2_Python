from random import randint
comp = randint(0, 10)
num = 1

""" acertou = False 'Outro modo de fazer' """

print('Tente adivinhar o número que eu imaginei entre 0 e 10!')
player = int(input('Qual número você escolhe? '))

""" while not acertou:
    player = int(input('Qual número você escolhe? '))
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('O número é maior. Tente novamente!')
        elif jogador > computador:
            print('O número é menor. Tente novamente!')"""

while player != comp:
    if player < comp:
        player = int(input('Você não acertou o número! Ele é maior!\nTenta de novo! '))
    else:
        player = int(input('Você não acertou o número! Ele é menor!\nTenta de novo! '))
    num += 1
print(f'Você acertouuu! E precisou de {num} tentativas!')
