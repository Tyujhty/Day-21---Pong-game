from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 32, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 240)
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.write(f"{self.l_score} | {self.r_score}", align=ALIGN, font=FONT)

    def increase_l_score(self):
        self.l_score += 1
        self.clear()
        self.write(f"{self.l_score} | {self.r_score}", align=ALIGN, font=FONT)

    def increase_r_score(self):
        self.r_score += 1
        self.clear()
        self.write(f"{self.l_score} | {self.r_score}", align=ALIGN, font=FONT)