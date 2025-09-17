import os
from art import logo

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

while True:
    print(logo)
    
    # Questions: Starting Number? Second Number? Operation Type?
    while True:
        starting_number = input("What's the first number? ")
        try:
            float(starting_number)
            break
        except ValueError:
            print("Invalid response. Please type a numerical value only.")
    while True:
        while True:
            operation = input("Pick an operation: ")
            if operation == "+" or operation == "-" or operation == "*" or operation == "/":
                break
            else:
                print("Invalid response. Please type one of the listed operations.")
        while True:
            second_number = input("What's the second number? ")
            try:
                float(second_number)
                break
            except ValueError:
                print("Invalid response. Please type a numerical value only.")

        starting_number = float(starting_number)
        second_number = float(second_number)
        end_calc = operations_dict[operation](starting_number,second_number)

        print(f"{starting_number} {operation} {second_number} = {end_calc}")

        # Question: Continue Calculation?
        while True:
            more_calculations = input(f"Type 'y' to continue calculating with {end_calc}, or type 'n' to start a new calculation: ")
            if more_calculations == "y" or more_calculations == "n":
                break
            else:
                print("Invalid response. Please try again.")

        if more_calculations == "y":
            starting_number = end_calc
        else:
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
            break
