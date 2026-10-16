
def calcular_media(notas):
    soma = 0

    for nota in notas:
        soma += nota

    media = soma / len(notas)

    return media


def contar_acima_media(notas, media):
    quantidade = 0

    for nota in notas:
        if nota > media:
            quantidade += 1

    return quantidade


notas = [7.5, 5.0, 8.5, 6.0, 9.0, 4.5, 7.0]

media = calcular_media(notas)
quantidade = contar_acima_media(notas, media)

print("Média da turma:", media)
print("Notas acima da média:", quantidade)
