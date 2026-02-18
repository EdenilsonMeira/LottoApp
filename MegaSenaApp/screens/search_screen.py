from kivy.uix.screenmanager import Screen


class SearchScreen(Screen):
    
    def text_display_search(self):
        self.ids.result_label.text = "Números pesquisados se baseiam \n " \
        "no período de Nov/1996 a Fev/2026"