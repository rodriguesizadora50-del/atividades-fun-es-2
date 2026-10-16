
def calcular_situacao(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3

    if media < 5:
        return "Reprovado"
    elif media < 7:
        return "Recuperação"
    else:
        return "Aprovado"


nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))

media = (nota1 + nota2 + nota3) / 3
situacao = calcular_situacao(nota1, nota2, nota3)

print("Média:", media)
print("Situação:", situacao)
