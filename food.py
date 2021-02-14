from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        x_random = random.randint(-210, 210)
        y_random = random.randint(-210, 210)
        self.goto(x_random, y_random)
        self.refresh()

    def refresh(self):
        x_random = random.randint(-240, 240)
        y_random = random.randint(-240, 240)
        self.goto(x_random, y_random)

