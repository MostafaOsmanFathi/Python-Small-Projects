from turtle import Turtle
from math import sqrt


class Snake:

    def create_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        return new_segment

    def __init__(self, head_color="red"):
        self.color = "white"
        self.speed = .09
        self.segments = [self.create_segment((0, 0))]
        self.add_segment()
        self.add_segment()
        self.segments[0].color(head_color)
        self.up = lambda: self.segments[0].setheading(90.0) if self.segments[0].heading() != 270.0 else None
        self.right = lambda: self.segments[0].setheading(0.0) if self.segments[0].heading() != 180.0 else None
        self.down = lambda: self.segments[0].setheading(270.0) if self.segments[0].heading() != 90.0 else None
        self.left = lambda: self.segments[0].setheading(180.0) if self.segments[0].heading() != 0.0 else None

    def move(self):
        old_pos = self.segments[0].pos()
        for i, segment in enumerate(self.segments):
            if i == 0:
                segment.forward(20)
            else:
                cur_pos = segment.pos()
                segment.goto(old_pos)
                old_pos = cur_pos

    def add_segment(self):
        self.segments.append(self.create_segment((self.segments[-1].xcor() - 20, self.segments[-1].ycor())))

    def calculate_distance(self, obj):
        return sqrt((((self.segments[0].xcor() - obj[0]) ** 2) + ((self.segments[0].ycor() - obj[1]) ** 2)))

    def is_there_collision(self, pos):
        return self.calculate_distance(pos) < 18

    def is_collision_snake_body(self):
        for i in range(1, len(self.segments)):
            if self.is_there_collision(self.segments[i].pos()):
                return True
        return False

    def is_snake_out_of_screen(self, width, height):
        return abs(self.segments[0].xcor()) > width/2 or abs(self.segments[0].ycor()) > height/2

    def increase_speed(self):
        self.speed -= .001
