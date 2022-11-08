num1 = int(input('Primeiro termo: '))
num2 = int(input('Razão: '))
décimo = num1 + (10 - 1) * num2
for c in range(num1, décimo + num2, num2):
    print(c, end=' ➡ ')
print('Acabou!')

