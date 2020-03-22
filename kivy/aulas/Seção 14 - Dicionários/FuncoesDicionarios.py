tel = {
    998438027: "Pedro Ramos",
    37201332: "Casa",
    981599231: "Sergio",
    981148427: "Estefânia"
}

print(tel)
print(len(tel))

# Deletar elementos dicionário
del(tel[37201332])
print(tel)

# Retorna os telefones das pessoas (chaves)
print(tel.keys())

# Retorna os nomes das pessoas (valores)
print(tel.values())

# popitem
for i in range(len(tel)):
    print(tel.popitem())
    print(tel)

tel = {
    998438027: "Pedro Ramos",
    37201332: "Casa",
    981599231: "Sergio",
    981148427: "Estefânia"
}

print(998438027 in tel)
print(991852341 in tel)

tel2 = {999999999: 'teste1', 888888888: 'teste2'}

# Mesclar dicionários
tel.update(tel2)
print(tel)

# Usar uma tupla como chave
tel[(10, 10, 10)] = 'eXcript'
print(tel)