s = 'iterando strings'
# EXEMPLO 1
for c in s:
    print(c)

# EXEMPLO 2
indice = 0
while indice < len(s):
    print(indice, s[indice])
    indice += 1

# EXEMPLO 3
for key, value in enumerate(s):
    print(key, value)
