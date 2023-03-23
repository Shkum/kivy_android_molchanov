from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class Container(BoxLayout):
    pass


class MyApp(App):
    def build(self):
        # bl = BoxLayout()
        # button1 = Button(text='Hello')
        # button2 = Button(text='World')
        # bl.add_widget(button1)
        # bl.add_widget(button2)
        return Container()


if __name__ == '__main__':
    MyApp().run()
