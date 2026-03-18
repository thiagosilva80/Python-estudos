# Exercício 9
# Leia a idade e classifique: criança (<12), adolescente (<18), adulto.

# escreva seu código abaixo

id = int(input('Digite a sua idade: '))

if id <= 12:
    print('Criança')
elif id <= 18:
    print('Adolecente')
else:
    print('Adulto')

