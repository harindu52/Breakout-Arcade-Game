from ball import Ball
from turtle import Screen
import time
from bricks import Bricks
from paddle import Paddle
from scoreboard import ScoreBoard, Score
from boundaries import Boundaries

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.listen()
screen.tracer(0)
screen.title("Breakout Classic")

ping_ball = Ball()
paddle = Paddle()
bricks_all = Bricks()
score_board = ScoreBoard()
brick_score = Score()
bounds = Boundaries()
game_on = True

screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")

move_speed = 0.1


def bounce_speed(color):
    global move_speed
    if color == "yellow":
        move_speed = 0.1
    elif color == "green":
        move_speed = 0.09
    elif color == "orange":
        move_speed = 0.07
    elif color == "red":
        move_speed = 0.05
    return move_speed


def collision_bricks():
    for brick in bricks_all.bricks:
        if ping_ball.distance(brick) < 20:
            brick_score.goto(3000, 3000)
            brick_score.clear()
            x_pos = brick.xcor()
            y_pos = brick.ycor()
            brick_score.print_score(x_pos, y_pos - 11, brick.color()[1])
            ping_ball.move_speed = bounce_speed(brick.color()[1])
            brick.clear()
            brick.goto(3000, 3000)
            bricks_all.bricks.remove(brick)
            ping_ball.bounce_y()
            score_board.up_score(brick.color()[1])
            break


def collision_paddle():
    if paddle.distance(ping_ball) < 50 and ping_ball.ycor() < -250:
        ping_ball.bounce_y()


while game_on:
    screen.update()
    ping_ball.move()
    time.sleep(ping_ball.move_speed)
    collision_bricks()
    collision_paddle()
    if ping_ball.xcor() > 370 or ping_ball.xcor() < -370:
        ping_ball.bounce_x()

    if ping_ball.ycor() > 230:
        ping_ball.bounce_y()

    if ping_ball.ycor() < -260:
        ping_ball.reset_ball()
        paddle.reset_paddle()
        score_board.update_lives()
        if score_board.game_end:
            score_board.game_over()
            game_on = False


screen.exitonclick()
