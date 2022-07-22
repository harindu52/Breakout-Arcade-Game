from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=0.5, stretch_len=4)
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.goto(0, -270)

    def go_left(self):
        new_x = self.xcor() - 60
        self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + 60
        self.goto(new_x, self.ycor())

    def reset_paddle(self):
        self.goto(0, -270)
