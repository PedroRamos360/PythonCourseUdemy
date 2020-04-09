def verificar_intervalo(inicio, fim, numero):
    intervalo = []
    while inicio <= fim:
        intervalo.append(inicio)
        inicio += 1

    if numero in intervalo:
        return True
    else:
        return False


print(verificar_intervalo(int(input()), int(input()), int(input())))
