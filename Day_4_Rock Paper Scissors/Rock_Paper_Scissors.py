rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
game_choices = [rock, paper, scissors]
n_generator = random.randint(0,2)
computer = game_choices[n_generator]
user_input = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n")

if user_input not in ["0", "1", "2"]:
    print("You typed an invalid character, you lose!")
else:
    n_user = int(user_input)
    user = game_choices[n_user]

    print(user)
    print("Computer Chose:")
    print(computer)
    if n_user == n_generator:
        print("You Draw!")
    elif n_user - n_generator in [-2, 1]:
        print("You Win!")
    else:
        print("You Lose!")