from tkinter import *
from tkinter import ttk
import tkinter as tk

    
def response_to(question:str)->str:
    question = question.lower().strip()
    if question == "what type of candy do you have?":
        return "We have everything! Gumdrop Mountains, Candy Cane Forest, Lollipop Woods, you name it!"
    elif question == "what is your favorite candy?":
        return "Hmm that's a hard one. I'm gonna have to say Licorice Castle!"
    elif question.startswith("hi"): 
        return "Hi, welcome to Candyland!" 
    elif question == "how do you play Candyland?":
        return "Come to Gumdrop Gardens to find out!" 
    elif question.startswith("where"):
        return "Near the Gumdrop Mountains just past the Lollipop Woods"
    elif question.startswith("who"):
        return "Probably King Kandy, the amazing ruler of Candyland"
    elif question.startswith("what"):
        return "Whatever you want it to be. Imagination is key at Candyland!"
    elif question.startswith("why"):
        return "Because King Kandy likes it that way!"
    elif question.startswith("is"):
        return "Sure, whatever makes you happy!"
    elif question.startswith("how"):
        return "Come to Candyland to find out!"
    else:
        default_number = len(question)%3
        if default_number == 0:
            return "Oh no! I am currently having a sugar rush but come back later for an answer🍬"
        elif default_number == 1:
            return "The answering machine is broken, but ask again later🍫"
        elif default_number == 2:
            return "Sorry, we are having a malfunction at Candyland. I'll get back to you later⏳"
        else:
            return "I'm not sure but here, have some candy 🍭"
        


root = Tk()
s = ttk.Style()
s.theme_use('classic')
s = ttk.Style()
s.configure('TFrame', background='pink')
s.configure('TLabel', background='pink', foreground='black', font=("Comic Sans MS", 20))
frm = ttk.Frame(root, padding=50)
frm.grid()
ttk.Label(frm, text=' \U0001F9C1', font=("Ariel",40 )).grid(column=0, row=0)
ttk.Label(frm, text=' Ask me anything about Candyland \U0001F60B', font=("Times New Roman", 28)).grid(column=1, row=4)                                                                
a = ttk.Label(frm, text="Hi, it's sweetbot. Candyland's Answering Machine!", font=("Times New Roman",24))
a.grid(column=1, row=0)
image = tk.PhotoImage(file="background.png")
image_label = ttk.Label(frm)
image_label .grid(column=1, row=2)
image_label.configure(image=image)
image_label.image = image



ttk.Label(frm, text=' ', font=("Times New Roman", 4)).grid(column=0, row=1)

q = Text(frm, height=5, width=55)
q.grid(column=0, row=2, columnspan = 2)


def answer_question():
    question = q.get("1.0", END)
    a.config(text=response_to(question.strip()))
    q.delete("1.0",END)

buttons = ttk.Frame(frm, padding=10)
ttk.Button(buttons, text="Ask", command=answer_question, width=18).grid(column=0, row=0)
ttk.Button(buttons, text="Quit", command=root.destroy, width=18).grid(column=1, row=0)
buttons.grid(row=3, column=0, columnspan=2)
root.mainloop()
frm = ttk.Frame(root, padding=20)
style = ttk.Style()


import tkinter as tk
from tkinter import PhotoImage


