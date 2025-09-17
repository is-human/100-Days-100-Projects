from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# def q_drink():
#     while True:
#         drink = input("What would you like? (espresso/latte/cappuccino): ").lower()
#         if drink == "espresso" or drink == "latte" or drink == "cappuccino" or drink == "report" or drink == "off":
#             return drink
#         else:
#             print("Invalid response. Please try again.")
# coffee_maker_oop = CoffeeMaker()
# money_machine_oop = MoneyMachine()
# menu_oop = Menu()
# menu_item_oop = MenuItem()

# drink = q_drink()
# menu_item_oop.name = drink
# if menu_oop.find_drink(menu_item_oop) != "None":
#     if coffee_maker_oop.is_resource_sufficient(menu_item_oop) == True:
#         coffee_maker_oop.make_coffee(menu_item_oop)

# print(coffee_maker_oop.report())
# print(money_machine_oop.report())

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)