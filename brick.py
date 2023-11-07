from turtle import Turtle


class Brick(Turtle):

    def __init__(self, brick_tuple):
        super().__init__()
        self.color("aquamarine3")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.goto(brick_tuple)
