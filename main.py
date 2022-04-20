from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    letter_list = [random.choice(letters) for char in range(nr_letters)]
    number_list = [random.choice(numbers) for char in range(nr_numbers)]
    symbol_list = [random.choice(symbols) for char in range(nr_symbols)]
    password_list = letter_list + number_list + symbol_list
    random.shuffle(password_list)
    password = "".join(password_list)
    third_entry.insert(0, password)
    pyperclip.copy(password)


#----------------------------- search -------------------------------------#


def search():
    website = first_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="file error", message=f"no details for the website exists")
    else:
        if website in data:
            web_mail = data[website]["email"]
            web_password = data[website]["password"]
            messagebox.showinfo(title=f"{website} details", message=f"email: {web_mail} \n password:{web_password}")
        else:
            messagebox.showinfo(title="Website error", message=f"{website} website is not found")
    finally:
        first_entry.delete(0, END)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = first_entry.get()
    email = second_entry.get()
    password = third_entry.get()
    new_data = {
        website : {
            "email": email,
            "password": password,
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="alert", message=f"do not leave website,password empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            first_entry.delete(0, END)
            third_entry.delete(0, END)
            first_entry.focus()
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200, highlightthickness=0)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
first_entry = Entry(width=17)
first_entry.grid(row=1, column=1)
first_entry.focus()
second_entry = Entry(width=35)
second_entry.grid(row=2, column=1, columnspan=2)
second_entry.insert(0, "mukesh@gmail.com")
third_entry = Entry(width=17)
third_entry.grid(row=3, column=1)
generate_button = Button(text="Generate Password", command=generate)
generate_button.grid(row=3, column=2)
add_button = Button(text="Add", width=30, command=save)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search", width=15, command=search)
search_button.grid(row=1, column=2)
window.mainloop()

