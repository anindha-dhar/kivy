import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.core.clipboard import Clipboard
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty




class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text="Enter your message: "))
        self.name = TextInput(hint_text='Enter text,Made by Priyam',allow_copy= True)
        self.inside.add_widget(self.name)

        #self.inside.add_widget(Label(text="Last Name: "))
        #self.lastName = TextInput(multiline=False)
        #self.inside.add_widget(self.lastName)

        #self.inside.add_widget(Label(text="Email: "))
        #self.email = TextInput(multiline=False)
        #self.inside.add_widget(self.email)

        self.add_widget(self.inside)

        self.submit = Button(text="Encrypt Data", font_size=20,size_hint= (0.3, 0.3))
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

        self.submit = Button(text="Decrypt Data", font_size=20,size_hint= (0.3, 0.3))
        self.submit.bind(on_press=self.pushed)
        self.add_widget(self.submit)

    def pressed(self, instance):
        name = self.name.text
        #last = self.lastName.text
        #email = self.email.text

        #print("Name:", name, "Last Name:", last, "Email:", email)
        #self.name.text = ""
        #self.lastName.text = ""
        #self.email.text = ""
        self.letter=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','.',',']
        self.secret=['T','J','9','A','7','1','R','U','B','0','5',',','F','3','M','8','K','W','4','E','.','Y','Q','L','D','P','X','G','I','C','6','Z','2','O','S','V','N','H']
        self.msg=""
        self.data=name
        #self.flag=0
        #self.data=self.data.read()
        self.data=self.data.split()
                #print(data)
        for i in self.data:
                    p=i.upper()
                    #print(p)
                    for j in p:
                        if j in self.letter:
                            index=self.letter.index(j)
                            self.msg += self.secret[index]
                        elif j=="&":
                            #self.msg += "&"
                            continue
                            #self.flag=1
                        else:
                            self.msg += "*"
                    self.msg += " "
        print(self.msg)
        layout = GridLayout(cols = 1, padding = 10)

		#popupLabel = Label(text = self.msg)
        popupLabel=Label(text=self.msg)
		#closeButton = Button(text = "Close the pop-up")
        closeButton=Button(text="Close it",size_hint= (0.3, 0.3))
        ctc=Button(text="Copy to Clipboard",on_press= self.on_clipboard,font_size=20,size_hint= (0.3, 0.3))



        layout.add_widget(popupLabel)

        layout.add_widget(closeButton)
        layout.add_widget(ctc)
        popup = Popup(title='Encrypted Message',
        content=layout,
        size_hint=(1, 1), size=(400, 400),auto_dismiss=False)
        popup.open()
        #content.bind(on_press=popup.dismiss)
        closeButton.bind(on_press = popup.dismiss)

        self.name.text = ""
    def on_clipboard(self, *args):
            '''Event handler to "Copy to Clipboard" button
            '''
            Clipboard.copy(self.msg)
    def pushed(self, instance):
        name = self.name.text
        #last = self.lastName.text
        #email = self.email.text

        #print("Name:", name, "Last Name:", last, "Email:", email)
        #self.name.text = ""
        #self.lastName.text = ""
        #self.email.text = ""
        self.letter=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','.',',']
        self.secret=['T','J','9','A','7','1','R','U','B','0','5',',','F','3','M','8','K','W','4','E','.','Y','Q','L','D','P','X','G','I','C','6','Z','2','O','S','V','N','H']
        self.msg1=""
        self.data=name
        #self.flag=0
        #self.data=self.data.read()
        self.data=self.data.split()
                #print(data)
        for i in self.data:
                    #p=i.upper()
                    #print(p)
                    for j in i:
                        if j in self.secret:
                            index=self.secret.index(j)
                            self.msg1 += self.letter[index]
                        elif j=="&":
                            #self.msg += "&"
                            continue
                            #self.flag=1
                        else:
                            self.msg1 += "*"
                    self.msg1 += " "
        print(self.msg1)
        layout = GridLayout(cols = 1, padding = 10)

		#popupLabel = Label(text = self.msg)
        popupLabel=Label(text=self.msg1)
		#closeButton = Button(text = "Close the pop-up")
        closeButton=Button(text="Close it",size_hint= (0.3, 0.3))
        ctc=Button(text="Copy to Clipboard",on_press= self.clipboard,font_size=20,size_hint= (0.3, 0.3))



        layout.add_widget(popupLabel)

        layout.add_widget(closeButton)
        layout.add_widget(ctc)
        popup = Popup(title='Decrypted Message',
        content=layout,
        size_hint=(1, 1), size=(400, 400),auto_dismiss=False)
        popup.open()
        #content.bind(on_press=popup.dismiss)
        closeButton.bind(on_press = popup.dismiss)

        self.name.text = ""
    def clipboard(self, *args):
            '''Event handler to "Copy to Clipboard" button
            '''
            Clipboard.copy(self.msg1)


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()

#python s.py
