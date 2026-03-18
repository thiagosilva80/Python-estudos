# Exercício 8
# Leia uma temperatura e classifique: frio (<15), ameno (15-25), quente (>25).

# escreva seu código abaixo
t = int(input('Digite a temperatura: '))

if t <= 15:
    print('Está frio')
elif t <= 25 :
    print('Está ameno')
else:
    print('Está quente')