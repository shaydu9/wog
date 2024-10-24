import math
import random

from currency_converter import CurrencyConverter


def get_money_interval(usd: int) -> int:
    return int(CurrencyConverter().convert(usd, 'USD', 'ILS'))


def get_guess_from_user(usd) -> int:
    return int(input(f'How much is {usd}$ converted to ILS? '))


def compare_results(result: int, guess: int, difficulty: int) -> bool:
    interval = 10 - difficulty
    return abs(guess - result) <= interval


def play_currency(difficulty):
    rand_usd = random.randint(0, 100)
    guess = get_guess_from_user(rand_usd)
    result = get_money_interval(rand_usd)
    print(f'{rand_usd}$ converted to ILS is: {result}₪.\n'
          f'Your guess ({guess})₪ is {compare_results(result, guess, difficulty)}')


