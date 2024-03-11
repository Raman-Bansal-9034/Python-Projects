from turtle import Screen
import time
from scoreboard import Scoreboard
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = Scoreboard()

screen.listen()  # To make our screen listen for the key press, so that we can make our snake turn around a/c to keys.
screen.onkey(snake.up, "Up")  # Here we are calling function inside another function, so we will pass its name only.
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    # We are going to detect this using a method from the turtle class called distance().
    if snake.head.distance(food) < 15:
        # Here we are checking distance between the head of the snake and the food position.
        # So that we can find, when the snake is going to collide with food.
        # As we know food size is 10 * 10 set by us. so we are comparing it with 15.
        food.refresh()
        snake.extend()
        score_board.increase_score()

    # Detect collision with Wall.
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        score_board.game_over()

    # Detect collision with tail.
    # If head of snake collides with any piece in the tail: trigger game_over.
    for piece in snake.snake_pieces[1:]:
        # if piece == snake.head:
        #     pass
        # Instead of this if statement, we will use list slicing.
        if snake.head.distance(piece) < 5:
            game_is_on = False
            score_board.game_over()

screen.exitonclick()
