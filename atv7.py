
def media_acima_limite(valores, limite):
    soma = 0
    quantidade = 0

    for valor in valores:
        if valor > limite:
            soma += valor
            quantidade += 1

    if quantidade == 0:
        return 0

    media = soma / quantidade

    return media


valores = [20, 50, 80, 10, 100, 60, 25]

limite = float(input("Digite o limite: R$ "))

resultado = media_acima_limite(valores, limite)

print("Média:", resultado)
