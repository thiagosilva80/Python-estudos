def mensagem():
    print("Olá mundo")
    
def calcular_desconto(preco):
    preco_final = preco * 0.8
    return preco_final


mensagem()
valor_pagar = calcular_desconto(100)
print(f"{valor_pagar: .2f}")