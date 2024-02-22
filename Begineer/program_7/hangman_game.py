import hangman_words
import random
from hangman_art import logo, stages

chosen_word = random.choice(hangman_words.words_list).lower()
length = len(chosen_word)

end_of_game = False

lives = 6

display = []

print(logo)

for blank in range(length):
    display += "_"

# print(display)  # This line will print like ['_', '_', '_', '_', '_']

print(f"Guess {length} letter words : {' '.join(display)}\n")
# To print like this _ _ _ _ _. we are using above join function.
# So that it still remains a list but pattern is printed like this.


while not end_of_game:
    guess = input("\nGuess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}.\n")
    for position in range(length):
        if guess == chosen_word[position]:
            print(f"\nYou guessed letter {guess},that's correct.")
            display[position] = guess

    if guess not in chosen_word:
        print(f"\nYou guessed letter {guess},that's not in the word.You lose a live.\n{lives-1} live remaining. "
              f"\n {stages[(lives * -1)]}")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You loose.\nCorrect Ans was: {chosen_word}")
            # print(f"Your final result is :{display}")
            break
        # Join all the elements in the list and turn it into String.
    print(f"{' '.join(display)}")

    if "_" not in display:  # In is used to check whether a particular element(_) exists in a list(display) or not.
        end_of_game = True
        print("You Guessed it all right.You won")
