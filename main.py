from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from blocks import Blocks
import time

screen = Screen()
screen.bgpic("./imgs/background.gif")
screen.setup(width=1000, height=800)
screen.title("Breakout")
screen.tracer(0)

screen.addshape("./imgs/ball.gif")
screen.addshape("./imgs/paddle.gif")

paddle = Paddle((0, -380))
ball = Ball()
blocks = Blocks()
scoreboard = Scoreboard(blocks)

screen.listen()
screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")

game_is_on = True
while game_is_on:
    time.sleep(0.01)
    screen.update()
    ball.move()

    # Detect collision with x wall
    if ball.xcor() > 480 or ball.xcor() < -480:
        ball.bounce_x()

    # Detect collision with y wall
    if ball.ycor() > 380:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(paddle) < 100 and ball.ycor() < -360:
        if ball.xcor() > paddle.xcor():
            # Ball hits the right half of the paddle
            ball.setx(paddle.xcor() + 50)  # Ensure ball moves to the right side
            ball.x_move = abs(ball.x_move)  # Ensure ball moves right on x-axis
        else:
            # Ball hits the left half of the paddle
            ball.setx(paddle.xcor() - 50)  # Ensure ball moves to the left side
            ball.x_move = -abs(ball.x_move)  # Ensure ball moves left on x-axis
        ball.bounce_y()

    # Detect paddle miss
    if ball.ycor() < -390 and ball.distance(paddle) > 10:
        ball.reset_position()
        scoreboard.minus_lives()

    # Detect collision with blocks
    blocks.detect_collision(ball)
    scoreboard.update_scoreboard()

    # Game over
    if scoreboard.lives == 0:
        scoreboard.game_over()
        game_is_on = False

    # Game win
    if blocks.get_blocks_removed() == blocks.get_block_count():
        scoreboard.game_win()
        game_is_on = False

screen.exitonclick()
