from higher_lower_game_art import logo, vs
from higher_lower_game_data import data
import random


def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(guess_by_user, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return guess_by_user == "a"
    else:
        return guess_by_user == "b"


print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)


while game_should_continue:

    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    guess = input("\nWho has more followers? Type 'A' or 'B': ").lower()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    print(logo)

    if is_correct:
        score += 1
        print(f"\nYou're right! Current score: {score}.\n")
    else:
        game_should_continue = False
        print(f"\nSorry, that's wrong. Final score: {score}.")

