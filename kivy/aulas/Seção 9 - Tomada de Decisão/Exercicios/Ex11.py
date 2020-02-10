def verficiarDecimal(numero):
    if type(numero) is float:
        print("{} é decimal".format(numero))
    else:
        print("{} não é decimal".format(numero))


verficiarDecimal(9)
verficiarDecimal("banana")
verficiarDecimal(9.3)
verficiarDecimal(-0.1)

