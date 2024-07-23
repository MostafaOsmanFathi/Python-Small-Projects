from turtle import Turtle


class Scoreboard(Turtle):
    SCOREBORDORINTATION = 100

    def __init__(self, alignment):
        super().__init__()
        if alignment == 'left':
            self.goto(-Scoreboard.SCOREBORDORINTATION, 200)
        elif alignment == 'right':
            self.goto(Scoreboard.SCOREBORDORINTATION, 200)
        else:
            raise ValueError(f'alignment must be either "left" or "right"')
        self.hideturtle()
        self.penup()
        self.color('white')
        self.__score = 0
        self.__update()

    def __update(self):
        self.clear()
        self.write(self.__score, align='center', font=('Courier', 80, 'bold'))

    def increase_score(self):
        self.__score += 1
        self.__update()

    def get_score(self):
        return self.__score

