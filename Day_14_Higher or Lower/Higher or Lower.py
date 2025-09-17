import os
import random
from game_data import data
import art

def check_a_or_an(list, binary):
    if list[binary]["description"][0] in vowels:
        return "an"
    else:
        return "a"
def print_setup(list):
    print(art.logo)
    print(f"Compare A: {list[0]["name"]}, " + check_a_or_an(list, 0) + f" {list[0]["description"]}, from {list[0]["country"]}.")
    print(art.vs)
    print(f"Against B: {list[1]["name"]}, " + check_a_or_an(list, 1) + f" {list[1]["description"]}, from {list[1]["country"]}.")
def q_guess():
    while True:
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        if guess == "a" or guess == "b":
            return guess
        else:
            print("Invalid response. Please try again.")

random.shuffle(data)
vowels = ["A", "E", "I", "O", "U"]
score = 0

while True:
    print_setup(data)
    option_a = data[0]["follower_count"]
    option_b = data[1]["follower_count"]
    guess = q_guess()

    if option_a > option_b:
        winner = "a"
    else:
        winner = "b"
    
    if guess == winner:
        del data[0]
        score += 1
        try:
            data[0]
        except IndexError:
            break
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    else:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        break

print(art.logo)

if score == 50:
    print("Congradulations! You guessed all the right answers!")
else:
    print(f"Sorry, that's wrong. Final Score: {score}")