from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

# Designate our .kv design file
Builder.load_file('accordion.kv')


class MyLayout(Widget):
    pass


class PanelApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    PanelApp().run()
