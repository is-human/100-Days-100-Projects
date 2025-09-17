import os
from art import logo

bid_folder = {}

while True:
    print(logo)
    while True:
        key_name = input("What is your name?: ")
        if key_name not in bid_folder:
            break
        else:
            print("Another bidder has your name!. Please type a new name so we can identify you.")
    while True:
        try:
            value_bid = float(input("What is your bid? $"))
            break
        except ValueError:
            print("Invalid response. Please enter a numerical value only.")

    bid_folder[key_name] = value_bid

    while True:
        new_players = input("Are there any other bidder? Type 'yes or 'no'.\n").lower()
        if new_players == "yes" or new_players == "no":
            break
        else:
            print("Invalid response. Please try again.")
    if new_players == "no":
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        break
    else:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

highest_amount = 0
highest_bidder = ""

for name in bid_folder:
    if bid_folder[name] > highest_amount:
        highest_amount = bid_folder[name]
        highest_bidder = name

print(logo)
print(f"The winner is: {highest_bidder}!\n" + f"SOLD for: ${highest_amount}")
