print("Welcome to the tip calculator!")

bill = float(input("What was the total bill?\n$"))
tip = float(input("What percentage tip would you like to give? 10, 12, 15?\n"))
people = int(input("How many people to split the bill?\n"))

final_bill = round(((bill*(tip/100))+bill), 2)
bill_per_person = round(((bill*(tip/100))+bill)/people, 2)

print(f"Total Amount: ${final_bill}")
print(f"Each person should pay: ${bill_per_person}")
