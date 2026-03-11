# Leia base (float). Aplique *= 1.05 (aumento 5%), depois -= 2 (taxa), depois /= 2.

base = float(input('Digite o valor: '))

base *= 1.05
print('Após aumento de 5%:', base)

base -= 2
print('Após taxa:', base)

base /= 2
print('Resultado final:', base)