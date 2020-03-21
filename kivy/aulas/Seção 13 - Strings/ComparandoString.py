# baseado na Tabela ASCII
print('a' > "X") # True
print('a' > '1') # True
print('a' > '9') # True

print(chr(100)) # Retorna a String respectivo ao código
print(ord("d")) # Retorna o código respectivo a String

for c in range(123):
    print(str(c) + ' - ' + chr(c))
