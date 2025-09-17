import random
from hangman_art import logo, stages
from hangman_words import word_list

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
chosen_word = random.choice(word_list)
cw_len = len(chosen_word)
display_text = cw_len * "_"
total_lives = 6

print(logo)
print(stages[total_lives])
print(f"Word to Guess: {display_text}")
print(f"Lives Remaining: {total_lives}")
print(f"Letter Pool: {letters}")

while total_lives > 0 and display_text != chosen_word:
    while True:
        guess = input("Guess a letter: ").lower()
        if guess in letters:
            placement = -1
            tally = 0
            break
        else:
            print("Invalid character, please enter a single letter listed in the pool.")

    for letter in chosen_word:
        placement += 1
        if letter == guess:
            display_text = display_text[:placement] + letter + display_text[placement+1:]
        else:
            tally += 1
    
    if tally == cw_len:
        total_lives -= 1
    
    letters.remove(guess)

    if total_lives > 0 and display_text != chosen_word:
        print(stages[total_lives])
        print(f"Word to Guess: {display_text}")
        print(f"Lives Remaining: {total_lives}")
        print(f"Letter Pool: {letters}")

if total_lives > 0:
    print(f"You Win! The word was: {chosen_word}!\n" + "Can you do that again!?")
else:
    print(stages[0])
    print(f"You Lose! The correct word was: {chosen_word} :(\n" + "Give it another shot!")