#Solicite ao usuário que informe um orçamento (float) e um gasto (float). 
# Utilize atribuição -= para descontar o gasto do orçamento.  

orçamento = float(input('Informe seu orçamento: ')) 
gasto =float(input('Informe seu gasto: '))

orçamento -= gasto

print('Valor restante: ', orçamento)
