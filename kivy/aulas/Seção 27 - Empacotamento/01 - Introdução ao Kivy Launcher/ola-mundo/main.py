from kivy.app import App
from kivy.uix.button import Button
import kivy
kivy.require("1.9.1")


class OlaMundoApp(App):
	def build(self):
		return Button(text='Funcionou', size_hint=(.2, .2), pos_hint={"center_x": .5, "center_y": .5})


if __name__ == '__main__':
	OlaMundoApp().run()