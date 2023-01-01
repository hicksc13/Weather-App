from osrs_api.const import AccountType
from osrs_api import Hiscores
import tkinter as tk

class MyGui:

    def __init__(self):
        self.root = tk.Tk()

        self.root.geometry("1000x1000")
        self.root.title("OSRS Look-up")

        self.name_var=tk.StringVar()
        self.name_var.set("")

        self.label = tk.Label(self.root, text="Hello Please enter your OSRS Name to Begin", font=('Arial', 20))
        self.label.pack(padx=20, pady=20)


        self.char_name = tk.Entry(self.root, textvariable = self.name_var, font = ('calibre',10,'normal'))
        self.char_name.pack()

        self.sub_btn=tk.Button(self.root,text = 'Submit', command = self.search_name)
        self.sub_btn.pack()

        self.text_box = tk.Text(self.root, width = 50, height = 25)
        self.text_box.pack()
        

        self.root.mainloop()


    def search_name(self, *args):

        name_entered = self.name_var.get()
        input_player = Hiscores(name_entered)
        #need to figure out how to display the hiscores info. Stuck at it giving me errors about the type. 
        return input_player.skills
        print(type(input_player))
        print(input_player)

MyGui()

