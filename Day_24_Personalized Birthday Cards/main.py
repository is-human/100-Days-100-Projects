#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open(r"Input/Names/invited_names.txt", "r") as names_file:
    names_manager = names_file.readlines()

names_manager = [name.replace("\n", "") for name in names_manager]

with open(r"Input/Letters/starting_letter.txt", "r") as starting_file:
    content = starting_file.read()

for i in names_manager:
    new_content = content.replace("[name]", f"{i}")
    with open(f"Output/ReadyToSend/letter_{i}.txt", "w") as new_file:
        new_file.write(new_content)