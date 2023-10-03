from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.app import App

Builder.load_file("LoginPage1.kv")
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
    def answer_question(self, text):
        if text.lower() == "deep in the heart of texas":
            self.manager.current = "correct"
        else:
            self.ids.invalid.text = "Invalid guess.\n Try again"
            self.ids.invalid.color = 1, .5, .5







dict = {}


class LoginPage1App(App):
    def build(self):
        return LoginManager()
class LoginManager(ScreenManager):
    pass

class LoggedInScreen(Screen):
    pass

class MainScreen(Screen):
    def press_button(self):
        self.manager.current = "new_account"

    def login(self, username1, password1):
        pass

class NewAccountScreen(Screen):
    def create_account(self, dict, username2, password2, password3):
        if username2 not in dict.items and password2 == password3:
            dict[username2] = password2
        elif username2 in dict.items:
            self.ids.incorrect.text = "Username taken"
        elif not password2 == password3:
            self.ids.incorrect.text = "Passwords don't match"




if __name__ == "__main__":
    LoginPage1App().run()