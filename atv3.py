
def calcular_compra(valor):
    if valor < 100:
        desconto = 0
    elif valor < 300:
        desconto = 0.05
    elif valor < 500:
        desconto = 0.10
    else:
        desconto = 0.15

    valor_final = valor - (valor * desconto)

    return valor_final


valor = float(input("Valor da compra: R$ "))

valor_final = calcular_compra(valor)
economia = valor - valor_final

print(f"Valor original: R$ {valor:.2f}")
print(f"Valor final: R$ {valor_final:.2f}")
print(f"Valor economizado: R$ {economia:.2f}")
