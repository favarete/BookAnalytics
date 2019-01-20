from kivy.lang import Builder
Builder.load_file('ui/layout.kv')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class View(GridLayout):
	pass

class BookAnalytics(App):
	def build(self):
		return View()

if __name__ == "__main__":
	BookAnalytics().run()