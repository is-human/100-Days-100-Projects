import random
import os
from art import logo

# ****************************************************
def q_blackjack():
    while True:
        blackjack = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
        if blackjack == "y" or blackjack == "n":
            return blackjack
        else:
            print("Invalid response. Please try again.")
def q_draw_card():
    while True:
        draw_card = input("Would you like another card? Type 'y' or 'n': ").lower()
        if draw_card == "y" or draw_card == "n":
            return draw_card
        else:
            print("Invalid response. Please try again.")
def q_continue_game():
    while True:
        continue_game = input("If you would like to continue game, type 'c'.\n" 
                              "If you would like to show card count and continue game, type 'cc'.\n" 
                              "If you would like to refresh the game, type 'r'.\n" 
                              "If you would like to discontinue play, type 'e'.\n").lower()
        if continue_game == "c" or continue_game == "r" or continue_game == "e" or continue_game == "cc":
            return continue_game
        else:
            print("Invalid response. Please try again.")
# ****************************************************
def game_setup():
    global user_total
    draw_card_user(card_pool, users_hand, user_total, discarded_cards)
    draw_card_computer(card_pool, computers_hand, computer_total, discarded_cards)
    draw_card_user(card_pool, users_hand, user_total, discarded_cards)
    draw_card_computer(card_pool, computers_hand, computer_total, discarded_cards)
    check_11s_user()
    if user_total == 21:
        print(f"Your Final Hand: {users_hand}. Final Score: {user_total}")
        print(f"Computer's Final Hand: {computers_hand}. Final Score: {computer_total}")
    else:
        print_current_scores()
# ****************************************************
def draw_card_user(pool, hand, total, discard):
    global cards
    global decks
    global card_pool
    global user_total
    while True:
        try:
            card_drawn = pool[0]
            break
        except IndexError:
            card_pool = cards * decks
            random.shuffle(card_pool)
            pool = card_pool
            discard = []
            print("Cards ran out, deck reshuffled.")
            hand_len = str(len(hand))
            if hand_len[-1] != "0" and hand_len[-1] != "1" and hand_len[-1] != "2":
                print(f"First card drawn as your {int(hand_len)+1}th card.")
            elif hand_len[-1] == "0":
                print(f"First card drawn as your {int(hand_len)+1}st card.")
            elif hand_len[-1] == "1":
                print(f"First card drawn as your {int(hand_len)+1}nd card.")
            else:
                print(f"First card drawn as your {int(hand_len)+1}rd card.")
            break
    card_drawn = pool[0]
    hand.append(card_drawn)
    pool.remove(card_drawn)
    discard.append(card_drawn)
    total = 0
    for n in hand:
            total += n
    user_total = total
def draw_card_computer(pool, hand, total, discard):
    global cards
    global decks
    global card_pool
    global computer_total
    while True:
        try:
            card_drawn = pool[0]
            break
        except IndexError:
            card_pool = cards * decks
            random.shuffle(card_pool)
            pool = card_pool
            discard = []
            print("Cards ran out, deck reshuffled.")
            hand_len = str(len(hand))
            if hand_len[-1] != "0" and hand_len[-1] != "1" and hand_len[-1] != "2":
                print(f"First card drawn as computer's {int(hand_len)+1}th card.")
            elif hand_len[-1] == "0":
                print(f"First card drawn as computer's {int(hand_len)+1}st card.")
            elif hand_len[-1] == "1":
                print(f"First card drawn as computer's {int(hand_len)+1}nd card.")
            else:
                print(f"First card drawn as computer's {int(hand_len)+1}rd card.")
            break
    card_drawn = pool[0]
    hand.append(card_drawn)
    pool.remove(card_drawn)
    discard.append(card_drawn)
    total = 0
    for n in hand:
            total += n
    computer_total = total
# ****************************************************
def print_current_scores():
    print(f"Your Cards: {users_hand}. Current Score: {user_total}")
    print(f"Computer's Hand: [Hidden, {computers_hand[1]}]. Known Score: {computers_hand[1]}")
