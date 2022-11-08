alt = float(input('Qual a sua altura? '))
peso = float(input('Qual o seu peso? '))
imc = peso / (alt ** 2)
print(f'Seu IMC é de {imc:.1f}!')

if imc <= 18.5:
    print('Você está Abaixo do peso!')
elif imc <= 25:
    print('Seu peso é Ideal!')
elif imc <= 30:
    print('Você está com Sobrepeso!')
elif imc <= 40:
    print('Você está com Obesidade!')
else:
    print('Você está com Obesidade Mórbida!')