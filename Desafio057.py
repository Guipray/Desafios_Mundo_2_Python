sexo = str(input('Qual seu sexo? [F/M] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Inválido. Tente novamente! \nQual seu sexo? [F/M] ')).strip().upper()[0]
print(f'Sexo {sexo} registrado!')
