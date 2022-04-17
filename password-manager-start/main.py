from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #



# ---------------------------- SAVE PASSWORD ------------------------------- #



def save():
    website = entry_1.get()
    email = entry_2.get()
    passwords = entry_3.get()
    with open("data.txt", "a") as data_file:
        data_file.write(f"{website} | {email} | {passwords}\n")
        entry_1.delete(0, END)
        entry_2.delete(0, END)
        entry_3.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

photo = PhotoImage(file="logo.png")

canvas = Canvas(width= 200, height= 200)

canvas.create_image(100, 100, image= photo)
canvas.grid(column= 1, row=0)

website = Label(text="Website")
website.grid(column=0, row=1)
entry_1 = Entry(width=35)
entry_1.focus()
entry_1.grid(column=1, row=1, columnspan=2)


email_username = Label(text="Email/Username:")
email_username.grid(column=0, row=2)
entry_2 = Entry(width=35)
entry_2.insert(0, "intisar.a@live.com")
entry_2.grid(column=1, row=2, columnspan=2)

password = Label(text="Password:")
password.grid(column=0, row=3)
entry_3 = Entry(width=21)
entry_3.grid(column=1, row=3)

generate_password = Button(text="Generate Password")
generate_password.grid(column=2, row=3)

add = Button(text="Add", width=36, command=save)
add.grid(column=1, row=4, columnspan=2)







window.mainloop()

