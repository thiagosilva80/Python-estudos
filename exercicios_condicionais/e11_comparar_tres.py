# Exercício 11
# Leia três números e mostre o maior.

# escreva seu código abaixo
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))

maior = n1

if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3

    print('O numero maior é: ' , maior)


