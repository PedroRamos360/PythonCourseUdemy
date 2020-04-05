def multiplicar(lista):
    produto = 1
    for number in range(len(lista)):
        produto *= lista[number]

    return produto


lista1 = 1, 3, 5, 7, 9
lista2 = 2, 2, 2, 2, 2
lista3 = 2, 4, 6, 8, 10

print(multiplicar(lista1))
print(multiplicar(lista2))
print(multiplicar(lista3))