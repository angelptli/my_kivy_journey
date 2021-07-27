# File: float_layout.py
# Desc: Accommodate code for button float layout exercise for Kv file.

import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
# from kivy.uix.floatlayout import FloatLayout

Builder.load_file('float_layout.kv')


class MyLayout(Widget):
    pass


class NiceApp(App):
    
    def build(self):
        # Can use either/or Kv canvas.before
        Window.clearcolor = (240/255.0, 240/255.0, 240/255.0, 1)
        return MyLayout()


if __name__ == '__main__':
    NiceApp().run()
