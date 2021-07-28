# File: hello.py
# Desc: Display the text "Hello World" in the app.

import kivy
from kivy.app import App
from kivy.uix.label import Label


class MyApp(App):
    """Display Hello World in the app.

    :param App: Contains the build() method
    :type App: class
    """

    def build(self):
        """Initialize a Label that will be the Root Widget of this app.

        :return: Label with the indicated text
        :rtype: MyApp object
        """
        # Return a label
        return Label(text="Hello World")


if __name__ == '__main__':
    # Run MyApp
    MyApp().run()
