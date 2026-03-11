#Solicite um número (int), aplique n %= 2 e exiba o valor na tela. 
# Se o resultado for 0, o número é par; se o resultado for 1, o número é ímpar.

n = int(input('Digite um número inteiro: '))
n %= 2

print(n)

if n == 0:
 print('Número par')

else: 
 print('Número ímpar')
