def verificarString(valor):
    if type(valor) is str:
        print("{} é uma string".format(valor))
    else:
        print("{} não é uma string".format(valor))


valor1 = "banana"
valor2 = 9

verificarString(valor1)
verificarString(valor2)
