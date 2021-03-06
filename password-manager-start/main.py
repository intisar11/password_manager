from tkinter import *
from tkinter import messagebox
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)



    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list1 = [random.choice(symbols) for _ in range(nr_symbols)]
    password_list2 = [random.choice(numbers) for _ in range(nr_numbers)]

    new_password_list = password_list2 + password_list1 + password_list

    random.shuffle(new_password_list)

    password = "".join(new_password_list)
    entry_3.insert(0, password)








# ---------------------------- SAVE PASSWORD ------------------------------- #

def find_password():
    with open("data.json") as data_file:
      search_pass = json.load(data_file)
    user_entry = entry_1.get()
    if user_entry in search_pass:
        email = search_pass[user_entry]["email"]
        password = search_pass[user_entry]["password"]
        messagebox.showinfo(title="Password Found", message=f"Your website:{user_entry}\n password:{password}\n email:{email}")
    else:
        user_entry not in search_pass
        messagebox.showinfo(title = "Error", message=f"Your {user_entry} password, and email not found")



def save():
    website = entry_1.get()
    email = entry_2.get()
    passwords = entry_3.get()
    new_data = {
        website: {
        "email": email,
        "password": passwords
    }
    }




    if len(website) == 0 or len(email) == 0 or len(passwords) == 0:
        messagebox.showinfo(title="Error", message="You can not leave any box empty")

    else:
        try:
           with open("data.json", "r") as data_file:
               data = json.load(data_file)

        except FileNotFoundError:
           with open("data.json", "w") as data_file:
            json.dump(new_data, data_file)

        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            entry_1.delete(0, END)
            entry_2.delete(0, END)
            entry_3.delete(0, END)


# ---------------------------- UI SETUP ----------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

photo = PhotoImage(file="logo.png")

canvas = Canvas(width= 200, height= 200)

canvas.create_image(100, 100, image= photo)
canvas.grid(column= 1, row=0)

website = Label(text="Website")
website.grid(column=0, row=1)
entry_1 = Entry(width=20)
entry_1.focus()
entry_1.grid(column=1, row=1)

search_button = Button(text="Search", width=13, command= find_password)
search_button.grid(column=2, row=1, columnspan=2)


email_username = Label(text="Email/Username:")
email_username.grid(column=0, row=2)
entry_2 = Entry(width=35)
entry_2.insert(0, "intisar.a@live.com")
entry_2.grid(column=1, row=2, columnspan=2)

password = Label(text="Password:")
password.grid(column=0, row=3)
entry_3 = Entry(width=21)
entry_3.grid(column=1, row=3)

generate_password = Button(text="Generate Password", command=generate_password)
generate_password.grid(column=2, row=3)

add = Button(text="Add", width=36, command=save)
add.grid(column=1, row=4, columnspan=2)







window.mainloop()

