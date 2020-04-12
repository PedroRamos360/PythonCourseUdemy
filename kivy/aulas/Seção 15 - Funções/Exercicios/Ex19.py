def pares(numeros):
    pares = []
    for numero in numeros:
        if int(numero) % 2 == 0:
            pares.append(numero)
    return pares


print(pares(input().split(' ')))