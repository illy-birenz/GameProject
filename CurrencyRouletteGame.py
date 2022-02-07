import random

from currency_converter import ECB_URL, CurrencyConverter
import os.path as op
import urllib.request
from datetime import date
import Verify_Non_String


# Properties
# 1. Difficulty

# Methods
# 1. get_money_interval -Will get the current currency rate from USD to ILS and will
# generate an interval as follows:
# a. for given difficulty d, and total value of money t the interval will be: (t - (5 - d), t +
# (5 - d))
# 2. get_guess_from_user - A method to prompt a guess from the user to enter a guess of
# value to a given amount of USD
# 3. play - Will call the functions above and play the game. Will return True / False if the user
# lost or won.


def create_currency_file():
    filename = f"ecb_{date.today():%Y%m%d}.zip"
    if not op.isfile(filename):
        urllib.request.urlretrieve(ECB_URL, filename)
    c = CurrencyConverter(filename, decimal=True)
    return c


def get_money_interval(c, user_difficulty):
    random_amount = random.randint(1, 100)
    # print(c.convert(1, 'USD', 'ILS'))
    print(f"Amount that has been chosen is {random_amount} USD dollars")
    result = c.convert(random_amount, 'USD', 'ILS')
    interval_range = [round(result - (5 - user_difficulty)), round(result + (5 - user_difficulty))]
    return interval_range


def get_guses_from_user():
    guess_from_user = input(
        f"Please enter your estimation of value amount when converting it to ILS, (ranges have been rounded)\n")
    while Verify_Non_String.verify_non_string(guess_from_user) is False:
        guess_from_user = input(
            f"Please enter your estimation of value amount when converting it to ILS, Only numbers!!!\n")
    return guess_from_user


def play(user_difficulty):
    c = create_currency_file()
    interval_range = get_money_interval(c, int(user_difficulty))
    guess_from_user = get_guses_from_user()
    if user_difficulty != "5":
        print(
            f"The range calculated when using difficulty of {user_difficulty} was between {interval_range[0]} to {interval_range[1]}")
    else:
        print(
            f"Difficulty {user_difficulty} has no range, the amount to calculate was exactly {interval_range[0]}")
    if interval_range[0] <= int(guess_from_user) <= interval_range[1]:
        return True
    else:
        return False
