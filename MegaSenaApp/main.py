from kivy.core.window import Window
Window.size = (400, 800)

from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder

from screens.main_screen import MainScreen
from screens.search_screen import SearchScreen
from screens.stats_screen import StatsScreen


class WindowManager(ScreenManager):
    pass


class MegaSenaApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.theme_style = "Light"

        Builder.load_file("kv/main.kv")
        Builder.load_file("kv/main_screen.kv")
        Builder.load_file("kv/search_screen.kv")
        Builder.load_file("kv/stats_screen.kv")

        sm = WindowManager()
        sm.add_widget(SearchScreen(name="search"))
        sm.add_widget(MainScreen(name="main"))
        sm.add_widget(StatsScreen(name="stats"))

        return sm


if __name__ == "__main__":
    MegaSenaApp().run()
