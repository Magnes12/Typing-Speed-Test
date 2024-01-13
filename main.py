from tkinter import *
import tkinter as tk
from tkinter import messagebox
import random
import time

words = ["elephant", "sunshine", "keyboard", "adventure", "butterfly", "chocolate", "happiness",
         "symphony", "rainbow", "blueprint", "velocity", "celebrate", "universe", "galaxy", "treasure",
         "whistle", "xylophone", "quasar", "wonderland", "pajamas", "radiant", "serendipity", "mysterious",
         "journey", "acoustic", "blueprint", "harmony", "cinnamon", "quicksilver", "blossom"]

app = tk.Tk()
app.title("Type speed test")
app.geometry("400x400")

app_font = ('times', 18, 'bold')

l1 = tk.Label(app, text="Typing speed test", width=30, font=app_font)
l1.grid(column=1, row=0)

type_field = Entry(app, width=30)
type_field.grid(column=1, row=3)

start_button = tk.Button(app, text="Start", width=10, command=lambda: start())
start_button.grid(column=1, row=4)

point = 0  

def start():
    global point  
    word_to_type = random.choice(words)
    l2 = tk.Label(app, text=word_to_type, width=50)
    l2.grid(column=1, row=1)

    type_field.delete(0, 'end')  
    type_field.focus()  

    def check(event):
        global point 
        entered_text = type_field.get()
        if entered_text == word_to_type:
            point += 1
            words.remove(word_to_type)

        start()

    type_field.bind('<Return>', check)  

def result():
    global point
    messagebox.showinfo(title="Results",
                                message=f"You've got {point} correct words in 60 seconds")
    time.sleep(2)
    quit()
               
app.after(60000, result)

start_button.configure(command=start)

app.mainloop()
