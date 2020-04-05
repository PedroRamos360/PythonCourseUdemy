def soma(lista):
    soma = 0
    for number in range(len(lista)):
        soma += lista[number]

    return soma


lista1 = 1, 2, 3, 4, 5
lista2 = 6, 0, 1, 17, 1
lista3 = 1, 3, 5, 7, 9

print(soma(lista1))
print(soma(lista2))
print(soma(lista3))

