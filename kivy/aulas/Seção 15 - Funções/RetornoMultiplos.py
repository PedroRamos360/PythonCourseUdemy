a, b = 1, 2


def func(valor1, valor2):
    return valor1*10, valor2*10


a, b = func(a, b)

print(a, b)


def potencia(x):
    quadrado = x**2
    cubo = x**3

    return quadrado, cubo


q, c = potencia(9)

print(q, c)