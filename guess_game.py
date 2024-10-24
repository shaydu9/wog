import random


def generate_number(difficulty: int) -> int:
    return random.randint(0, difficulty)


def get_guess_from_user(difficulty):
    while True:
        try:
            guess_num = int(input(f'Please enter a number between 0 to {difficulty}:\n'))
        except ValueError:
            print('Please enter only numbers')
            continue
        if guess_num not in range(0, difficulty + 1):
            print(f'Please enter numbers between 0 to {difficulty}')
        else:
            return guess_num
    return


def compare_results(guess_num, secret_num) -> bool:
    return guess_num == secret_num


def play_guess_game(difficulty):
    secret_number = generate_number(difficulty)
    guess_num = get_guess_from_user(difficulty)
    print(f'The secret number is: {secret_number}, you guessed: {guess_num}\n'
          f'Your guess is: {compare_results(guess_num, secret_number)}')

