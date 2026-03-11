# Leia dias (int). Mantenha apenas os dias restantes após converter para semanas (7 dias) usando %=.

dias = int(input('Digite a quantidade de dias: '))

dias %= 7

print('Dias restantes: 'dias)
