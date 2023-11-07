from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 23, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("DarkOliveGreen")
        self.penup()
        self.hideturtle()

    def update_score(self, lives, score):
        self.clear()
        self.goto(0, 250)
        self.write(f"Lives: {lives} | Score: {score}", align=ALIGNMENT, font=FONT)

    def game_over(self, score):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        self.goto(0, -40)
        self.write(f"Your score is: {score}", align=ALIGNMENT, font=FONT)

    def you_won(self, score):
        self.clear()
        self.goto(0, 0)
        self.write("YOU WON!", align=ALIGNMENT, font=FONT)
        self.goto(0, -40)
        self.write(f"Your score is: {score}", align=ALIGNMENT, font=FONT)
