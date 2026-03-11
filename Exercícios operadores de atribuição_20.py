# Leia tempo em segundos (int). Converta para minutos inteiros com //= 60 e depois use %= para obter segundos restantes.

segundos = int(input('Digite os segundos: '))

resto = segundos % 60
segundos //= 60

print('Minutos:', segundos)
print('Segundos:', resto)
