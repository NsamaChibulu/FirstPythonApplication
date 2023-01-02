## import components widgets for the application
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button 
from kivy.uix.textinput import TextInput
from datetime import datetime

class AgeCalculator(App):

    def getAge(self, event):
        current_dateTime = datetime.now()
        current_year = current_dateTime.year
        dob = self.date.Text
        age = int(current_year) - int(dob)
        self.ageRequest.text = (f"You are {age} years old.")

    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"centre_x":0.5, "centre_y":0.5}
        self.window.add_widget(image(source("logo.png")))

        self.ageRequest = Label (
        text = "Enter the year of your birth:",
        font_size = 50,
        color = "#ffffff",
        bold = True
        )

        self.window.add_widget(self.ageRequest)

        self.date = TextInput (
        multiline = False,
        padding_y = (30,30),
        size_hint = (1,0.7),
        font_size = 30
        )

        self.window.add_widget(self.date)

        self.button = Button(
        text = "Calulate age",
        size_hint = (0.5, 0.5),
        bold = True,
        font_size = 30
        )

        self.button.bind(on_press = self.getAge)
        self.window.add_widget(self.button)

        return self.window


if __name__ == "___main___":
    AgeCalculator().run()
