inicio, fim = [int(i) for i in input().split()]

n1, n2, n3 = [int(i) for i in input().split()]

numerosIntervalo = []

while inicio <= fim:
   numerosIntervalo.append(inicio)
   inicio += 1

numerosIntervalo.remove(n1)
numerosIntervalo.remove(n2)
numerosIntervalo.remove(n3)

print(numerosIntervalo)