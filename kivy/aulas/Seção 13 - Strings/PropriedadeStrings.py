# Comprimento Strings
s = "Lista de Caracteres"
print(len(s))

# Alterar strings
print(s[6])
# s[6] = 'x'  retorna erro
print(s.replace('d', 'x'))
lista = s.split(" ") # separa entre palavras
print(lista[0] + " " + lista[2])
# ou
print(s.replace("de", ""))