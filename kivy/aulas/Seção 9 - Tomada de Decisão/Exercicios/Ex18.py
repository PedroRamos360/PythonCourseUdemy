data = input()
listaData = data.split("/")

if data.count("/") != 2 or len(listaData) < 3:
    print("Data inválida")
elif len(listaData[0]) != 2 or len(listaData[1]) != 2:
    print("Data inválida")
else:
    print("Data válida")


