import random

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
           'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
           'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
           'Y', 'Z']

symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']

print("\nWelcome to the password generator program!\n")

in_letters = int(input("How many letters do you want in your password? "))
in_symbols = int(input("How many symbols do you want in your password? "))
in_digits = int(input("How many digits do you want in your password? "))

password = ""

for _ in range(in_letters):
    password += random.choice(letters)
    # This random.choice() function will loop through our letters list and will give a random letter.

for _ in range(in_symbols):
    password += random.choice(symbols)
    # Similarly, it will also loop through our symbol list, and give a random symbol from our list.

for _ in range(in_digits):
    password += random.choice(numbers)

# Shuffle the characters in the password
password_list = list(password)
random.shuffle(password_list)
password = ''.join(password_list)  # Performing join operation on an empty String.

print(f"Your password is {password}")
