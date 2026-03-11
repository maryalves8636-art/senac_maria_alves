# Leia um número (int), aplique n %= 2 e imprima.
# 0 = par, 1 = ímpar

n = int(input('Digite um numero inteiro: '))

n %= 2 
if n == 0:
    print('Número par')
else:
    print('Número ímpar')


