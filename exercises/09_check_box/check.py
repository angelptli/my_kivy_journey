from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

# Designate our .kv design file
Builder.load_file('check.kv')


class MyLayout(Widget):
    toppings_list = []
    def checkbox_click(self, instance, checked_box, topping):
        """Update info displayed on the screen on a pizza order according
        to the user's clicks on check boxes.

        :param instance: CheckBox object's memory address
        :type instance: class: 'checkbox.Checkbox' object, optional
        :param checked_box: `True` if user checked a box, and `False` if
            user unchecked a box
        :type checked_box: bool
        :param topping: The selected topping(s) chosen by the user
        :type topping: str
        """
        # Default pizza price
        price = 10.00
        toppings = MyLayout.toppings_list

        if checked_box == True:
            ## Display selected topping
            # self.ids.output_label.text = f'You Selected: {topping}'

            ## List checked toppings with brackets
            # MyLayout.checks.append(topping)
            # self.ids.output_label.text = f'You Selected: {MyLayout.checks}'

            toppings.append(topping)

            # Pepperoni and sausage each add $1 to total price
            if 'Pepperoni' in toppings:
                price += 1
            if 'Sausage' in toppings:
                price += 1
            
            # Display selected toppings and total price
            self.ids.select_toppings.text = ',  '.join(toppings)
            self.ids.order_pricing.text = f'${price:.2f}'
            
        else:
            toppings.remove(topping)

            # Pepperoni and sausage each add $1 to total price
            if 'Pepperoni' in toppings:
                price += 1
            if 'Sausage' in toppings:
                price += 1

            # Display selected toppings and total price
            self.ids.select_toppings.text = ',  '.join(toppings)
            self.ids.order_pricing.text = f'${price:.2f}'


class MakeYourPizzaApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    MakeYourPizzaApp().run()
