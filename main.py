import random
import hangman_art
import hangman_words
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def password_generator():
    print("Welcome to the PyPassword Generator!")
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))
    password = ''
    password_list = []

    for char in range(1, nr_letters + 1):
        password_list.append(random.choice(letters))

    for char in range(1, nr_symbols + 1):
        password_list += random.choice(symbols)

    for char in range(1, nr_numbers + 1):
        password_list += random.choice(symbols)

    random.shuffle(password_list)

    for char in password_list:
        password += char
    print(password)


def hangman():
    print(hangman_art.logo)
    display = []

    chosen_word = random.choice(hangman_words.word_list)
    word_length = len(chosen_word)
    lives = 6

    for _ in chosen_word:
        display.append('_')

    end_of_game = False

    while not end_of_game:
        guess = input("Please guess a letter: ").lower()
        print('\n' * 25)

        if guess in display:
            print(f"You already guessed this letter {letter}")

        for position in range(word_length):
            letter = chosen_word[position]

            if letter == guess:
                display[position] = letter

        if guess not in chosen_word:
            print(f"You guessed an incorrect letter and lost a life {letter}")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lose")

        print(f"{' '.join(display)}")

        if "_" not in display:
            end_of_game = True
            print("You win")

        print(hangman_art.stages[lives])
