import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text="First Name: "))
        self.FirstName = TextInput(multiline=False)
        self.inside.add_widget(self.FirstName)

        self.inside.add_widget(Label(text="Last Name: "))
        self.LastName = TextInput(multiline=False)
        self.inside.add_widget(self.LastName)

        self.inside.add_widget(Label(text="Email Address: "))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)

        self.add_widget(self.inside)
        

        self.submit = Button(text="Submit", font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)
     

    def pressed(self, instance):
        FirstName = self.FirstName.text
        LastName = self.LastName.text
        email = self.email.text

        print("\nFirst Name: ", FirstName, "\nLast Name: ", LastName, "\nEmail: ", email)
        self.FirstName.text = ""
        self.LastName.text = ""
        self.email.text = ""

        
class TestApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    TestApp().run()
    
