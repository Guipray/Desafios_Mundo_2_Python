from datetime import date
ano = int(input('Em qual ano você nasceu? '))
data = date.today().year
idade = data - ano
print(f'Você tem {idade} anos de idade.')

if idade <= 9:
    print('Sua categoria é : Mirim.')
elif idade <= 14:
    print('Sua categoria é : Infantil.')
elif idade <= 19:
    print('Sua categoria é : Junior.')
elif idade <= 25:
    print('Sua categoria é : Sênior.')
else:
    print('Sua categoria é : Master.')
