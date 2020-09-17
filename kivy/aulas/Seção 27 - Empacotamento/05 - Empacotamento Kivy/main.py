from kivy.app import App
from kivy.uix.button import Button


class PyInstallerApp(App):
	def build(self):
		return Button(text="PyInstaller")


if __name__ == '__main__':
	PyInstallerApp().run()