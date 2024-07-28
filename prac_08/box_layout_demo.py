from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout


def handle_greet():
    print("Greet button pressed!")


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root


BoxLayoutDemo().run()
