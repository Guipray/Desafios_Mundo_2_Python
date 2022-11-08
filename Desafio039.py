from datetime import date
sexo = str(input('Qual o seu sexo? ')).strip().upper()
if sexo == 'FEMININO':
    print('Você não precisa se alistar obrigatoriamente.')
else:
    atual = date.today().year
    ano = int(input('Em que ano você nasceu? '))
    idade = date.today().year - ano
    print(f'Você tem {idade} anos, ou quase. Isso em {atual}.')
    if idade < 18:
        falta = 18 - idade
        print(f'Você ainda é novo para se alistar. Faltam {falta} anos para você se alistar.')
        alistamento = atual + falta
        print(f'Seu alistamento será em {alistamento}.')
    elif idade == 18:
        print('Você já pode e deve se alistar este ano!')
    elif idade > 18:
        passou = idade - 18
        foi = atual - passou
        print(f'Você provavelmente se alistou em {foi} a {passou} anos atrás. ')
