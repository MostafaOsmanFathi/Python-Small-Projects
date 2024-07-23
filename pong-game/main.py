from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from socreboard import Scoreboard

SCREEN_SPEED = .03


def main():
    # screen init
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgpic('background.gif')
    screen.tracer(0)
    right_paddle = Paddle(xcor=350, ycor=0)
    left_paddle = Paddle(xcor=-350, ycor=0)
    screen.listen()
    screen.onkeypress(lambda: (left_paddle.up(), right_paddle.up(), screen.update()), 'w')
    screen.onkeypress(lambda: (left_paddle.down(), right_paddle.down(), screen.update()), 's')

    scoreboard_left = Scoreboard('left')
    scoreboard_right = Scoreboard('right')

    ball = Ball()
    debug = 0
    while scoreboard_left.get_score() != 5 and scoreboard_right.get_score() != 5:
        debug += 1
        if ball.collision_right():
            print("player 2 lost")
            scoreboard_left.increase_score()
            ball.reset_ball()
        elif ball.collision_left():
            print("player 1 lost")
            scoreboard_right.increase_score()
            ball.reset_ball()
        elif left_paddle.detect_collision(*ball.pos(), debug):
            ball.reverse_move()
        elif right_paddle.detect_collision(*ball.pos(), debug):
            ball.reverse_move()
        ball.move()
        screen.update()
        sleep(SCREEN_SPEED)

    if scoreboard_left.get_score() > scoreboard_right.get_score() :
        ball.write_winner_message('winner is player 1')
    else:
        ball.write_winner_message('winner is player 2')

    screen.exitonclick()


if __name__ == '__main__':
    main()
