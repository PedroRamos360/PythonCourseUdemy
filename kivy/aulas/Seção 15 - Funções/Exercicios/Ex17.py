def lista_sem_repeticao(lista):
    index = 0
    for i in range(len(lista)):
        if lista.count(lista[index]) > 1:
            lista.pop(index)
            index -= 1

        index += 1

    return lista


print(lista_sem_repeticao([1, 2, 3, 3, 3, 3, 4, 5]))
print(lista_sem_repeticao([1, 1, 1, 1]))
print(lista_sem_repeticao([1, 1, 1, 5, 6, 77, 77]))
