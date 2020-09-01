import kivy
from kivy.app import App
from kivy.lang import Builder
kivy.require("1.9.1")

code = """
BoxLayout:
	Button:
		text: "1"
	Button:
		text: "2"

"""


class Estudo6App(App):
	def build(self):
		return Builder.load_string(code)


janela = Estudo6App()
janela.run()
