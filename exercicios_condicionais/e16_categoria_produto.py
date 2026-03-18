# Exercício 16
# Leia o preço e classifique: barato(<50), médio(<100), caro.

# escreva seu código abaixo
p = int(input('Digite o valor: '))

if p <= 50:
    print('barato')
elif p <= 100:
    print('medio')
else:
    print('caro')