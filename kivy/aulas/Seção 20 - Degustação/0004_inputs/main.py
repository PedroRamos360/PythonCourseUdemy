# coding: utf-8
# author: Pedro Henrique Warken Ramos
from kivy.app import App
from kivy.uix.textinput import TextInput


def build():
	data = TextInput()
	data.text = 'Componente TextInput'
	return data


janela = App()
janela.build = build
janela.run()