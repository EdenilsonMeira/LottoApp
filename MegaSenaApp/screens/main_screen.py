#:import MDCard kivymd.uix.card.MDCard

from kivy.uix.screenmanager import Screen
from kivy.properties import ListProperty
import random



class MainScreen(Screen):
    numbers = ListProperty([8, 17, 23, 31, 42, 49])

    def generate_random(self):
        self.numbers = sorted(random.sample(range(1, 61), 6))
        self.ids.result_label.text = "Números gerados aleatoriamente:\n " + ", ".join(str(num) for num in self.numbers)

    def generate_frequent(self):
        # Exemplo de números mais frequentes (você pode substituir por dados reais)
        frequent_numbers = [10, 20, 30, 40, 50, 60]
        self.numbers = sorted(random.sample(frequent_numbers, 6))
        self.ids.result_label.text = "Números mais frequentes:\n " \
        "do período de Nov/1996 a Fev/2026"

    def generate_ai_predicted(self):
        # Exemplo de números previstos por IA (você pode substituir por dados reais)
        ai_predicted_numbers = [5, 15, 25, 35, 45, 55]
        self.numbers = sorted(random.sample(ai_predicted_numbers, 6))
        self.ids.result_label.text = "Números previstos por IA"