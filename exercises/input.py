# File: input.py
# Desc: Use user input to return a sentence about the input.

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGridLayout(GridLayout):
    # Initialize infinite keywords **kwargs

    def __init__(self, **kwargs):
        # Call grid layout constructor super
        super(MyGridLayout, self).__init__(**kwargs)

        # Set columns
        self.cols = 1

        # Add widgets below:
        # Indicate widget's text
        self.add_widget(Label(text="Name: "))
        # Add input box next to the above widget and turn on multiline
        self.name = TextInput(multiline=True)
        # Finish adding the widget
        self.add_widget(self.name)

        self.add_widget(Label(text="Favorite Pizza: "))
        self.pizza = TextInput(multiline=False)
        self.add_widget(self.pizza)

        self.add_widget(Label(text="Favorite Color: "))
        self.color = TextInput(multiline=False)
        self.add_widget(self.color)

        # Create a submit button
        self.submit = Button(text="Submit", font_size=32)
        # Bind the button to make it clickable
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self, instance):
        """Create variables of the input boxes.
        """
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text

        # print(f'Hi {name}, you like {pizza} pizza, '
        #       f'and your favorite color is {color}.')

        # Print it on the app screen
        self.add_widget(Label(text=f'Hi {name}, you like {pizza} pizza, '
                                   f'and your favorite color is {color}.'))

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
