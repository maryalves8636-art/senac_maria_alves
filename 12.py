#Solicite ao usuário uma distância em metros e depois converta para km inteiros com //= 1000, guarde os metros restantes utilizando %= (utilize outra variável).

metros = int(input('Informe a distância em metros: '))

km = metros
km //= 1000

metros_restantes = metros
metros_restantes %= 1000

print('km:', km)
print('metros :', metros_restantes)