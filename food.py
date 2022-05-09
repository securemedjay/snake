from turtle import Turtle
from random import randint,choice

ORIENTATION = [0, 90, 180, 270]

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.speed("fastest")
        self.refresh_food()

    def refresh_food(self):
        self.setheading(randint(0, 359))
        self.goto(randint(-280,280), randint(-280,280))

    
