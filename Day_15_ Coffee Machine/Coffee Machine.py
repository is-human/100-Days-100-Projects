import lists

def q_drink():
    while True:
        drink = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if drink == "espresso" or drink == "latte" or drink == "cappuccino" or drink == "report" or drink == "off":
            return drink
        else:
            print("Invalid response. Please try again.")
def q_insert_coins():
    while True:
        try:
            q_quarters = int(input("How Many Quaters?: "))
            break
        except ValueError:
            print("Invalid response. Please try again.")
    while True:
        try:
            q_dimes = int(input("How Many Dimes?: "))
            break
        except ValueError:
            print("Invalid response. Please try again.")
    while True:
        try:
            q_nickles = int(input("How Many Nickles?: "))
            break
        except ValueError:
            print("Invalid response. Please try again.")
    while True:
        try:
            q_pennies = int(input("How Many Pennies?: "))
            break
        except ValueError:
            print("Invalid response. Please try again.")
    quarters = q_quarters*0.25
    dimes = q_dimes*0.1
    nickles = q_nickles*0.05
    pennies = q_pennies*0.01
    coins_inserted = quarters + dimes + nickles + pennies
    return coins_inserted
def dispense_drink(list, drink_type, bank):
    starting_water = list.resources["water"]
    starting_milk = list.resources["milk"]
    starting_coffee = list.resources["coffee"]

    drink_cost = list.MENU[f"{drink_type}"]["cost"]
    required_water = list.MENU[f"{drink_type}"]["ingredients"]["water"]
    required_milk = list.MENU[f"{drink_type}"]["ingredients"]["milk"]
    required_coffee = list.MENU[f"{drink_type}"]["ingredients"]["coffee"]

    if required_water <= starting_water and required_coffee <= starting_coffee and required_milk <= starting_milk:
        list.resources["water"] -= required_water
        list.resources["milk"] -= required_milk
        list.resources["coffee"] -= required_coffee
        print("Please insert your coins.")
        coins_received = q_insert_coins()
        if coins_received < drink_cost:
            print("Sorry, that's not enough money. Money Refunded.")
            return bank
        elif coins_received > drink_cost:
            change = drink_cost - coins_received
            change = round(abs(change), 2)
            print(f"Here is ${change} in change.")
            print(f"Here is your {drink_type} ☕. Enjoy!")
            bank += drink_cost
            return bank
        else:
            print("Exact amount given.")
            print(f"Here is your {drink_type} ☕. Enjoy!")
            bank += drink_cost
            return bank
    else:
        print(f"Sorry, not enough resources to produce {drink_type}.")
        return bank
earned_money = 0

while True:
    drink = q_drink()

    if drink == "off":
        break
    elif drink == "report":
        print(f"Water: {lists.resources["water"]}ml\n"+
                f"Milk: {lists.resources["milk"]}ml\n"+
                f"Coffee: {lists.resources["coffee"]}g\n"+
                f"Money: ${earned_money}")
    else:
        earned_money = dispense_drink(lists, drink, earned_money)