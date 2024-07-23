from turtle import Screen, Turtle
from snake import Snake
from scoreboard import Scoreboard
import time
from food import Food


def main():
    # Screen Data
    screen_height = 600
    screen_width = 600
    screen = Screen()
    Screen().setup(width=screen_width, height=screen_height)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)
    # Snake object
    snake = Snake("blue")
    # snake2 = Snake("red")
    screen.update()

    # Screen control
    screen.listen()
    screen.onkey(snake.up, 'w')
    screen.onkey(snake.right, 'd')
    screen.onkey(snake.down, 's')
    screen.onkey(snake.left, 'a')

    scoreboard = Scoreboard()


    # screen.onkey(snake2.up, 'Up')
    # screen.onkey(snake2.right, 'Right')
    # screen.onkey(snake2.down, 'Down')
    # screen.onkey(snake2.left, 'Left')

    food = Food(screen_width, screen_height)

    game_is_on = True
    while game_is_on:
        snake.move()
        screen.update()
        time.sleep(snake.speed)
        if snake.is_snake_out_of_screen(screen_width, screen_height) or snake.is_collision_snake_body():
            game_is_on = False
            scoreboard.game_over()
        elif snake.is_there_collision(food.get_position()):
            food.random_food()
            snake.add_segment()
            snake.increase_speed()
            scoreboard.increase_score()

        # snake2.move()
        # screen.update()
        # time.sleep(snake2.speed)
        # if snake2.is_snake_out_of_screen(screen_width, screen_height) or snake2.is_collision_snake_body():
        #     game_is_on = False
        # elif snake2.is_there_collision(food.get_position()):
        #     food.random_food()
        #     snake2.add_segment()
        #     snake2.increase_speed()

    print("you lose")
    screen.exitonclick()


if __name__ == '__main__':
    main()
