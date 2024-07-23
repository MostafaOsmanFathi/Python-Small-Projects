from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__(shape='circle')
        self.penup()
        self.color('white')
        self.speed('fastest')
        self.dir_x = 10
        self.dir_y = 10

    def __detect_collision(self):
        if self.xcor() + 10 >= 400 or abs(self.xcor() - 10) >= 400:
            self.dir_x *= -1
        if self.ycor() + 10 >= 300 or abs(self.ycor() - 10) >= 300:
            self.dir_y *= -1

    def move(self):
        self.__detect_collision()
        self.goto(self.xcor() + self.dir_x, self.ycor() + self.dir_y)

    def collision_right(self):
        return self.xcor() > 380

    def collision_left(self):
        return self.xcor() < -380

    def reverse_move(self):
        self.dir_x *= -1
        self.dir_y *= -1

    def reset_ball(self):
        self.goto(0, 0)
        self.dir_x = abs(self.dir_x)
        self.dir_y = abs(self.dir_y)
    def write_winner_message(self,message):
        self.reset_ball()
        self.hideturtle()
        self.color('white')
        self.write(message, align='center', font=('Arial', 60, 'bold'))
