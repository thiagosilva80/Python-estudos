anos_experiencia = int(input("Digite os anos de experiência: "))

if anos_experiencia == 0:
    nivel = "estagiario"
elif anos_experiencia <=3:
    nivel = "júnior"
elif anos_experiencia <=8:
    nivel = "pleno"
else:
    nivel = "sênior"

print(f"Voce é um desenvolvedor do nivel: {nivel}")
