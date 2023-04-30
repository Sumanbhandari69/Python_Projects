from tkinter import *

window = Tk()
window.title("Mile To KM Converter")
window.minsize(height=200, width=200)
window.config(padx=20,pady=20)

#Entry
input = Entry(width=8)
input.grid(column=1, row=0)


#Label

my_label = Label(text="Miles")
my_label.grid(column= 2,row= 0)

my_label1 = Label(text="is equal to ")
my_label1.grid(column= 0,row= 1)

my_label2 = Label(text="KM ")
my_label2.grid(column= 2,row= 1)

my_label3 = Label(text="0 ")
my_label3.grid(column= 1,row= 1)

#Button


def to_convert():
    miles = float(input.get())
    # print(type(miles))
    km = 1.6 * miles
    my_label3.config(text=km)


button = Button(text="Calculate",command=to_convert)
button.grid(column=1, row=2)


window.mainloop()