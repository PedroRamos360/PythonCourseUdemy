lista = [1, 2, 8, 5, 15, 3, 6, 8]
soma = 0

print(type(lista))
print(type(["ffa", "hyg"]))

for i in range(len(lista)):
    print(lista[i])

for i in range(len(lista)):
    soma += lista[i]

print(soma)

# Outro jeito de declarar listas:

l1 = list("eXcript") # Um elemento pra cada letra
print(l1)

l2 = list((4, 5, 8))
print(l2)

l3 = list(("eXcript",)) # Um elemento só
# a vírgula é usada para mostrar que os parênteses não são para isolar operações
print(l3)