from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
# Only need this if doing all markup from python file
# from kivy.uix.slider import Slider

# Designate our .kv design file
Builder.load_file('slider.kv')


class MyLayout(Widget):
    def slide_it(self, *args):
        # print(args[1])
        self.slide_text.text = str(int(args[1]))
        self.slide_text.font_size = str(int(args[1]) * 5)


class SlideItApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    SlideItApp().run()
