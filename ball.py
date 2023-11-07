from turtle import Turtle

INCREMENT = 20


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("DarkSlateGray4")
        self.penup()
        self.goto(0, -250)
        # self.speed("fastest")
        self.x_inc = 0
        self.y_inc = 1
        self.starting = True

    def set_position(self, xcor):
        self.goto(xcor, -250)

    def reset_position(self):
        self.x_inc = 0
        self.y_inc = 1
        self.starting = True

    def start_playing(self):
        self.starting = False

    def move(self):
        x_pos = self.xcor() + self.x_inc * INCREMENT
        y_pos = self.ycor() + self.y_inc * INCREMENT
        self.goto(x_pos, y_pos)

    def x_switch(self):
        self.x_inc *= -1

    def y_switch(self):
        self.y_inc *= -1

    def plus_x(self):
        self.x_inc += 0.5

    def minus_x(self):
        self.x_inc -= 0.5
