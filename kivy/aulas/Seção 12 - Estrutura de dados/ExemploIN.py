a = 10
b = 25
c = 66

x = int(input())

if x in [a, b, c]:
    print("Está contido")
else:
    print("Não está contido")

cores = ["azul", "amarelo", "branco", "vermelho"]

while True:
    cor = input()

    if cor == "0":
        break
    if cor in cores:
        print("Está contida")
    else:
        print("Não está contida")