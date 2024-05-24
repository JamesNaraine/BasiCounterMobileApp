from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class CounterApp(App):
    def build(self):
        self.counter = 0

        self.layout = BoxLayout(orientation='vertical')

        self.counter_label = Label(text=str(self.counter), font_size='40sp')
        self.layout.add_widget(self.counter_label)

        self.increment_button = Button(text='count', font_size='30sp', on_press=self.increment_counter)
        self.layout.add_widget(self.increment_button)

        self.reset_button = Button(text='Reset', font_size='30sp', on_press=self.reset_counter)
        self.layout.add_widget(self.reset_button)

        return self.layout

    def increment_counter(self, instance):
        self.counter += 1
        self.counter_label.text = str(self.counter)

    def reset_counter(self, instance):
        self.counter = 0
        self.counter_label.text = str(self.counter)

if __name__ == '__main__':
    CounterApp().run()
