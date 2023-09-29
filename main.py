from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.app import App

Builder.load_file("LoginPage.kv")
class LoginPageApp(App):
    def build(self):
        return QuizManager()

class QuizManager(ScreenManager):
    pass
class Question1Screen(Screen):
    def answer_question(self, bool):
        if bool:
            self.manager.current = "correct"
        else:
            self.manager.current = "error"

class CorrectScreen(Screen):
    def press_button(self):
        self.manager.current = "question2"


class ErrorScreen(Screen):
    def press_button(self):
        self.manager.current = "question2"

class Question2Screen(Screen):
    def answer_question(self, heart):
        if heart.lower() == "deep in the heart of texas":
            self.manager.current = "question1"


if __name__ == "__main__":
    LoginPageApp().run()