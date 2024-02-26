from random import randint
from number_guessing_game_art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def set_difficulty():
    """  This function returns the difficulty level chosen by the user. """
    level = input("\nChoose a difficulty. Type 'easy' or 'hard' ")
    if level == "hard":
        return HARD_LEVEL_TURNS
    elif level == "easy":
        return EASY_LEVEL_TURNS
    else:
        print("\nYou choose the wrong option.")


def guess_the_number(chances):
    """ This function check whether the number guessed by the user is correct or not."""
    number_not_guessed = True
    print(f"\nyou have {chances} chances to guess the number")
    while number_not_guessed:
        if chances == 0:
            number_not_guessed = False
            print(f"\nYou didn't guessed the right number. You lose.")

        else:
            guess = int(input("\nEnter your guess "))
            chances -= 1
            if number > guess:

                print(f"\nYour Guess is smaller than the number.\nYou have {chances} chances remaining.\n")
            elif number < guess:
                print(f"\nYour Guess is Greater than the number.\nYou have {chances} chances remaining.\n")
            else:
                print(f"\nYou got it! The answer was {number}. You won.")
                number_not_guessed = False


print(logo)
print("\nWelcome to the Number Guessing Game!")
print("\nI'm thinking of a number between 1 and 100.")
# number = random.choice(range(101))
number = randint(1, 100)
# print(number)
guess_the_number(set_difficulty())
