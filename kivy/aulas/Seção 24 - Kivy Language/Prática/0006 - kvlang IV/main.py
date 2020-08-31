import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

kivy.require("1.9.1")


class Tela(BoxLayout):
	a = 0
	b = 0
	def click(self):
		print(self.a, self.b)
		self.a += 1
		self.b += 2
		self.ids.lb1.text = str(self.a)
		self.ids.lb2.text = str(self.b)


class Estudo4App(App):
	pass


janela = Estudo4App()
janela.run()
