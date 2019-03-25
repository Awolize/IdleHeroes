from kivy.app import App
from kivy.uix.button import *
from kivy.uix.gridlayout import *
from kivy.config import Config

class ButtonLayout(GridLayout):
    def __init__(self, **kwargs):
        
        super(ButtonLayout, self).__init__(**kwargs)
        self.cols = 3

        self.add_widget(Button(text="1", on_press=lambda a: btn1_callback()))

        self.add_widget(Button(text="2", on_press=lambda a: btn1_callback()))

        self.add_widget(Button(text="3", on_press=lambda a: btn1_callback()))

        self.add_widget(Button(text="4", on_press=lambda a: btn1_callback()))

class SampleApp(App):
    def build(self):
        return ButtonLayout()


if __name__ == '__main__':
    Config.set('graphics', 'width', '320')
    Config.set('graphics', 'height', '180')
    SampleApp().run()