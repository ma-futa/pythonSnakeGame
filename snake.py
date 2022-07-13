from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for index in range(7):
            self.add_segment(index)

    def add_segment(self,index):
        segment = Turtle(shape='square')
        segment.penup()
        segment.color('white')
        offset = -20.0 * index
        segment.goto(x=offset, y=0)
        self.snake_body.append(segment)

    def extend(self):

        segment = Turtle(shape='square')
        segment.penup()
        segment.color('white')
        # offset = -20.0 * index
        segment.goto(self.snake_body[-1].position())
        self.snake_body.append(segment)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)



    def move(self):
        for seg_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[seg_num - 1].xcor()
            new_y = self.snake_body[seg_num - 1].ycor()
            self.snake_body[seg_num].goto(new_x, new_y)
        self.snake_body[0].forward(MOVE_DISTANCE)
