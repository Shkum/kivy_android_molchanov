from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window

from kivymd.app import MDApp

# Window.size = (720, 1280) # * 1.5 - below
Window.size = (480, 853)

from kivy.config import Config

Config.set('kivy', 'keyboard_mode', 'systemanddock')

from kivymd.theming import ThemeManager


def get_ingridients(m):
    nitro = str(10 * m / 1000)
    salt = str(15 * m / 1000)
    starts = str(0.5 * m / 1000)
    sugars = str(5 * m / 1000)
    salting_time = str(round(m / 500 * 2))

    return {
        'nitro': nitro,
        'salt': salt,
        'starts': starts,
        'sugars': sugars,
        'time': salting_time
    }


class Container(GridLayout):

    def calculate(self):
        try:
            mass = int(self.text_input.text)
        except:
            mass = 0

        ingridients = get_ingridients(mass)

        self.salt.text = ingridients.get('salt') + ' + 5'
        self.nitro.text = ingridients.get('nitro')
        self.sugars.text = ingridients.get('sugars')
        self.starts.text = ingridients.get('starts')
        self.time.text = ingridients.get('time')


class My1App(MDApp):
    theme_clc = ThemeManager()
    title = 'Coppa app'

    def build(self):
        self.theme_clc.theme_style = 'Light'
        return Container()


if __name__ == '__main__':
    My1App().run()
