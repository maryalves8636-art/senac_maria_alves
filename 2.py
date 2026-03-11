#Solicite ao usuário que informe o saldo da sua conta e o valor que será depositado; ambos os valores devem ser do tipo FLOAT. 
#Utilize atribuição += para adicionar o deposito ao saldo da conta e exiba o novo saldo na tela.  

saldo = float(input('Digite seu saldo: '))
deposito = float(input('Digite o valor do depósito: '))

saldo += deposito

print('Saldo atual: ', saldo)
