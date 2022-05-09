from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.title("Snake Reloaded")
screen.tracer(0)

snake_food = Food()
snake = Snake()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_right, "Right")
screen.onkey(snake.move_left, "Left")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    snake.move()

    # detect collision with food
    if snake_food.distance(snake.snake_head) < 20:
        snake_food.refresh_food()
        snake.extend()
        scoreboard.display_score()

    # Detect collision with walls
    if snake.snake_head.xcor() > 300 or snake.snake_head.xcor() < -300 or snake.snake_head.ycor() > 300 or snake.snake_head.ycor() < -295:
        game_is_on = False



screen.exitonclick()