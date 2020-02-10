def verificarInteiro(numero):
    if numero == int(numero):
        print("{} é inteiro".format(numero))
    else:
        print("{} não é inteiro".format(numero))


n = float(input())

verificarInteiro(n)
