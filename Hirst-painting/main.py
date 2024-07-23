import colorgram
from turtle import Turtle as t, Screen,colormode
from random import choice as random_choice
colors = colorgram.extract('unnamed.jpg', 30)
for i in range(len(colors)):
    colors[i] = (colors[i].rgb.r, colors[i].rgb.g, colors[i].rgb.b)

screen = Screen()
spaced = 50
width = 20
x=10
y=10
timmy = t()
timmy.width(width)
colormode(255)
timmy.penup()
timmy.speed(0)
startX=-350
startY=-250
timmy.hideturtle()
timmy.goto(startX,startY)
for i in range(y):
    timmy.goto(startX,startY+(i*60))
    for _ in range(x):
        timmy.color(random_choice(colors))
        timmy.dot()
        timmy.forward(spaced)

screen.exitonclick()