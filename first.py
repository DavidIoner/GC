import pandas as pd
from kivy.app import App
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.uix.floatlayout import FloatLayout

from uteis import *


class Demo(FloatLayout):
    pass


class Main(App):
    def build(self):
        return Demo()

    """def build(self):
        Window.bind(on_dropfile=self._on_file_drop)
        return

    def _on_file_drop(self, window, file_path):
        print(file_path)
        return"""


if __name__ == "__main__":
    Builder.load_file(r"interface.kv")
    Main().run()
