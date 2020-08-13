from time import sleep


class Carro:
	ligado = False
	velocidade = 0

	def __init__(self, Marca, AnoDeFabricacao):
		self.marca = Marca
		self.ano_de_fabricacao = AnoDeFabricacao
		if self.ano_de_fabricacao >= 2000:
			self.velocidade_maxima = 200
		else:
			self.velocidade_maxima = 100

	def informacoes_carro(self):
		print("A marca do carro é {} e o ano de fabricação é {}".format(
			self.marca,
			self.ano_de_fabricacao
		))

	def ligar(self):
		if self.ligado:
			print("O carro já está ligado")
		else:
			print("Motor iniciando...")
			sleep(1)
			print("Pronto para sair")
			self.ligado = True

	def parar(self):
		if self.ligado is False:
			print("O carro já está parado")
		else:
			print("Freiando...")
			sleep(1)
			print("Parou")
			self.velocidade = 0
			self.ligado = False

	def acelerar(self):
		if self.ligado:
			if self.velocidade != self.velocidade_maxima:
				self.velocidade += 10
				print("A velocidade é de {}".format(self.velocidade))
			else:
				print("Velocidade máxima atingida")
		else:
			print("O carro está desligado")


carro1 = Carro("Toyota", 2010)

carro1.informacoes_carro()
carro1.ligar()

for i in range(21):
	carro1.acelerar()
	sleep(0.5)

carro1.parar()

carro2 = Carro("Ford", 1990)

carro2.informacoes_carro()
carro2.ligar()

for i in range(11):
	carro2.acelerar()
	sleep(0.5)

carro2.parar()


