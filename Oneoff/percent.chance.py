

from tkinter import *
import random

value = random.randint(20,97)
insult = ['time to use the wizard hat', 'you yellowbelly', 'Chances that high eh?', 'doubtful tbh', 'With those updrages we never stood a chance', ' but I doubt you will ever win again', 'you are fookin pathetic mate','Cody focus, for fucks sake', 'Jeong wake the fuck up']
name = random.choice(insult)


window = Tk()
window.title("What are my Chances?")
window.geometry('800x400')
window.configure(background = 'black')

lbl = Label(window, text="Roll to see your chances", bg='black',fg='white', font='none 16 bold')
lbl.grid(column=3, row=1)



def clicked():
    lbl.configure(text= f"Your chances of winning are currently {value}%! {name}!")
    btn = Button(window, text="Roll", command=clicked)
    btn.grid(column=0, row=0)


    
window.mainloop()




