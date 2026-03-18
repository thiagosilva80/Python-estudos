# Exercício 4
# Leia duas notas e informe se o aluno foi aprovado (>=7) ou reprovado.

# escreva seu código abaixo
Nota1 = float(input('Digite a nota1: '))
Nota2 = float(input('Digite a nota2: '))

media = (Nota1 + Nota2) / 2
if media >= 7:
    print('Aluno aprovado')
else:
    print('Aluno reprovado')



