# File: design.py
# Desc: Move customization code into separate kv file.

import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


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


class MyApp(App):
    
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    # Run MyApp
    MyApp().run()
