# Properties
# 1. Difficulty - game_difficulty
# 2. Secret number - secret_number
#
# 1. generate_number - Will generate number between 1 to difficulty and save it to
# secret_number.
# 2. get_guess_from_user - Will prompt the user for a number between 1 to difficulty and
# return the number.
# 3. compare_results - Will compare the the secret generated number to the one prompted
# by the get_guess_from_user.
# 4. play - Will call the functions above and play the game. Will return True / False if the user
# lost or won
import random


def generate_number(user_difficulty):
    secret_number = random.randint(1, 1 + int(user_difficulty))
    return secret_number


def get_guess_from_user(game_difficulty, game_range_min):
    game_difficulty_max = int(game_difficulty) + game_range_min
    game_difficulty_min = str(game_range_min)
    guess_from_user = input(f"Please enter the number you guess, it should be between {game_difficulty_min} to {str(game_difficulty_max)}\n")
    return guess_from_user


def compare_results(secret_number, guess_from_user):
    if str(secret_number) == guess_from_user:
        return True
    else:
        return False


def play(game_difficulty, game_difficulty_min):
    secret_number = generate_number(game_difficulty)
    guess_from_user = get_guess_from_user(game_difficulty, game_difficulty_min)
    did_guess = compare_results(secret_number, guess_from_user)
    print(f"you guessed {guess_from_user} and the secret number is {secret_number}")
    return did_guess
