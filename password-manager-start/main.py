from tkinter import *
from tkinter import messagebox
from random import randint,shuffle,choice
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for _ in range(randint(8,10))]
    password_symbols = [choice(symbols) for _ in range(randint(2,4))]
    password_numbers = [choice(numbers) for _ in range(randint(2,4))]

    password_list = password_numbers + password_symbols + password_letters

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0,END)
    password_entry.insert(0,password)
    pyperclip.copy(password)








# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website_value = website_entry.get()
    email_value = email_entry.get()
    password_value = password_entry.get()
    new_data = {
        website_value: {
            "email" : email_value,
            "password" : password_value,

        }
    }

    if website_value == "" or password_value == "":
        messagebox.showerror(title="Error",message="All Fields Are Mandatory!!")

    else:
        try:
            with open("data.json","r") as file:
                #Reading data
                data = json.load(file)

        except FileNotFoundError:
            with open("data.json","w") as file:
                json.dump(new_data,file, indent=4)

        else:
            #Updating data
            data.update(new_data)


            with open("data.json","w") as file:
                # Saving updated data
                json.dump(data,file,indent=4)

        finally:
            clear_data()




def clear_data():
    website_entry.delete(0,END)
    email_entry.delete(0,END)
    email_entry.insert(0, "sumanbhandari6969@gamil.com")
    password_entry.delete(0,END)

#Find password

def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="File not found!")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website,message=f"Email: {email}\n Password: {password}")

        else:
            messagebox.showerror(title="Error", message=f"No details for {website} exists.")





# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)


canvas = Canvas(width=200,height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image = logo_img)
canvas.grid(column=1,row=0)


website_label = Label(text="Website:")
website_label.grid(column=0,row=1)


website_entry = Entry(width=21)
website_entry.grid(column=1,row=1)
website_entry.focus()

email_label = Label(text="Email/Username:")
email_label.grid(column=0,row=2)

email_entry = Entry(width=35)
email_entry.grid(column=1,row=2,columnspan=2)
email_entry.insert(0,"sumanbhandari6969@gamil.com")

password_label = Label(text="Password:")
password_label.grid(column=0,row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1,row=3)

generate_password_button = Button(text="Generate Password",command=generate_password)
generate_password_button.grid(column=2,row=3)

add_password_button = Button(text="Add",width=36,command=save_data)
add_password_button.grid(column=1,row=4,columnspan=2)

search_button = Button(text="Search",width= 13,command=find_password)
search_button.grid(column=2,row=1)








window.mainloop()