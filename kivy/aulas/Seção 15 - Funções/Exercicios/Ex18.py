def identificar_primos(*params):
    numeros = []
    for param in params:
        numeros.append(int(param))
    nao_primos = []
    for numero in numeros: # 1, 2, 3, 4, 5, 6, 7
        index = numero
        if numero == 0 or numero == 1:
            nao_primos.append(numero)
        while index > 1:
            index -= 1
            if index == 1:
                break
            if numero % index == 0:
                nao_primos.append(numero)
                break

    for i in range(len(nao_primos)):
        numeros.remove(nao_primos[i])

    return numeros


inputs = input().split(' ')

print(identificar_primos(*inputs))