from kivy.lang import Builder
Builder.load_file('ui/layout.kv')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout

import _global_
from features import *

def main():
	word_frequency.catch()
	print _global_.session_info

class View(GridLayout):
	pass

class BookAnalytics(App):
	def build(self):
		main()
		return View()

if __name__ == "__main__":
	BookAnalytics().run()