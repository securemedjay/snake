from tkinter.constants import LEFT, RIGHT
from turtle import Turtle

STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
MOVE_PACE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0



class Snake:

    def __init__(self):
        self.snake_body = []
        for segment in STARTING_POSITION:
            self.grow(segment)
        self.snake_head = self.snake_body[0]

            

    def grow(self, position):
        """Create a new segment, set its position and add it to the snake body"""
        segment = Turtle()
        segment.shape("square")
        segment.penup()
        segment.setposition(position)
        self.snake_body.append(segment)

    
    def extend(self):
        """Pass the position of the last segment of the snake body to grow()"""
        self.grow(self.snake_body[-1].position())



    def move(self):
        for seg_num in range(len(self.snake_body) - 1,0,-1):
            new_x = self.snake_body[seg_num - 1].xcor()
            new_y = self.snake_body[seg_num - 1].ycor()
            self.snake_body[seg_num].setposition(new_x, new_y)
        self.snake_head.forward(MOVE_PACE)

    def move_up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def move_down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def move_right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)

    def move_left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)
