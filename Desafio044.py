print(f'\033[1:31m{" Lojas Roubo ":=^40}\033[m')
preço = float(input('Qual o preço do produto? R$'))
escolha = str(input("""Formas de Pagamento:
[ 1 ] À vista no dinheiro/cheque.
[ 2 ] À vista no cartão.
[ 3 ] Em até 2x no cartão.
[ 4 ] 3x ou mais no Cartão.\nQual forma você escolhe? """)).strip()
desc10 = preço - (preço * (10 / 100))
desc5 = preço - (preço * (5 / 100))
juros = preço + (preço * (20 / 100))
if escolha == '1':
    print(f'Você ganhou 10% de desconto, pague R${desc10:.2f}!')
elif escolha == '2':
    print(f'Você ganhou 5% de desconto, pague R${desc5:.2f}!')
elif escolha == '3':
    print(f'Sua compra será parcelada em 2x, ou seja R${preço/2:.2f}!')
    print(f'O preço permanece o mesmo. R${preço:.2f}!')
elif escolha == '4':
    print(f'Sua compra será de R${juros:.2f}!')
    parcela = int(input('Em quantas parcelas? '))
    preço2 = juros / parcela
    print(f'Como você parcelou a compra em {parcela} vezes! \nO valor parcelado será de R${preço2:.2f}!')
else:
    print('\033[31mOpção inválida. Tente Novamente.')
