from art import logo

# Logo & Alphabet Lists
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
print(logo)

# Caesar's Cipher Loop
while True:

    # Questions: Encode or Decode?, Text?, Shift Number?
    while True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        if direction == "encode" or direction == "decode":
            break
        else:
            print("Invalid response. Please try again.")

    text = input("Type your message:\n").lower()

    while True:
        shift = input("Type the shift number:\n")
        try:
            int(shift) > 0
            break
        except ValueError:
            print("Invalid response. Please type a numerical value greater than 0.")
    shift = int(shift)


    # Encrypt/Decrypt Function
    def caesar(original_text, shift_amount):
        if direction == "encode":
            encrypted_text = ""
            alp_length = (len(alphabet)) - 1
            for letter in original_text:
                if letter in alphabet:
                    alp_position = alphabet.index(letter) + shift_amount
                    while alp_position > alp_length:
                        alp_position -= (alp_length + 1)
                    encrypted_letter = alphabet[alp_position]
                    encrypted_text += encrypted_letter
                elif letter not in alphabet:
                    encrypted_text += letter
            print(f"Here is your encoded result: {encrypted_text}")
        elif direction == "decode":
            deciphered_text = ""
            alp_length = len(alphabet)
            for letter in original_text:
                if letter in alphabet:
                    alp_position = alphabet.index(letter) - shift_amount
                    while alp_position < 0:
                        alp_position += alp_length
                    encrypted_letter = alphabet[alp_position]
                    deciphered_text += encrypted_letter
                elif letter not in alphabet:
                    deciphered_text += letter
            print(f"Here is your decoded result: {deciphered_text}")


    # Calling Function
    caesar(text, shift)

    # Question: Would you like to continue Caesar's Cipher?
    while True:
        continue_cipher = input("Would you like to continue?\n" + "Please enter 'Yes' or 'No': ").lower()
        if continue_cipher == "no":
            break
        elif continue_cipher == "yes":
            break
        else:
            print("Invalid response. Please try again.")

    # End Code or Restart
    if continue_cipher == "no":
        print("Good Bye...")
        break