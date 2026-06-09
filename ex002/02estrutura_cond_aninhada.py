nota = float(input("Digite sua nota: "))
frequencia = int(input("Digite sua frenquência: "))

if nota >= 5 and frequencia >= 75:
    situacao = "aprovado"
elif nota >= 5 or frequencia >75:
    situacao = "na recuperação"
else:
    sitaca0 = "reprovado"

print(f"Voce está {situacao}")