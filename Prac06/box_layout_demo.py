from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        print("Successful")
        self.root.ids.output_label.text = "Good day to you " + self.root.ids.input_name.text

    def handle_clear(self):
        self.root.ids.output_name.text = ""
        return self.root


BoxLayoutDemo().run()