def fatorial(numero):
    index = numero
    while index > 1:
        index -= 1
        numero *= index

    return numero


print(fatorial(int(input())))