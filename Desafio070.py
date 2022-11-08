s = cont = acima = menor = 0
barato = ' '
while True:
    nome = str(input('Nome do Produto: '))
    preço = float(input('Preço R$'))
    s += preço
    cont += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = nome
    if preço > 1000:
        acima += 1
    fim = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    while fim not in 'SN':
        fim = str(input('Comando Inválido! Tente Novamente!\nVocê quer continuar? [S/N] ')).strip().upper()[0]
    if fim == 'N':
        break
print(f'-'*5, 'Finalizado', f'-'*5,
      f'\nO total gasto foi de R${s:.2f}.'
      f'\n{acima} produtos custam mais de R$1000,00.'
      f'\nO produto mais barato foi {barato}, que custa R${menor:.2f}.')
