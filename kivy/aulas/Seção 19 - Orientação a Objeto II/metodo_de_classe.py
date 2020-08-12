class Bichos:
	quantidade_bichos = 0
	def __init__(self):
		self.add_bicho()

	def __del__(self):
		self.del_bicho()
		if self.quantidade_bichos == 0:
			print("Todos bichos foram mortos!")

	@classmethod
	def add_bicho(cls):
		cls.quantidade_bichos += 1

	@classmethod
	def del_bicho(cls):
		cls.quantidade_bichos -= 1

	# add_bicho = classmethod(add_bicho)
	# del_bicho = classmethod(del_bicho)


b1 = Bichos()
print(Bichos.quantidade_bichos)
b2 = Bichos()
print(Bichos.quantidade_bichos)
b3 = Bichos()
print(Bichos.quantidade_bichos)

del(b1)
print(Bichos.quantidade_bichos)
del(b2)
print(Bichos.quantidade_bichos)
del(b3)
print(Bichos.quantidade_bichos)