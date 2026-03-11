#Solicite um valor de estoque (int), subtraia as vendas utilizando -= e depois a reposição do estoque utilizando +=, por fim, aplique %= 6. 

estoque = int(input('Quantidade de estoque: '))
vendas = int(input('Quantidade vendida: '))
reposição = int(input('Reposição: '))

estoque -= vendas
estoque += reposição
estoque %= 6

print('Estoque final:', estoque)