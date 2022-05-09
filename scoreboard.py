from turtle import Turtle

FONT = ("Arial", 20, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(-0,270)
        self.display_score()
        

    def display_score(self):
        """Display and increase score"""
        self.clear()
        self.write(f"Score: {self.score}", font=FONT)
        self.score += 1
