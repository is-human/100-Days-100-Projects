from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for i in range(nr_letters)]
    password_list += [random.choice(symbols) for i in range(nr_symbols)]
    password_list += [random.choice(numbers) for i in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)

    password_input.delete(0, END)
    password_input.insert(0, password)
    
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_text = website_input.get()
    username_text = username_input.get()
    password_text = password_input.get()
    
    if website_text == "" or username_text == "" or password_text == "":
        messagebox.showerror(title="Error", message="Oops! Please makes sure you haven't left a field empty.")
    else:
        is_true = messagebox.askokcancel(title=website_text, message=f"These are the details entered:\n"
                                        f"Username: {username_text}\n"
                                        f"Password: {password_text}\n"
                                        "Is it okay to save?")
        
        if is_true == True:
            with open(r"data.txt", "a") as file:
                file.write(f"\n{website_text} | {username_text} | {password_text}")
            
            website_input.delete(0, END)
            password_input.delete(0, END)
            username_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=190, height=200)
my_pass_image = PhotoImage(file=r"logo.png")
canvas.create_image(100,95,image=my_pass_image)
canvas.grid(column=2, row=1)

website_label = Label(text="Website:")
website_label.grid(column=1, row=2, sticky="e")

username_label = Label(text="Email/Username:")
username_label.grid(column=1, row=3, sticky="e")

password_label = Label(text="Password:")
password_label.grid(column=1, row=4, sticky="e")

password_generator_button = Button(text="Generate Password", highlightthickness=0, command=generate_password)
password_generator_button.grid(column=3, row=4, sticky="w")

add_password_button = Button(text="Add", highlightthickness=0, width=42, command=save)
add_password_button.grid(column=2, row=5, columnspan=2, sticky="w")

website_input = Entry(width=50)
website_input.grid(column=2, row=2, columnspan=2, sticky="w")
website_input.focus()

username_input = Entry(width=50)
username_input.grid(column=2, row=3, columnspan=2, sticky="w")
username_input.insert(0, "example@example.com")

password_input = Entry(width=31)
password_input.grid(column=2, row=4, sticky="w")

window.mainloop()