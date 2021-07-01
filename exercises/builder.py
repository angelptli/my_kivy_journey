# File: builder.py
# Desc: Make Kivy look for a specifically named Kv file to load.

import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

# Load Kv file with whatever path or filename. This looks only for whatever.kv.
Builder.load_file('whatever.kv')
# # Redundant alternative way (DON'T DO THIS)
# Builder.load_file("""Paste everything from whatever.kv here""")


class MyGridLayout(Widget):
    # kvlang customize these objects
    name = ObjectProperty(None)
    pizza = ObjectProperty(None)
    color = ObjectProperty(None)

    def press(self):
        """Create variables of the input boxes.
        """
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text

        # Print it on the app screen
        # self.add_widget(Label(text=f'Hi {name}, you like {pizza} pizza, '
        #                            f'and your favorite color is {color}.'))

        # Print into terminal
        print(f'Hi {name}, you like {pizza} pizza, '
              f'and your favorite color is {color}.')

        # Clear the input boxes
        self.name.text = ""
        self.pizza.text = ""
        self.color.text = ""


class NiceApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    NiceApp().run()
