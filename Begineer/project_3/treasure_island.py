from treasure_art import treasure

print(treasure)

print("Welcome To Treasure Island.Your Mission Is To Find The Treasure.\n")


direction = input('You\'re at a crossroad, where do you want to go? Type "left" or "right".\n').lower()
if direction == "right":
    print("You fell into a hole.Game Over.\n")
elif direction == "left":
    wait = input('You\'ve come to a lake.There is an island in the middle of the lake.'
                 'Type "wait" to wait for a boat.Type "swim" to swim across.\n').lower()
    if wait == "swim":
        print("You got attacked by crocodile.Game Over \n")
    elif wait == "wait":
        gate = input("Which gate do you want to choose?  Red, Blue, yellow \n").lower()
        if gate == "yellow":
            print("Congratulations. You found the treasure.")
        else:
            print("Sorry.You got burn out.\n")
