treasure = '''

*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____/__
*******************************************************************************

'''
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
