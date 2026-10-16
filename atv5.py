
def somar_pares(numeros):
    soma = 0

    for numero in numeros:
        if numero % 2 == 0:
            soma += numero

    return soma


numeros = [10, 7, 4, 9, 20, 3, 6, 11]

resultado = somar_pares(numeros)

print("Soma dos pares:", resultado)
