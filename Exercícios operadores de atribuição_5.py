# Leia estoque (int) e vendidas (int). Atualize com -= e mostre o estoque final.

estoque = int(input('Digite a quantidade de estoque: '))
vendidas = int(input('Digite a quantidade vendida'))

estoque -= vendidas

print('Estoque', estoque)