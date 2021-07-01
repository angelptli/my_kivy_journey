# File: calc.py
# Desc: Create functional calculator app.

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

# Set the app size
Window.size = (500, 700)

# Designate our .kv design file
Builder.load_file('calc.kv')

class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = '0'

    # Create a button pressing function
    def button_press(self, button):
        # Create a variable that contains whatever was in the text box already
        prior = self.ids.calc_input.text

        # Test for error first
        if "Error" in prior:
            prior = ''

        # Determine if 0 is sitting there
        if prior == "0":
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text = f'{prior}{button}'

    # Create function to remove last character in text box
    def remove(self):
        prior = self.ids.calc_input.text
        # Remove the last item in the text box
        prior = prior[:-1]
        # Output back to the textbox
        self.ids.calc_input.text = prior

    # Create function to make text box positive or negative
    def pos_neg(self):
        prior = self.ids.calc_input.text
        # Test to see if there's a - sign already
        if "-" in prior:
            self.ids.calc_input.text = f'{prior.replace("-", "")}'
        else:
            self.ids.calc_input.text = f'-{prior}'

    # Create decimal function
    def dot(self):
        prior = self.ids.calc_input.text

        # Split out text box by +
        num_list = prior.split("+")

        if "+" in prior and "." not in num_list[-1]:
            # Add a decimal to the end of the text
            prior = f'{prior}.'
            # Output back to the text box
            self.ids.calc_input.text = prior
        elif "." in prior:
            pass
        else:
            # Add a decimal to the end of the text
            prior = f'{prior}.'
            # Output back to the text box
            self.ids.calc_input.text = prior

    # Create addition function
    def math_sign(self, sign):
        # Create a variable that contains whatever was in the text box already
        prior = self.ids.calc_input.text

        # Slap a plus sign to the text box
        self.ids.calc_input.text = f'{prior}{sign}'

    # Create equals to function
    def equals(self):
        # Create a variable that contains whatever was in the text box already
        prior = self.ids.calc_input.text

        # Error Handling
        try:
            # Evaluate the math from the text box
            answer = eval(prior)
            # Output the answer
            self.ids.calc_input.text = str(answer)
        except:
            self.ids.calc_input.text = "Error"

        '''
        # Addition
        if "+" in prior:
            num_list = prior.split("+")
            answer = 0.0
            
            # Loop through our list
            for number in num_list:
                answer += float(number)

            # Print the answer in the text box
            self.ids.calc_input.text = str(answer)
        '''

class CalculatorApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    CalculatorApp().run()
