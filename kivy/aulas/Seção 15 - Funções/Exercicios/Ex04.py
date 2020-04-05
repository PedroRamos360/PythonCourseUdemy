def organizar(*params):
    lista = list()
    for i in range(len(params)):
        lista.append(int(params[i]))

    lista.sort()
    print(lista)

    soma = 0
    for number in range(len(lista)):
        soma += lista[number]

    print(soma / len(lista))


organizar(input(), input(), input())



