from kivy.app import App
from kivy.lang import Builder


def handle_greet():
    print('greet')


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root


BoxLayoutDemo().run()
