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


n = 1

while n <= 100:
    if verificar_primo(n):
        print(n)

    n += 1

