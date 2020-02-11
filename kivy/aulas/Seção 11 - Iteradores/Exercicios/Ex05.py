n = 1
lista = []

while n <= 100:
    if n % 2 == 0:
        lista.append(n)
        n += 2
    else:
        n += 1

print(len(lista))