# Exercício 6
# Leia dois números e mostre qual é o maior.

# escreva seu código abaixo
n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))

if n1 > n2:
    print("O maior numero é", n1)
elif n2 > n1:
    print("O maior numero é", n2)
else:
    print("Os dois são iguais")