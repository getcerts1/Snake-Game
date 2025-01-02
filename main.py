from turtle import Screen
import time
from SnakeClass import Snake
from food import Food
from turtledemo.penrose import start

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("--Snake-Game--")
screen.tracer(0)


snake = Snake()
food = Food()

screen.listen()

screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #Test for collision

    if snake.head.distance(food) < 15:
        food.refresh()

























screen.exitonclick()