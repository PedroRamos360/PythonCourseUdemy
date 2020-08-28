import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

kivy.require('1.9.1')


class Tela1(BoxLayout):
	@staticmethod
	def on_press_bt():
		janela.root_window.remove_widget(janela.root)
		janela.root_window.add_widget(Tela2())


class Tela2(BoxLayout):
	@staticmethod
	def on_press_bt():
		janela.root_window.remove_widget(janela.root)
		janela.root_window.add_widget(Tela1())


class KVvsPY2(App):
	# é possível implementar essa classe através do arquivo .kv
	# só é necessário declarar qual tela é a root
	# Então para substituir esse código seria usado "Tela1:"
	def build(self):
		return Tela1()


janela = KVvsPY2()
janela.run()