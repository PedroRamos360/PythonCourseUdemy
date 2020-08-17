# coding: utf-8
# author: Pedro Henrique Warken Ramos
from kivy.app import App
from kivy.uix.button import Button


def click():
	print("O Botão foi clicado")


def build():
	button = Button()
	button.text = "Click me"
	button.on_press = click
	return button


janela = App()
janela.build = build
janela.run()