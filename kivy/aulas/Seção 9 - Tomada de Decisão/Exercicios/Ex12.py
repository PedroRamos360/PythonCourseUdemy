def verficiarDecimal(numero):
    if numero == int(numero):
        print("{} é inteiro".format(numero))
    else:
        print("{} é decimal".format(numero))


n = float(input())

verficiarDecimal(n)

