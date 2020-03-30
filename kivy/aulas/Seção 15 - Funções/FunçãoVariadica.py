# Funções variádicas são funções que recebem um número indetermindado de parâmetros
# * lista
# ** dicionário


def lista_quadrado(*lista):
    lista_quadrados = []
    for i in range(len(lista)):
        quadrado = lista[i]**2
        lista_quadrados.append(quadrado)

    print(lista_quadrados)


lista_quadrado(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


# def dicionario_quadrado(**dicionario):
#     valores_quadrados = []
#     valores = dicionario.values()
#     chaves = dicionario.keys()
#     for i in range(len(dicionario)):
#         quadrado = int(valores[])
#         valores_quadrados.append(quadrado**2)
#
#     print(valores_quadrados)
#
#
# dicionario_quadrado(a=1, b=2, c=3, d=4)

dicionario = {'a': 1, 'b': 2}
print(dicionario.values())
print(dicionario.keys())
valores = []
for i in range(len(dicionario)):
    valores.append(dicionario.values())

print(valores)




