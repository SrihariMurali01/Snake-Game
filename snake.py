import random
import turtle
from turtle import Turtle

start_pos = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()


    def snake_colors(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return (r, g, b)

    def create_snake(self):
        for pos in start_pos:
            self.add_turtle(pos)

    def add_turtle(self, pos):
        turtle.colormode(255)
        new_turtle = Turtle(shape='square')
        new_turtle.penup()
        new_turtle.color(self.snake_colors())
        new_turtle.goto(pos)
        self.turtles.append(new_turtle)

    def extend(self):
        # Adding a new segment to the snake.
        self.add_turtle(self.turtles[-1].position())

    def move(self):
        for seg_num in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[seg_num - 1].xcor()
            new_y = self.turtles[seg_num - 1].ycor()
            self.turtles[seg_num].goto(new_x, new_y)
        self.turtles[0].forward(move_distance)

    def up(self):
        if self.turtles[0].heading() != DOWN:
            self.turtles[0].setheading(UP)

    def down(self):
        if self.turtles[0].heading() != UP:
            self.turtles[0].setheading(DOWN)

    def left(self):
        if self.turtles[0].heading() != RIGHT:
            self.turtles[0].setheading(LEFT)

    def right(self):
        if self.turtles[0].heading() != LEFT:
            self.turtles[0].setheading(RIGHT)

    def reset(self):
        for seg in self.turtles:
            seg.goto(1000, 1000)
        self.turtles.clear()
        self.create_snake()
