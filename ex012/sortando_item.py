import random
n1 = str(input("Nome do primeiro aluno: "))
n2 = str(input("Nome do segundo aluno: "))
n3 = str(input("Nome do terceiro aluno:"))
lista = [n1, n2, n3]
escolhido = random.choice(lista)
print("O aluno escolhido foi {}".format(escolhido))

