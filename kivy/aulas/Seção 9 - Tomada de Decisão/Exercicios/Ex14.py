n1, n2, n3 = [float(i) for i in input().split()]

numeros = [n1, n2, n3]
numerosEmOrdem = []

for i in range(len(numeros)):
    maior = max(numeros)
    numerosEmOrdem.append(maior)
    numeros.remove(maior)

print(numerosEmOrdem)