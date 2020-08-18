# coding: utf-8
# author: Pedro Henrique Warken Ramos
from kivy.app import App
from kivy.uix.label import Label
# Criação de um app com orientação a objeto => forma mais correta


# extende a classe App
class MeuPrograma(App):
	def build(self):
		label = Label()
		return label


MeuPrograma().run()