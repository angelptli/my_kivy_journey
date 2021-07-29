from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

# Designate our .kv design file
Builder.load_file('carousel.kv')


class MyLayout(Widget):
    pass


class ImageScrollApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    ImageScrollApp().run()
