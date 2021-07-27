# File: images.py
# Desc: Accomodate python code for image adding exercise.

import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
# from kivy.uix.image import Image

Builder.load_file('images.kv')


class MyLayout(Widget):
    pass


class NiceApp(App):
    
    def build(self):
        # Can use either/or Kv canvas.before
        Window.clearcolor = (240/255.0, 240/255.0, 240/255.0, 1)
        return MyLayout()


if __name__ == '__main__':
    NiceApp().run()
