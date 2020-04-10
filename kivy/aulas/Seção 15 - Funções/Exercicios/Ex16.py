def contador_letras(string):
    caracteres = []
    for caracter in string:
        caracteres.append(caracter)
    minusculas = 0
    maisculas = 0

    for caracter in caracteres:
        if caracter.islower():
            minusculas += 1
        elif caracter.isupper():
            maisculas += 1
    return maisculas, minusculas


maiusculas, minusculas = contador_letras('Pedro Henrique Warken Ramos')

print(maiusculas, minusculas)