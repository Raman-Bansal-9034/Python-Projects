# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze
# &url=worlds%2Ftutorial_en%2Fmaze1.json
# go to this url remove all the methods that contain pass keyword and run the below code. It will work fine.

def move():
    pass


def turn_left():
    pass


def at_goal():
    pass


def right_is_clear():
    pass


def is_facing_north():
    pass


def wall_in_front():
    pass


def wall_on_right():
    pass


def front_is_clear():
    pass


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    move()


while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    if is_facing_north() and wall_on_right():
        turn_left()
    if wall_in_front() and wall_on_right():
        turn_left()
    elif front_is_clear():
        move()
