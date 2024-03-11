from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_pieces = []
        self.create_snake()
        self.head = self.snake_pieces[0]
        # Here this line of code must be below the other 2 lines, because once some segments are created,

    #   # only then we can access 0 location, else it will give error.
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_new_snake_piece(position)

    def add_new_snake_piece(self, position):
        new_snake_piece = Turtle(shape="square")
        new_snake_piece.penup()
        new_snake_piece.shapesize(stretch_len=0.5, stretch_wid=0.5)
        new_snake_piece.color("white")
        new_snake_piece.goto(position)
        self.snake_pieces.append(new_snake_piece)

    def extend(self):
        self.add_new_snake_piece(self.snake_pieces[-1].position())

    def move(self):
        for snake_num in range(len(self.snake_pieces) - 1, 0, -1):
            new_x = self.snake_pieces[snake_num - 1].xcor()
            new_y = self.snake_pieces[snake_num - 1].ycor()
            self.snake_pieces[snake_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
