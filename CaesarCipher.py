import CaesarArt

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(plain_text, shift_amount, cipher_direction):
    cipher_text = ''
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)
            if cipher_direction == "decode":
                new_position = position + shift_amount
            elif cipher_direction == "encode":
                new_position = position - shift_amount
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        else:
            cipher_text += char

    print(f"{cipher_direction}d text is {cipher_text}")


def check_user_input(plain_text):
    for char in plain_text:
        if char in alphabet:
            print("All good")
        else:
            print("user entered bad character Please renter an alphabetic character")


def user_option(user_text, user_shift, user_direction):
    if user_direction == "encode" or user_direction == "decode":
        caesar(plain_text=user_text, shift_amount=user_shift, cipher_direction=user_direction)
    else:
        print("Please enter a valid option")


def main():
    print(CaesarArt.logo)
    should_continue = True
    while should_continue:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        shift = shift % 26
        user_option(user_text=text, user_shift=shift, user_direction=direction)
        result = input("Type 'yes' to continue or enter 'no' to exit")
        if result == 'no':
            should_continue = False
            print("GoodBye")

main()