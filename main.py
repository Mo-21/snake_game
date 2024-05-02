import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from game_settings import GameSettings

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

my_snake = Snake()
food = Food()
score = Scoreboard()
game = GameSettings()

screen.listen()
screen.onkey(fun=my_snake.up, key="Up")
screen.onkey(fun=my_snake.down, key="Down")
screen.onkey(fun=my_snake.right, key="Right")
screen.onkey(fun=my_snake.left, key="Left")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(game.speed)
    my_snake.move()

    if my_snake.head.distance(food) < 15:
        food.refresh_position()
        score.increase_score()
        my_snake.extend()
        game.increase_speed()

    if (my_snake.head.xcor() > 295 or my_snake.head.xcor() < -295
            or my_snake.head.ycor() > 295 or my_snake.head.ycor() < -295):
        game_is_on = False
        score.game_over()

    for seg in my_snake.snake_segments[1:]:
        if my_snake.head.distance(seg) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
