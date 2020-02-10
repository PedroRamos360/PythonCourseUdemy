dias = int(input("dias: "))
horas = int(input("horas: "))
minutos = int(input("minutos: "))
segundos = int(input("segundos: "))

diasS = dias * 24 * 3600
horasS = horas * 3600
minutosS = minutos * 60

print("Tempo em segundos: {}".format(diasS + horasS + minutosS + segundos))