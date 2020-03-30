def pessoa(nome, sobrenome, idade):
    print(nome)
    print(sobrenome)
    print(idade)

# desempacotamento de listas/tuplas
lista = ["eXcript", "Brasil", 20]
# pessoa(tupla[0], tupla[1], tupla[2]) sem desempacotamento
pessoa(*lista) # com desempacotamento

# desempacotamento de dicionários
d = {'nome': "eXcript", 'sobrenome': "Brasil", 'idade': 20}
pessoa(**d)