from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
# from kivy.uix.togglebutton import ToggleButton

# Set window size
Window.size = (320, 568)

# Designate our .kv design file
Builder.load_file('my_planner.kv')


class MyLayout(Widget):
    pass


class MyPlannerApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return MyLayout()

if __name__ == '__main__':
    MyPlannerApp().run()
