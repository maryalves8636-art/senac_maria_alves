#Solicite ao usuário que informe o estoque no início do dia (int) e a quantidade vendida ao final do dia (int). 
# Atualize a quantidade utilizando atribuição -= para mostrar o estoque final.

estoque_inicial = int(input('Estoque inicial: '))
quantidade_vendida = int(input('Quantidade vendida: '))

estoque_inicial -= quantidade_vendida

print('Estoque atual: ', estoque_inicial)