# Leia metros (int). Converta para km inteiros com //= 1000 e guarde metros restantes com %= (em outra variável).

mt = int(input('Digite os metros: '))

km = mt
km //= 1000

mt_restantes = mt
mt_restantes %= 1000

print('Km:', km)
print('Metros restantes:', mt_restantes)