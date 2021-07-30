from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

# Designate our .kv design file
Builder.load_file('radio.kv')


class MyLayout(Widget):
    def checkbox_click(self, instance, checked_button, pineapple_pieces):
        """Update info displayed on the screen on a pizza order according
        to the user's clicks on radio buttons.

        :param instance: CheckBox object's memory address
        :type instance: class: 'checkbox.Checkbox' object, optional
        :param checked_button: `True` if user checked a box, and `False` if
            user unchecked a box
        :type checked_button: bool
        :param pieces: The selected topping(s) chosen by the user
        :type pieces: str
        """
        # Default pizza price
        price = 10.00

        if checked_button == True:
            # 5 pieces = $1.50, 10 pieces = $2.00
            if '5 pieces' == pineapple_pieces:
                price += 1.5
            if '10 pieces' == pineapple_pieces:
                price += 2
            
            # Display selected option and total price
            self.ids.select_pieces.text = pineapple_pieces
            self.ids.order_pricing.text = f'${price:.2f}'


class PineapplePizzaApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    PineapplePizzaApp().run()
