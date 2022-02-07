import os
import sys

game_type_min_range = 1
game_type_max_range = 3
game_difficulty_min = 1
game_difficulty_max = 5


def verify_input_len(string, min_len):
    while len(string) < min_len:
        string = input("You didn't write any name, please enter your name, one character at least, tnx :)\n")
    return string


def verify_range(num, min_range, max_range):
    if min_range > num or num > max_range:
        return False
    return num


def verify_non_string(input_test):
    if input_test == "quit":
        print("u have chosen to quit the program")
        sys.exit(0)
    try:
        input_test = int(input_test)
    except ValueError:
        print(f"Value error, you can only insert numbers, characters or strings will not be accepted -> value entered was '{input_test}'")
        return False
    except TypeError:
        print(f"Type error, you can only insert numbers, characters or strings will not be accepted -> value entered was '{input_test}'")
        return False
    return input_test


def welcome(name):
    name = verify_input_len(name, 1)
    return f"Hello {name} and welcome to the World of Games (WoG).\n" \
           "Here you can find many cool games to play."


def game_type_print():
    game_type_mode = input("\nPlease choose a game to play,:\n    "
                           "1. Memory Game - a sequence of numbers will appear for 1 second and you have to"
                           " guess it back\n    "
                           "2. Guess Game - guess a number and see if you chose like the computer\n    "
                           "3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n    ")
    return game_type_mode


def game_difficulty_mode_print():
    game_diff_input = input(f"Please choose game difficulty from {game_difficulty_min} to {game_difficulty_max}\n")
    return game_diff_input


# string_with_name = f"Hello {person_name} and welcome to the World of Games (WoG).\n" \
#                    "Here you can find many cool games to play."
# return string_with_name

def quit_message():
    input("\n *** Please note that from here on, you can type 'quit' (without ') at any input line in order to quit\n,"
          "press Enter to continue... ***\n")
    os.system("cls")


def load_game():
    game_type = game_type_print()
    while verify_non_string(game_type) is False:
        game_type = game_type_print()
    while not verify_range(int(game_type), game_type_min_range, game_type_max_range):
        game_type = input(
            f"Type selection is wrong, you typed: '{game_type}', please choose value between {game_type_min_range} and {game_type_max_range}\n")
        while not verify_non_string(game_type):
            game_type = input(
                f"Type selection is wrong, you typed: '{game_type}', please choose value between {game_type_min_range} and {game_type_max_range}\n")

    game_difficulty = game_difficulty_mode_print()
    while verify_non_string(game_difficulty) is False:
        game_difficulty = game_difficulty_mode_print()
    while not verify_range(int(game_difficulty), game_difficulty_min, game_difficulty_max):
        game_difficulty = input(
            f"Difficulty selection is wrong, you typed: '{game_difficulty}', please choose value between {game_difficulty_min} and {game_difficulty_max}\n")
        while not verify_non_string(game_difficulty):
            game_difficulty = input(
                f"Difficulty selection is wrong, you typed: '{game_difficulty}', please choose value between {game_difficulty_min} and {game_difficulty_max}\n")
    feedback_to_gamer(game_type, game_difficulty)


def feedback_to_gamer(game_type, game_difficulty):
    if game_type == "1":
        print("\nGame chosen to play was 'Memory game'")
    elif game_type == "2":
        print("\nGame chosen to play was 'Guess game'")
    else:
        print("\nGame chosen to play was 'Currency Roulette' game")
    print(f"Difficulty chosen was {game_difficulty}\n"
          "Thank you for playing")


person_name_input = input("Please enter your name\n")
welcome_message = welcome(person_name_input)
print(welcome_message)
quit_message()
load_game()
