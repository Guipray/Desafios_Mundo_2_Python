num = cont = s = 0
num = int(input('Digite um número (999 para o programa): '))
while num != 999:
    s += num
    cont += 1
    num = int(input('Digite um número (999 para o programa): '))
print(f'Foram digitados {cont} números, e a soma entre eles é {s}!')
