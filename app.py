from time import sleep

from currency_roulette_game import play_currency
from guess_game import play_guess_game
from memory_game import play_memory_game

TYPE_DIFFICULTY = 10
TYPE_GAME = 3


class GameCodes:
    GAME_MEMORY = 1
    GAME_GUESS = 2
    GAME_CURRENCY = 3


def welcome():
    username = input("Please enter your name: ")
    print(f'Hi {username} and welcome to the World of Games: The Epic Journey')


def check_validity(top_range) -> int:
    user_input = 'Please choose your game:\n' if top_range == TYPE_GAME else \
        'Please enter the difficulty level between 1 to 10:\n'
    user_range = 'Chosen game is not on the list. Please try again.' if top_range == TYPE_GAME else \
        'Difficulty level must be between 1 to 10. Please try again.'

    while True:
        try:
            result = int(input(user_input))
        except ValueError:
            print('Please enter only numbers.')
            continue
        if result not in range(1, top_range + 1):
            print(user_range)
        else:
            return result


def start_play():
    games = ['1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.',
             '2. Guess Game - guess a number and see if you chose like the computer.',
             '3. Currency Roulette - try and guess the value of a random amount of USD in ILS']

    for game in games:
        print(game)

    chosen_game = check_validity(TYPE_GAME)
    difficulty_level = check_validity(TYPE_DIFFICULTY)
    print(f'You have chosen {games[chosen_game - 1]}, with difficulty level of: {difficulty_level}\nLoading game...')
    sleep(2)
    match chosen_game:
        case GameCodes.GAME_MEMORY:
            play_memory_game(difficulty_level)
        case GameCodes.GAME_GUESS:
            play_guess_game(difficulty_level)
        case GameCodes.GAME_CURRENCY:
            play_currency(difficulty_level)
        case _:
            return
