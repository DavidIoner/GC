import pandas as pd
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.floatlayout import FloatLayout


class Demo(FloatLayout):
    pass


class Main(App):
    def build(self):
        return Demo()


if __name__ == "__main__":
    Builder.load_file(r"interface.kv")
    Main().run()
