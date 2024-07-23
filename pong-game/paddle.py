from turtle import Turtle


class Paddle(Turtle):
    SENSITIVITY = 20
    EDGE_LIMIT = 70

    def __init__(self, xcor, ycor):
        super().__init__(shape="square")
        self.color("white")
        self.penup()
        self.goto(xcor, ycor)
        self.shapesize(5, 1)
        self.speed("fastest")

    def up(self):
        if self.ycor() + 20 + Paddle.EDGE_LIMIT < 350:
            self.goto(self.xcor(), self.ycor() + Paddle.SENSITIVITY)

    def down(self):
        if abs(self.ycor() - 20 - Paddle.EDGE_LIMIT) < 350:
            self.goto(self.xcor(), self.ycor() - Paddle.SENSITIVITY)

    def detect_collision(self, x, y, debug=1):
        xx = self.xcor()
        yy = self.ycor()
        if abs(x - self.xcor()) <= 10 and y < self.ycor() + 50 and y > self.ycor() - 50:
            return True
        else:
            return False
