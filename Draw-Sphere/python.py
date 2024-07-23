from turtle import Turtle as t, Screen,colormode
from random import choice as random_choice, seed as random_seed, randint


colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def random_color():
    return random_choice(colors)

colormode(255)
screen = Screen()
timmy = t()
timmy.width(1)
screen.bgcolor('black')
timmy.speed(0)

def draw_spirograph(size_of_gap):
    colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
              "SeaGreen"]
    for _ in range(360//size_of_gap):
        timmy.pencolor(random_color())
        timmy.circle(200)
        timmy.setheading(timmy.heading()+size_of_gap)


gaps=screen.numinput("Gaps", "enter the gaps number from 1 to 360:", 1, minval=1, maxval=360)
draw_spirograph(int(gaps))
screen.exitonclick()
