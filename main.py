from turtle import Screen

from food import Food
from scoreboard import ScoreBoard
from snake import Snake
import time

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor('black')
screen.title('My snake game')
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()

directions = {"Up": snake.up, "Down": snake.down, "Left": snake.left, "Right": snake.right}
screen.listen()
for direction in directions:
    print(direction)
    print(directions[direction])
    screen.onkey(key=direction, fun=directions[direction])

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        print('game over')
        game_is_on = False
        score_board.game_over()

    for segment in snake.snake_body:
        if snake.head == segment:
            pass
        elif snake.head.distance(segment) < 10:
            score_board.game_over()
            game_is_on = False
screen.exitonclick()
