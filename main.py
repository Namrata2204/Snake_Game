from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

my_screen = Screen()
my_screen.setup(width=500, height=500)
my_screen.title("Snake Game!!")
my_screen.bgcolor("black")
my_screen.tracer(0)

my_screen.update()

snake = Snake()
my_screen.listen()
my_screen.onkeypress(snake.up, "Up")
my_screen.onkeypress(snake.down, "Down")
my_screen.onkeypress(snake.left, "Left")
my_screen.onkeypress(snake.right, "Right")

snake_food = Food()
score = Score()

play_game = True
while play_game:
    my_screen.update()
    time.sleep(0.5)
    snake.move()
    if snake.head.distance(snake_food) < 15:
        snake_food.refresh()
        score.update_score()
        snake.increase_snake()

    if snake.head.xcor() > 240 or snake.head.xcor() < -240 or snake.head.ycor() > 240 or snake.head.ycor() < -240:
        score.high_score()
        time.sleep(0.5)
        snake.reset()
        my_screen.update()
        time.sleep(2)

    for seg in snake.segments[1::]:
        if seg.distance(snake.head) < 15:
            score.high_score()
            time.sleep(1)
            snake.reset()
            my_screen.update()
            time.sleep(2)
my_screen.exitonclick()
