from caesar_cipher_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
            'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z']


def caesar(cipher_direction, start_text, shift_amount):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            index_of_current_letter = alphabet.index(char)
            index_of_shifted_letter = index_of_current_letter + shift_amount
            end_text += alphabet[index_of_shifted_letter]
        else:
            end_text += char
    print(f"The {cipher_direction}d message is : \n {end_text}")


print(logo)
should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
    if direction == "encode":
        text = input("Type your message to encode : \n").lower()
    else:
        text = input("Type your encoded message to decode : \n").lower()

    shift = int(input("Type the shift number : \n"))
    shift %= 26
    caesar(cipher_direction=direction, start_text=text, shift_amount=shift)
    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result == "no":
        should_continue = False
        print("Goodbye")
