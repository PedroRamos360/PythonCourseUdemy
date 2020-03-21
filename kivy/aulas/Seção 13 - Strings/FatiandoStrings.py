s = "Para Python, toda String é uma lista imutável"

print(s)
print(s[0])

print(type(s[0])) # No python não existem caracteres apenas listas

# lista[Start:Stop:Step]
# Mesmo que com listas

print(s[5:11]) # 5 ao 11
print(s[5:]) # 5 até a última
print(s[::-1]) # inverte a lista
print(s[::5]) # pula de 5 em 5
