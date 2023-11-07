from turtle import Turtle

MOVEMENT = 20


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.color("coral1")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.goto(0, -270)

    def move_left(self):
        self.forward(-MOVEMENT)

    def move_right(self):
        self.forward(MOVEMENT)
