def welcome():
    username = input("Please enter your name: ")
    print(f'Hi {username} and welcome to the World of Games: The Epic Journey')


def start_play():
    games = ['1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.',
             '2. Guess Game - guess a number and see if you chose like the computer.',
             '3. Currency Roulette - try and guess the value of a random amount of USD in ILS']
    print('Please choose a game to play:')
    for game in games:
        print(game)
    chosen_game = int(input())
    if 0 < chosen_game <= 3:
        difficulty_level = int(input("Please choose difficulty level between 1 and 5: "))
        if 0 < difficulty_level <= 5:
            print(f'You have chosen {games[chosen_game]}\nAnd difficulty level of: {difficulty_level}')
        else:
            print('Difficulty level not supported.')
    else:
        print('Game number does not exists')

