from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from brick import Brick
from maze import mazes
import time

NO_OF_LIVES = 3

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("AntiqueWhite")
screen.title("Breakout game")
screen.tracer(0)

paddle = Paddle()
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle.move_left, "Left")
screen.onkey(paddle.move_right, "Right")
screen.onkey(ball.start_playing, "Up")

lives = NO_OF_LIVES
score = 0
game_is_on = True

# to chose maze one by one
for maze in mazes:
    bricks = []
    screen.update()

    # to enable the game, if you're still alive
    if lives != 0:
        game_is_on = True

        # to build up the maze from bricks
        for brick_tuple in maze:
            brick = Brick(brick_tuple)
            bricks.append(brick)

    # to play the game
    # while game_is_on:
    scoreboard.update_score(lives, score)
    print(f"lives left: {lives}")
    print("starting while")
    game_starting = True

    # to move paddle together with ball before bouncing the ball
    while game_starting:
        screen.update()
        time.sleep(0.1)
        x_cor = paddle.xcor()
        ball.set_position(x_cor)
        game_starting = ball.starting

    game_running = True
    print("running while")

    # to let the ball running
    while game_running:
        screen.update()
        time.sleep(0.1)
        ball.move()

        # collision with side walls
        if ball.xcor() > 280 or ball.xcor() < -280:
            ball.x_switch()

        # collision with top wall
        if ball.ycor() > 280:
            ball.y_switch()

        # collision with paddle
        if ball.distance(paddle) < 30 and ball.ycor() < -230:
            ball.y_switch()

        if 30 < ball.distance(paddle) < 60 and ball.ycor() < -230 and ball.xcor() > paddle.xcor():
            ball.y_switch()
            ball.plus_x()

        if 30 < ball.distance(paddle) < 60 and ball.ycor() < -230 and ball.xcor() < paddle.xcor():
            ball.y_switch()
            ball.minus_x()

        # falling to the bottom
        if ball.ycor() < -300:
            game_running = False
            ball.reset_position()
            lives -= 1

        # collision with brick
        for brick in bricks:
            if abs(ball.ycor() - brick.ycor()) < 20 and abs(ball.xcor() - brick.xcor()) < 60:
                bricks.remove(brick)
                brick.goto(1080, 0)
                ball.y_switch()
                print(f"bricks left: {len(bricks)}")

        # out of bricks
        if len(bricks) == 0:
            score += 1
            ball.reset_position()
            scoreboard.you_won(score)
            game_running = False
            # game_is_on = False

        # out of lives
        if lives == 0:
            scoreboard.game_over(score)
            game_running = False
            # game_is_on = False

screen.exitonclick()
