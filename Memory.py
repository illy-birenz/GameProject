# Properties
# 1. Difficulty

# Methods
# 1. generate_sequence - Will generate a list of random numbers between 1 to 101. The list
# length will be ​difficulty​.
# 2. get_list_from_user - Will return a list of numbers prompted from the user. The list length
# will be in the size of ​difficulty​.
# 3. is_list_equal - A function to compare two lists if they are equal. The function will return
# True / False.
# 4. play - Will call the functions above and play the game. Will return True / False if the user
# lost or won.
import random
import time
import os
import Verify_Non_String


def generate_sequence(user_difficulty):
    number_list = [1] * int(user_difficulty)
    for i in range(int(user_difficulty)):
        number_list[i] = random.randint(1, 101)
    return number_list


def get_list_from_user(user_difficulty):
    user_number_list = [1] * int(user_difficulty)
    for i in range(int(user_difficulty)):
        user_input = input(f"please enter the {i + 1} number you saw, only numbers will be accepted!!!\n")
        while Verify_Non_String.verify_non_string(user_input) is False:
            user_input = input(
                f"You didn't enter a number!\nplease enter the {i + 1} number you saw, only numbers will be accepted!!!\n")
        user_number_list[i] = int(user_input)
    return user_number_list


def is_list_equal(number_list, user_number_list):
    if number_list == user_number_list:
        return True
    else:
        return False


def play(user_difficulty):
    number_list = generate_sequence(user_difficulty)
    input("Click any key to display list of number, you have 0.7 seconds to remember these numbers\n")
    print(number_list)
    time.sleep(0.7)
    os.system("cls")
    user_number_list = get_list_from_user(user_difficulty)
    did_remember = is_list_equal(number_list, user_number_list)
    print(f"the list displayed was {number_list},\nThe list you typed in is {user_number_list}")
    return did_remember
