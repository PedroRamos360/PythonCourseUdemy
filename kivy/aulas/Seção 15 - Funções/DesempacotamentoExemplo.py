lista = [11, 10, 12]
tupla = (11, 10, 12)


def func(a, b, c):
    print(a, b, c)


# Ordenar lista
lista.sort()
func(*lista)

# Ordenar tupla
tupla = [*tupla] # para desempacotar tupla
tupla.sort()
func(*tupla)


# Zip e ordenar dicionário
lista.reverse()
func(**dict(zip(('c', 'b', 'a'), lista)))



