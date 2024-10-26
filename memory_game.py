import random
import os
from time import sleep

import app


# from helper import play_again


def generate_sequence(length: int):
    return [random.choice(range(101)) for _ in range(length)]


def get_list_from_user(difficulty: int):
    print(f"Please type the list of {difficulty} numbers you remember, divided by ',':\n")
    return list(map(int, input().strip().split(',')))[:difficulty]


def is_list_equal(generated_list, guessed_list) -> bool:
    return generated_list == guessed_list


def play_memory_game(difficulty: int):
    generated_list = generate_sequence(difficulty)
    print(f'This is the list: {generated_list}...Try to remember!')
    sleep(0.7)
    os.system('clear')
    guessed_list = get_list_from_user(difficulty)
    print(f'You guessed: {guessed_list}, generated list was: {generated_list}.\n'
          f'Your guess is {is_list_equal(generated_list, guessed_list)}')
    app.play_again()

