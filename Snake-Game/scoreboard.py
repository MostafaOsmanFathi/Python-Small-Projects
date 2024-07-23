from turtle import Turtle, Screen


class Scoreboard(Turtle):
    def __init__(self):
        self.__score = 0
        super().__init__()
        self.speed("fastest")
        self.penup()
        self.goto(0, 250)
        self.color("white")
        self.write("0", align="center", font=("Courier", 30, "normal"))
        self.hideturtle()

    def increase_score(self):
        self.__score += 1
        self.update()

    def game_over(self):
        self.clear()
        self.write(f"Game Over with Score {self.__score}", align="center", font=("Courier", 30, "normal"))

    def update(self):
        self.clear()
        self.write(str(self.__score), align="center", font=("Courier", 24, "normal"))
