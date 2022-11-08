from datetime import date
date = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input(f'Em qual ano a {c}ª pessoa nasceu? '))
    idade = date - ano
    if idade < 21:
        menor += 1
    elif idade >= 21:
        maior += 1
print('')
print(f'Ao todo {maior} pessoas são maiores de 21 anos, e {menor} são menores de 21!')
