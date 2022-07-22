from turtle import Turtle
MOVE_SPEED = 0.1


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5)
        self.color("white")
        self.penup()
        self.goto(0, -200)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = MOVE_SPEED

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1

    def reset_ball(self):
        self.goto(0, -200)
        self.move_speed = 0.1
        self.bounce_y()

    # def bounce_speed(self, color):
    #     global MOVE_SPEED
    #     if color == "yellow":
    #         MOVE_SPEED = 0.1
    #     elif color == "green":
    #         MOVE_SPEED = 0.09
    #     elif color == "orange":
    #         MOVE_SPEED = 0.07
    #     elif color == "red":
    #         MOVE_SPEED = 0.05
    #     return MOVE_SPEED
