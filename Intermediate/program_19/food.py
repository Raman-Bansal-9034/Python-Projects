import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) # This will create a 10*10 circle.
        self.color("blue")
        self.speed("fastest")
        # All these methods are coming from super class, and we can access them because we are inheriting the class.
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)


# All of these above steps will be performed as soon as we create a new food object from the food class.
# Whenever we initialize a new object, from the class, the __init__ method get called.
