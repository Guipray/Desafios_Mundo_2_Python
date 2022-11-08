opção = 0
num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
while opção != 5:
    opção = int(input("[ 1 ] Somar"
      "\n[ 2 ] Multiplicar"
      "\n[ 3 ] Maior"
      "\n[ 4 ] Novos números"
      "\n[ 5 ] Sair do programa"
      "\nQual das opções a cima você escolhe? "))
    if opção == 1:
        soma = num1 + num2
        print(f'A soma entre {num1} e {num2} é {soma}!')
    elif opção == 2:
        mult = num1 * num2
        print(f'A multiplicação entre {num1} e {num2} é {mult}!')
    elif opção == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print(f'Dos números {num1} e {num2} que você digitou, o {maior} é maior!')
    elif opção == 4:
        print('Informe os números novos números!')
        num1 = int(input('Primeiro número: '))
        num2 = int(input('Segundo número: '))
    elif opção != 5:
        print('Opção inválida! Tente novamente!')
    print('='*40)
print('Programa finalizado!')
