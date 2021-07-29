from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

# Designate our .kv design file
Builder.load_file('menu.kv')


class MyLayout(Widget):
    def selected(self, filename):
        try:
            self.ids.your_image.source = filename[0]
            print(filename[0])
        except:
            pass


class YourImagesApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    YourImagesApp().run()
