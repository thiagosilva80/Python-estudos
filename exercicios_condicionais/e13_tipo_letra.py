# Exercício 13
# Leia uma letra e informe se é vogal ou consoante.

# escreva seu código abaixo
le = input('Digite uma letra: ').lower()

if le in "aeiou":
    print('Vogal')
else:
    print('Consoante')
