from turtle import Turtle, Screen

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor('black')
screen.title('My snake game')

snake_body = []
for index in range(3):
    segment = Turtle(shape='square')
    segment.penup()
    segment.color('white')
    offset = -20.0 * index
    segment.goto(x=offset, y=0)
    snake_body.append(segment)

screen.exitonclick()
