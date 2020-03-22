# formas de criar um dicionário
d1 = {}
d2 = dict()
print(type(d1), type(d2))

# adicionar elementos em um dicionario
d1['a'] = 1000
d1['b'] = 2000
d1['c'] = 3000
d1['d'] = 'banana'
d1[10] = 'maçã'
print(d1)
print(d1['b'])

d2 = {1.1: 'teste1', 2.2: 'teste2', 3.3: 'teste3'}
print(d2)

for key in d2:
    print(d2[key])
