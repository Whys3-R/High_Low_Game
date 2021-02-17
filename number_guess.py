import os
import random

# os.system('cls' if os.name == 'nt' else 'clear')
# line of code to clear the terminal

# Introductory text for the program
# The user makes a decision whether they would like to have a number
# or have the computer guess the number
def welcome():
    print("""Welcome to the High Low game.
    This is a number guessing game with 2 different modes of play.""")
    while True:
        print("""Your choices:
        1 : AI vs Player (AI guess)
        2 : Player vs AI (You guess)""")
        mode = input("Which mode would you like to play: ")
        if mode == "1":
            # AI Guesses
            os.system('cls' if os.name == 'nt' else 'clear')
            ai_guess()
            break
        elif mode == "2":
            # Player guess
            os.system('cls' if os.name == 'nt' else 'clear')
            player_guess()
            print()
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Please enter a 1 or 2.")

# This function contains the code if the computer is to guess a number and the 
# player decides the number.
def ai_guess():
    low = 1
    high = 1000
    print("Think of a number between {0} and {1}.".format(low, high))
    print("Press ENTER to start the program.")
    test = input()

    guess = 0
    attempts = 1
    while True:
        guess = low + (high - low) // 2
        hi_lo = input('I\'m going to guess {}. \nEnter:\n"h" if I need to go '
                    'higher.\n"l" if i need to go lower. \n"c" if I\'m '
                    'correct."'.format(guess))
        if hi_lo.lower() == "c":
            print("It took me {} attempts to guess your number."
                .format(attempts))
            input("Press ENTER to end the program")
            break
        elif hi_lo.lower() == "h":
            low = guess +1
            os.system('cls' if os.name == 'nt' else 'clear')
            attempts += 1
        elif hi_lo.lower() == "l":
            high = guess -1
            os.system('cls' if os.name == 'nt' else 'clear')
            attempts += 1
        else:
            print("You did not enter a valid input. Please enter h, c, or l.")

# this function contains the code where the computer generates a number and
# the player guesses   
def player_guess():
    difficulty = set_diff()
    x = random.randint(1, difficulty)
    # print(x)
    print("Okay, I have a number!")
    while True:
        user_in = int(input('Enter your guess: '))
        if user_in > x:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("{} is too high.\nGuess again!".format(user_in))
        elif user_in < x:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("{} is too low.\nGuess again!".format(user_in))
        elif user_in == x:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("You got it!")
            break
    go_again =  input("Would you like to guess another number? (Y/N)")
    if go_again.lower() == 'y':
        player_guess()

def set_diff():
    print("""Please select a difficulty:
    1. Easy (1-100)
    2. Medium (1-1,000)
    3. Hard (1-10,000)
    4. Very Hard (1-100,000)""")
    user_in = input("Enter desired difficulty: ")
    difficulties = {
        "1": 100,
        "2": 1000,
        "3": 10000,
        "4": 100000,
    }
    return difficulties[user_in]

def main():
    welcome()
main()
