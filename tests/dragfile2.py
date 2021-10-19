from kivy.app import App
from kivy.lang import Builder
from kivy.uix.behaviors import DragBehavior
from kivy.uix.label import Label

# You could also put the following in your kv file...
kv = """
<DragLabel>:
    # Define the properties for the DragLabel
    drag_rectangle: self.x, self.y, self.width, self.height
    drag_timeout: 10000000
    drag_distance: 0

FloatLayout:
    # Define the root widget
    DragLabel:
        size_hint: 0.25, 0.2
        text: 'Drag me'
"""


class DragLabel(DragBehavior, Label):
    pass


class TestApp(App):
    def build(self):
        print()
        return Builder.load_string(kv)


TestApp().run()
