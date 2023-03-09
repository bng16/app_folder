from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.colormode(255)
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
# screen.onkey(scoreboard.gameover,'e')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collution wirh food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.score_count()

    # detact collution with wall
    if snake.head.xcor() > 282 or snake.head.xcor() < -282 or snake.head.ycor() > 282 or snake.head.ycor() < -282:
        scoreboard.resat()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 18:
            scoreboard.resat()
            snake.reset()

screen.exitonclick()
