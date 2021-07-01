# File: box.py
# Desc: Accomodate python code for box customization exercise.

import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

# Load Kv file with whatever path or filename. This looks only for whatever.kv.
Builder.load_file('box.kv')


class MyLayout(Widget):
    pass


class NiceApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    NiceApp().run()
