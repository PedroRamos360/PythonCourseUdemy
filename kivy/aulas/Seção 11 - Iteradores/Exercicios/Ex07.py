def verificar_primo(numero):
    divisores = []
    teste = numero
    while teste > 0:
        if numero % teste == 0:
            divisores.append(teste)

        teste -= 1

    if len(divisores) == 2:
        return True
    else:
        return False


inicio, fim = [int(i) for i in input().split()]

while inicio <= fim:
    if verificar_primo(inicio):
        print(inicio)

    inicio += 1