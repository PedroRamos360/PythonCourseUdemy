def verficar_classe(numero):
    classe = ""
    if numero >= 0 and numero <= 127:
        classe = "A"

    if numero > 127 and numero <= 191:
        classe = "B"

    if numero > 191 and numero <= 223:
        classe = "C"

    if numero > 223 and numero <= 239:
        classe = "D"

    if numero > 240:
        classe = "E"

    return classe


num = int(input())
print("classe", verficar_classe(num))