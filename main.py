from turtle import Screen
import time

from food import Food
from snake import Snake
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("azure2")
screen.title("My Snake Game!")
screen.tracer(0)  # Animation switched off for smooth  movement of snake along with the body

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()

# Controlling the snake
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
score.write_score()
food.refresh()

while game_is_on:
    screen.update()
    time.sleep(0.1)

    # Following subsequent turtles for the latter part of the snake to follow the head
    snake.move()

    # Detect collision with food
    if snake.turtles[0].distance(food) < 15:
        food.refresh()
        score.update_score()
        snake.extend()

    # Detect collision with wall:
    if snake.turtles[0].xcor() > 290 or snake.turtles[0].ycor() < -290 or snake.turtles[0].ycor() > 290 or snake.turtles[0].xcor() < -290:
        score.reset()
        snake.reset()

    # Detect collision with tail:
    for seg in snake.turtles[1:]:
        if snake.turtles[0].distance(seg) < 10:
            score.reset()
            snake.reset()
screen.exitonclick()
