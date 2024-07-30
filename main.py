from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.metrics import Metrics

class MainLayout(Widget):
	pass

class MyApp(App):
	def window_sizing(self):
		Window.size = (450, 800)

	def build(self):
		self.window_sizing()

		# screen_density_dpi = Metrics.dpi
		# print(f"Screen density: {screen_density_dpi} dpi")

		return MainLayout()

if __name__ == "__main__":
	app = MyApp()
	app.run()

