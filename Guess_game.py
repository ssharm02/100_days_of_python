import random
import guessing_game_art

random_number = 0
game_flag = True


def welcome_to_the_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")


def choose_difficulty():
    difficulty_level = input("Choose a difficulty.  Type 'easy', or 'hard': ")
    return difficulty_level


def difficulty_loop():
    life_level = choose_difficulty()
    loop_game = 0
    if life_level == "hard":
        loop_game = 5
    elif life_level == "easy":
        loop_game = 10
    else:
        print("Please enter a valid option")
        choose_difficulty()
    return loop_game


def user_number():
    user_guess = int(input("Make a guess: "))
    return user_guess


def generate_random_number():
    global random_number
    random_number = random.randint(1, 101)
    # print("global rand is ")
    print(random_number)
    return random_number


def winning_conditions():
    global game_flag
    user_num = user_number()
    # comp_num = generate_random_number()
    if user_num < random_number:
        print("Too Low \nGuess Again")
    elif user_num > random_number:
        print("Too High \nGuess Again")
    elif user_num == random_number:
        game_flag = False
        print("You win! Correct answer")


def game_loop():
    num_tries = difficulty_loop()
    while num_tries > 0 and game_flag is not False:
        winning_conditions()
        num_tries -= 1
        if game_flag is True:
            print(f"You have {num_tries} attempts remaining to guess the number.")

print(guessing_game_art.logo)
welcome_to_the_game()
generate_random_number()
game_loop()
