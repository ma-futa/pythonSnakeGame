from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('white')
        self.goto(x=0,y=270)
        self.update_score
        self.hideturtle()
        self.retrieve_high_score()

    def retrieve_high_score(self):
        with open('data.txt') as file:
            content = file.read()
            self.high_score = int(content)

    def write_high_score(self):
        with open('data.txt',mode='w') as file:
            file.write(str(self.high_score))


    def increase_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'Score: {self.score}  High Score: {self.high_score}', align='center', font=('Arial', 24, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score()
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.clear()
    #     self.write('GAME OVER', align='center', font=('Arial', 24, 'normal'))

