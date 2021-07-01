# File: inherit.py
# Desc: Accommodate python code for inherit colors exercise.

import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

# Load Kv file with whatever path or filename. This looks only for whatever.kv.
Builder.load_file('inherit.kv')


class MyLayout(Widget):
    pass


class NiceApp(App):
    """Display Hello World in the app.

    :param App: Contains the build() method
    :type App: class
    """

    def build(self):
        """Display app with the MyLayout widgets.
        """
        # Return a label
        return MyLayout()


if __name__ == '__main__':
    # Run MyApp
    NiceApp().run()
