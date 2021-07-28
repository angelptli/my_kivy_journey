# File: bg.py
# Desc: 

import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window

Builder.load_file('bg.kv')


class MyLayout(Widget):
    pass


class NiceApp(App):
    
    def build(self):
        # Can use either/or Kv canvas.before
        Window.clearcolor = (0.7, 0, 0.2, 1)
        return MyLayout()


if __name__ == '__main__':
    NiceApp().run()
