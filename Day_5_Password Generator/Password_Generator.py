import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

while True:
    try:
        nr_letters = int(input("How many letters would you like in your password?\n"))
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

while True:
    try:
        nr_numbers = int(input("How many numbers would you like?\n"))
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

while True:
    try:
        nr_symbols = int(input("How many symbols would you like?\n"))
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

list_letters = random.choices(letters,k=nr_letters)
list_numbers = random.choices(numbers,k=nr_numbers)
list_symbols = random.choices(symbols,k=nr_symbols)

password = list_letters + list_numbers + list_symbols
random.shuffle(password)

string_text = ""

for character in password:
    string_text += character

print(f"Your password is: {string_text}")