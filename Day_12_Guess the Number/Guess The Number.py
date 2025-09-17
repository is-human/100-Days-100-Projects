import random
from art import logo

low_n = 1
high_n = 100

print(logo)
print("Welcome to the Number Game!")
print(f"I'm thinking of a number between {low_n} and {high_n}.")
random_n = random.choice(range(low_n, high_n+1))
lives_remaining = 0

while True:
    skill_mode = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if skill_mode == "easy" or skill_mode == 'hard':
        break
    else:
        print("Invalid response. Please try again.")

if skill_mode == "hard":
    lives_remaining = 5
else:
    lives_remaining = 10
while lives_remaining > 0:
    print(f"You have {lives_remaining} attempts remaining to guess the number.")
    while True:
        guess = input("Make a guess: ")
        try:
            int(guess)
            break
        except ValueError:
            print(f"Invalid response. Please type a numerical value within the range: {low_n} - {high_n}")
    
    guess = int(guess)

    if guess == random_n:
        print(f"You got it! The answer is {random_n}.")
        break
    else:
        lives_remaining -= 1
        if guess > random_n:
            print("Too High")
        else:
            print("Too Low")
    if lives_remaining == 0:
        print("You ran out of attempts. You lose!")
        print(f"The correct number is: {random_n}")