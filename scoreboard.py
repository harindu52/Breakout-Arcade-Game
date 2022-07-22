from turtle import Turtle

ALIGNMENT = "center"

try:
    high_score = int(open('highestScore.txt', 'r').read())
except FileNotFoundError:
    high_score = open('highestScore.txt', 'w').write(str(0))
except ValueError:
    high_score = 0


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.game_end = False
        self.color("white")
        self.hideturtle()
        self.penup()
        self.score = 0
        self.lives = 3
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(130, 250)
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=("Courier", 30, "bold"))
        self.goto(-180, 250)
        self.write(f"{self.live(self.lives)}", align=ALIGNMENT, font=("Courier", 30, "bold"))

    def up_score(self, color):
        if color == "yellow":
            self.score += 1
        elif color == "green":
            self.score += 2
        elif color == "orange":
            self.score += 5
        elif color == "red":
            self.score += 10
        self.update_scoreboard()

    def update_lives(self):
        self.lives -= 1
        self.update_scoreboard()
        if self.lives == 0:
            self.game_end = True

    def game_over(self):
        self.goto(0, 150)
        self.write(f"GAME OVER!", align=ALIGNMENT, font=("Courier", 50, "bold"))
        self.goto(0, 120)
        if self.score > high_score:
            open('highestScore.txt', 'w').write(str(self.score))
            self.write(f"High score : {self.score}", align=ALIGNMENT, font=("Courier", 30, "normal"))
            if self.score == 504:
                self.game_end = True
        else:
            self.write(f"High score : {high_score}", align=ALIGNMENT, font=("Courier", 30, "normal"))

    @staticmethod
    def live(num):
        hearts = f"❤❤❤"
        if num == 2:
            hearts = f"❤❤"
        elif num == 1:
            hearts = f"❤"
        elif num == 0:
            hearts = f"💔"
        return hearts


class Score(Turtle):
    def __init__(self):
        super(Score, self).__init__()
        self.penup()
        self.hideturtle()

    def print_score(self, x, y, color):
        self.goto(x, y)
        self.color(color)
        if color == "yellow":
            self.write(f"+1", align=ALIGNMENT, font=("Courier", 10, "normal"))
        elif color == "green":
            self.write(f"+2", align=ALIGNMENT, font=("Courier", 10, "normal"))
        elif color == "orange":
            self.write(f"+5", align=ALIGNMENT, font=("Courier", 10, "normal"))
        elif color == "red":
            self.write(f"+10", align=ALIGNMENT, font=("Courier", 10, "normal"))
