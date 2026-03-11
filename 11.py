#Solicite ao usuário que informe os tempos em segundos (int). Converta para minutos inteiros com //= e depois use %= para obter segundos restantes.  

segundos = int(input('Informe os segundos: '))

minutos = segundos // 60
segundos_restantes = segundos % 60

print('Minutos:', minutos)
print('Segundos restantes:', segundos_restantes)