from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.shapesize(0.5, 0.5)
        self.color('blue')
        self.speed(0)
        self.pos()

    def pos(self):
        pos = (random.randint(-290, 290), random.randint(-290, 290))
        self.goto(pos)

