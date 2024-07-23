from random import randint
from turtle import Turtle


class Food(Turtle):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.shape('circle')
        self.color('blue')
        self.penup()
        self.screen_width = (screen_width // 2) - 40
        self.screen_height = (screen_height // 2) - 40
        self.shapesize(stretch_wid=0.7, stretch_len=0.7)
        self.random_food()

    def random_food(self):
        x = randint(-self.screen_width, self.screen_width)
        y = randint(-self.screen_height, self.screen_height)
        self.goto(x, y)

    def get_position(self):
        return self.pos()
