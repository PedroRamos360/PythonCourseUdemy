valor = input()

vogais = ["a", "e", "i", "o", "u"]

for i in range(len(vogais)):
    if valor == vogais[i]:
        print("{} é uma vogal".format(valor))
        break
    elif i == 4:
        print("{} não é uma vogal".format(valor))
