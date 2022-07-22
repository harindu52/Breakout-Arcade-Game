from turtle import Turtle


class Boundary(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.lines = []
        self.goto(x, y)


class Boundaries:

    def __init__(self):
        self.lines = []
        self.horizontal_lines()

    def horizontal_lines(self):
        for i in range(0, 5):
            if i == 0:
                boundary = Boundary(0, 250)
                boundary.shapesize(stretch_wid=0.5, stretch_len=40)
                self.lines.append(boundary)
            if i == 1:
                boundary = Boundary(0, 300)
                boundary.shapesize(stretch_wid=0.5, stretch_len=40)
                self.lines.append(boundary)
            if i == 2:
                boundary = Boundary(0, -290)
                boundary.shapesize(stretch_wid=0.5, stretch_len=40)
                self.lines.append(boundary)
            if i == 3:
                boundary = Boundary(-395, 0)
                boundary.shapesize(stretch_wid=29.5, stretch_len=0.5)
                self.lines.append(boundary)
            if i == 4:
                boundary = Boundary(390, 0)
                boundary.shapesize(stretch_wid=29.5, stretch_len=0.5)
                self.lines.append(boundary)
