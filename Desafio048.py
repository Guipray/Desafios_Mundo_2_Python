import math
print('Aqui está a soma entre todos os números impares múltiplos de 3, de 1 a 500!')
s = 0
contador = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        contador += 1  # Resumido
        """contador = contador + 1"""  # Completo
        s += c  # Resumido
        """ s = s + c"""  # Completo
print(f'A soma dos {contador} valores é {s}!')
