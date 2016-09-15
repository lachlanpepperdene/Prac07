from kivy.app import App
from kivy.lang import Builder

miles_conversion = 1.60934


class MilesConverterApp(App):

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_m_km.kv')
        return self.root

    def calculations(self):
        value = self.get_validated_miles()
        result = value * miles_conversion
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        value = self.get_validated_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.calculations()
        return self.root

    def get_validated_miles(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0

MilesConverterApp().run()
