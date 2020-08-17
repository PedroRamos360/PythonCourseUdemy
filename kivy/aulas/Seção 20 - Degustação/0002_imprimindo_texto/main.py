# coding: utf-8
from kivy.app import App
from kivy.uix.label import Label


def build():
	lb = Label()
	lb.text = "Curso de Python e Kivy"
	lb.bold = True
	lb.font_size = 50
	lb.pos = (0, 200)
	return lb


app = App()
app.build = build
app.run()

