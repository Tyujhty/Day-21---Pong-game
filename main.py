from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
# Deactivate animation
screen.tracer(0)

# Create the paddles
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "z")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move_ball()

    # Detect collision with walls
    if ball.ycor() > 280 or ball.ycor() < - 280:
        ball.bounce_y()
    # Detect collision with paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320
            or ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()
    # Detect when paddles misse
    if ball.xcor() > 380 or ball.xcor() < - 380:
        ball.reset_ball()

screen.exitonclick()
