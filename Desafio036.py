valor = float(input('Qual o valor da casa: R$'))
salário = float(input('Qual o seu salário: R$'))
anos = int(input('Em quantos anos você vai pagar a casa: '))
prestação = valor / (anos * 12)
excedente = salário * 30/100
print(f'Para pagar uma casa de R${valor:.2f} em {anos} anos, a prestação será de R${prestação:.2f}!')
if prestação >= excedente:
    print('Seu empréstimo foi NEGADO!')
else:
    print('Seu empréstimo foi concedido!')
