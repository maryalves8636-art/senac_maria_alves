# Leia estoque (int). Subtraia venda com -=, depois reposição com +=, por fim %= 6.

estoque = int(input('Digite o estoque: '))
venda = int(input('Digite a quantidade vendida: '))
reposição = int(input('Digite a quanyodade reposta: '))

estoque -= venda 
estoque += reposição
estoque %= 6

print('Estoque atual: ', estoque)