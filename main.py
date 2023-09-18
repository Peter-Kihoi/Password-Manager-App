from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    generated_password = "".join(password_list)

    password_input.insert(0, generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get().title()
    email = username_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Opps", message="Please don't leave any fields empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading the old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # saving updated data
                json.dump(new_data, data_file, indent=4)
        else:
            # updating the old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- Search Password ------------------------------- #
def find_password():
    website = website_input.get().title()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
        web_dict = data[website]
        messagebox.showinfo(title=website, message=f"Email: {web_dict['email']}\nPassword: {web_dict['password']}")
    except KeyError:
        messagebox.showerror(title="Oops", message=f"No details for {website} found")
    except FileNotFoundError:
        messagebox.showerror(title="Oops", message="No Data File Found")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

# Canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
pass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.config(padx=10, pady=10)
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:")
username_label.config(padx=10, pady=10)
username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.config(padx=10, pady=10)
password_label.grid(column=0, row=3)

# Entry
website_input = Entry(width=21)
website_input.focus()
website_input.grid(column=1, row=1)

username_input = Entry(width=50)
username_input.insert(0, "elit3p254@gmail.com")
username_input.grid(column=1, row=2, columnspan=2)

password_input = Entry(width=21)
password_input.grid(column=1, row=3)

# Button
search_btn = Button(text="Search", width=20, command=find_password)
search_btn.grid(column=2, row=1)

generate_btn = Button(text="Generate Password", width=20, command=generate_password)
generate_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=36, command=save)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()
