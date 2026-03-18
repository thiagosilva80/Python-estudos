# Exercício 15
# Leia um ano e informe se é bissexto.

# escreva seu código abaixo
ano = int(input('Digite um ano: '))

if('ano % 4 == 0 and % 100 !=0') or (ano % 400 == 0):
    print('Ano é bissexto')
else:
    print('Ano não é bissexto')