# ****************************************************
def total_grt_21():
    global user_total
    global users_hand
    if user_total > 21:
        if 11 in users_hand:
            index_11 = users_hand.index(11)
            users_hand.insert(index_11, 1)
            users_hand.remove(11)
            if user_total > 21:
                return True
            else:
                return False
        else:
            return True
    else:
        False
def total_less_17():
    global computer_total
    global computers_hand
    if computer_total < 17:
        return True
    else:
        return False
# ****************************************************
def check_winner():
    global user_total
    global computer_total
    global blackjack
    if blackjack == False:
        if user_total > 21:
            print(f"You Lose!")
        elif user_total == computer_total:
            print(f"You Draw!")
        elif user_total < computer_total and computer_total <= 21:
            print(f"You Lose!") 
        elif user_total > computer_total:
            print(f"You Win!")
        elif user_total <= 21:
            print("You Win!")
    print("********************************************")
    print("********************************************")
# ****************************************************
def check_11s_user():
    global user_total
    global users_hand
    while user_total > 21:
        if 11 in users_hand:
            index_11 = users_hand.index(11)
            users_hand.insert(index_11, 1)
            users_hand.remove(11)
            user_total = 0
            for n in users_hand:
                user_total += n
        else:
            break
def check_11s_computer():
    global computer_total
    global computers_hand
    while computer_total > 21:
        if 11 in computers_hand:
            index_11 = computers_hand.index(11)
            computers_hand.insert(index_11, 1)
            computers_hand.remove(11)
            computer_total = 0
            for n in computers_hand:
                computer_total += n
        else:
            break
# ****************************************************
def count_cards(discard):
    card_count = 0
    for n in discard:
        if n in n_plus_one:
            card_count += 1
        elif n in n_minus_one:
            card_count -= 1
    return card_count
# ****************************************************
# First Question: Would you like to play Blackjack?
play_game = q_blackjack()

# Start Game
while play_game == "y":
    # Setup
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    decks = 4*6
    discarded_cards = []
    card_pool = cards * decks
    random.shuffle(card_pool)
    user_total = 0
    computer_total = 0
    n_plus_one = range(2,6+1)
    n_minus_one = [10,11,1]
    n_do_nothing = range(7,9+1)
    card_count = 0

    # Game w/ Original Card Pool
    while True:
        # First Hand
        users_hand = []
        computers_hand = []
        blackjack = False
        game_setup()
        if user_total == 21 and computer_total == 21:
            blackjack = True
            print(f"Draw!")
        elif user_total == 21:
            blackjack = True
            print(f"Blackjack! You Win!")
        
        # Second Question: Would you like another card?
        while user_total < 21:
            draw_card = q_draw_card()
            print("********************************************")
            if draw_card == "y":
                draw_card_user(card_pool, users_hand, user_total, discarded_cards)
                check_11s_user()
                if user_total >= 21:
                    break
                print_current_scores()
            else:
                break
        
        # Computer Draws(If Needed)
        while total_less_17() and blackjack == False and user_total <= 21:
            draw_card_computer(card_pool, computers_hand, computer_total, discarded_cards)
            check_11s_computer()
        
        if blackjack == False:
            print(f"Your Final Hand: {users_hand}. Final Score: {user_total}")
            print(f"Computer's Final Hand: {computers_hand}. Final Score: {computer_total}")
        
        # Winner
        check_winner()

        # Count Cards
        card_count = count_cards(discarded_cards)

        # Third Question: Continue Game, Refresh Game, or End Game?
        continue_game = q_continue_game()
        print("********************************************")
        if continue_game == "r" or continue_game == "e":
            break
        elif continue_game == "cc":
            print(f"The running card count is: {card_count}")
    if continue_game == "e":
        break
    else:
        if os.name == "nt":
            os.system("cls")
            print(f"Last game's running card count was: {card_count}")
        else:
            os.system("clear")
            print(f"Last game's runnning card count was: {card_count}")