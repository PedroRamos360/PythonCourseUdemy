import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

kivy.require("1.9.1")


def func_self(x):
	print("func_self")


Button.func_self = func_self


class Tela(BoxLayout):
	a = 0
	b = 0
	@staticmethod
	def func_root():
		print("func_root")


class Estudo5App(App):
	@staticmethod
	def func_app():
		print("func_app")


janela = Estudo5App()
janela.run()
