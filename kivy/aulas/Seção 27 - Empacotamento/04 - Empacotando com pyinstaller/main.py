class App:
	def __init__(self):
		self.n1 = int(input("Primeiro número: "))
		self.n2 = int(input("Segundo número: "))

	def soma(self):
		return self.n1 + self.n2


app = App()
print(app.soma())
input()

# pyinstaller main.py