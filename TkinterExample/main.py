from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500,height=400)

#Label

my_label = Label(text="I am a Label", font=("Arial",24,"bold"))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text = "New Text")

#Button

def button_clicked():
    print("Clicked")
    new_text = input.get()
    my_label.config(text=new_text)

button = Button(text="Click me" ,command=button_clicked)
button.pack()

#Entry
input = Entry(width=20)
input.pack()


window.mainloop()


