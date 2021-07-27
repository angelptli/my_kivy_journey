from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window

# Set window size
Window.size = (380, 600)

# Designate our .kv design file
Builder.load_file('round_buttons.kv')


class MyLayout(Widget):
    pass


class GreeterChanApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return MyLayout()

if __name__ == '__main__':
    GreeterChanApp().run()
