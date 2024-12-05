"""
CP1404/CP5632 Practical
Kivy GUI program to square a number
Lindsay Ward, IT@JCU
Started 13/10/2015
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Lindsay Ward'


class SquareNumberApp(App):
    """ SquareNumberApp is a Kivy App for squaring a number """
    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (400, 300)
        self.title = "Square Number"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self, value):
        """ handle calculation (could be button press or other call), output result to label widget """
        try:
            result = float(value) ** 2
            self.root.ids.output_label.text = str(result)
        except ValueError:
            pass

    def handle_up(self):
        """ handle up button press, increment the input number by 1 """
        try:
            value = float(self.root.ids.input_number.text)
            value += 1
            self.root.ids.input_number.text = str(value)
        except ValueError:
            pass

    def handle_down(self):
        """ handle down button press, decrement the input number by 1 """
        try:
            value = float(self.root.ids.input_number.text)
            value -= 1
            self.root.ids.input_number.text = str(value)
        except ValueError:
            pass


SquareNumberApp().run()

