l = list('abc')

# append para adicionar elementos
l.append('d')
print(l)

# insert para adicionar elementos em localizações específicas
l.insert(0, '0')
print(l)

# alterar items
l[0] = 'a0'
print(l)

# clear para tirar todos elementos de uma lista
l.clear()
l = list('abcde')

# pop para deletar um item
print(l.pop(-1))
print(l)

# del para excluir um intervalo de items em uma lista
del(l[1:-1])
print(l)