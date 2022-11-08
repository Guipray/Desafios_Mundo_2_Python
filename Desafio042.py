r1 = float(input('Qual o comprimento da primeira reta: '))
r2 = float(input('Qual o comprimento da segunda reta: '))
r3 = float(input('Qual o comprimento da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Essas retas formam um triângulo ', end='')
    if r1 == r2 == r3:
        print('Equilátero!')
    elif r1 != r2 != r3 != r1:
        print('Escaleno!')
    else:
        print('Isósceles!')
else:
    print('Essas retas NÃO formam um triãngulo!')
