saque = int(input('Qual o valor do saque? R$'))
valor = saque
nota = 50
cont = 0
while True:
    if valor >= nota:
        valor -= nota
        cont += 1
    else:
        if cont > 0:
            print(f'Foram entregues {cont} cédulas de R${nota:.2f}!')
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        cont = 0
        if valor == 0:
            break
print('='*10, 'Fim da Transação!', '='*10)
