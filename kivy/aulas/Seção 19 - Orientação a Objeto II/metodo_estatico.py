class MEstaticos:
	@staticmethod
	def func1():
		print('func1()')

	@staticmethod
	def func2(x, y):
		print('Função "func2" invocada. \nParams=({}, {})'.format(x, y))

	@staticmethod
	def func3(a, b, c):
		info = """
		Nome da função: {nome}
		Quantidade de Args: {quantidade}
		Args: {args}
		"""
		info = info.format(
			nome=MEstaticos.func3.__name__, # Pega o nome da função
			quantidade=MEstaticos.func3.__code__.co_argcount, # Pega o número de variáveis da função
			args=MEstaticos.func3.__code__.co_varnames # Pega o nome das variáveis
		)
		print(info)

	# func1 = staticmethod(func1)
	# func2 = staticmethod(func2)
	# func3 = staticmethod(func3)


me = MEstaticos()
MEstaticos.func1()
me.func1()
me.func2(20, 30)
me.func3(5, 10, 15)