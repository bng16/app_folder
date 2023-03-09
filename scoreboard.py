from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.pu()
        self.score = 0
        with open('h_score.txt') as data:
            self.h_score = int(data.read())
        self.goto(0, 269)
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f'Score:-{self.score},highest Score:-{self.h_score}', False, 'center', ('Courier', 20, 'normal'))

    def resat(self):
        if self.h_score < self.score:
            self.h_score = self.score
            with open('h_score.txt', 'w') as data:
                data.write(f'{self.h_score}')
        self.score = 0
        self.update()

    # def gameover(self):
    #     self.goto(0,0)
    #     self.write('Game Over', False, 'center', ('Courier', 20, 'normal'))
    #     self.goto(0, -25)
    #     self.write('click to exit', False, 'center', ('Courier', 15, 'normal'))

    def score_count(self):
        self.score += 1
        self.update()
