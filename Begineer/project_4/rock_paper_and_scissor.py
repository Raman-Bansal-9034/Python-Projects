import random
from rock_paper_and_scissor_art import *

game_images = [rock_sign, paper_sign, scissor_sign]
game_keyword = ("rock", "paper", "scissor")

print(hello)

user_choice = int(input("What do you choose ? Type 0 for Rock, 1 For paper, and 2 for Scissor "))
choice = ""

if user_choice > 2:
    print("You typed a Wrong number. You loose.")
else:
    print(f"\nYou chooses: {game_keyword[user_choice]}")
    print(game_images[user_choice])

computer_choice = random.randint(0, 2)

print(f"Computer chooses: {game_keyword[computer_choice]} \n {game_images[computer_choice]}")

if user_choice == computer_choice:
    print("Match Draw.")
elif user_choice == 0 and computer_choice == 1:
    print("You Lose! Computer Wins.")
elif user_choice == 0 and computer_choice == 2:
    print("You Win! Computer Loose.")
elif user_choice == 1 and computer_choice == 0:
    print("You Win! Computer Loose.")
elif user_choice == 1 and computer_choice == 2:
    print("You Loose! Computer Wins.")
elif user_choice == 2 and computer_choice == 0:
    print("You Loose! Computer Wins.")
elif user_choice == 2 and computer_choice == 1:
    print("You Win! Computer Loose.")
