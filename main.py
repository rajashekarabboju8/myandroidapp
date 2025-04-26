from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class MyApp(App):
    def build(self):
        # Create a BoxLayout
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Create a Label
        self.label = Label(text="Hello, Kivy!")

        # Create a Button
        button = Button(text="Click me!")
        button.bind(on_press=self.on_button_click)

        # Add widgets to the layout
        layout.add_widget(self.label)
        layout.add_widget(button)

        return layout

    def on_button_click(self, instance):
        self.label.text = "Button clicked!"

if __name__ == '__main__':
    MyApp().run()