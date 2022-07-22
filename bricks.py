from turtle import Turtle

col = ['yellow', 'green', 'orange', 'red']


class Brick(Turtle):

    def __init__(self, colors):
        super().__init__()
        self.shape("square")
        self.color(colors)
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=2.3)


class Bricks:

    def __init__(self):
        self.x_start = -360
        self.y_start = -70
        self.bricks = []
        self.create_bricks(self.x_start, self.y_start)

    def create_bricks(self, x, y):
        for i in range(0, 4):
            for n in range(0, 2):
                for j in range(0, 14):
                    brick = Brick(colors=col[i])
                    brick.goto(x=x, y=y)
                    self.bricks.append(brick)
                    x += 55
                y += 20
                x = -360
