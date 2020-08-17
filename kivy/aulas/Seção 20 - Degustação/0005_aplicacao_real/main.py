# coding: utf-8
# author: Pedro Henrique Warken Ramos
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window


def click():
	print(ed.text)


def build():
	layout = FloatLayout()

	global ed
	ed = TextInput(text="eXcript")
	# Para não ocupar a tela inteira
	ed.size_hint = None, None
	ed.height = 300
	ed.width = 400
	ed.x = 100
	ed.y = 250

	button = Button(text="Enviar")
	button.on_press = click
	button.size_hint = None, None
	button.height = 50
	button.width = 200
	button.y = 150
	button.x = 200

	layout.add_widget(ed)
	layout.add_widget(button)

	return layout


janela = App()
janela.title = "eXcript"

Window.size = 600, 600

janela.build = build
janela.run()