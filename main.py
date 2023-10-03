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
    def press_button(self):
        self.manager.current = 'main'

class MainScreen(Screen):
    def press_button(self):
        self.ids.error.text = ""
        self.ids.password1.text = ""
        self.ids.username1.text = ""
        self.manager.current = "new_account"

    def login(self, username1, password1):
        if username1 in dict and password1 == dict[username1]:
            self.ids.error.text = ""
            self.ids.password1.text = ""
            self.ids.username1.text = ""
            self.manager.current = "logged"
        else:
            self.ids.error.text = "incorrect username or password"
            self.ids.password1.text = ""

class NewAccountScreen(Screen):
    def create_account(self, username2, password2, password3):
        var1 = False
        var2 = False
        var3 = False
        var4 = False
        var5 = False
        for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            if letter in password2:
                var1 = True
        for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower():
            if letter in password2:
                var2 = True
        for num in "0123456789":
            if num in password2:
                var3 = True
        for char in "~!@#$%^&*()_+`-={}|[];',./<>?:":
            if char in password2:
                var4 = True
        if len(password2) >= 8:
            var5 = True
        if var1 == True and var2 == True and var3 == True and var4 == True and var5 == True:
            if username2 not in dict and password2 == password3:
                dict[username2] = password2
                self.ids.incorrect.text = "Account registered. Return to main page"
            elif username2 in dict:
                self.ids.incorrect.text = "Username taken"
                self.ids.username2.text = ""
            elif not password2 == password3:
                self.ids.incorrect.text = "Passwords don't match"
                self.ids.password3.text = ""
        else:
            self.ids.incorrect.text = "Password doesn't contain an uppercase letter, lowercase letter, number, or special character, or is not 8 characters in length"
            self.ids.password2.text = ""
            self.ids.password3.text = ""
    def press_button(self):
        self.ids.incorrect.text = ""
        self.ids.password2.text = ""
        self.ids.password3.text = ""
        self.ids.username2.text = ""
        self.manager.current = 'main'






if __name__ == "__main__":
    LoginPage1App().run()