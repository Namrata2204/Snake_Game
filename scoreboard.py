from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 220)
        self.hideturtle()
        with open('data.txt', 'r') as data:
            self.highscore = int(data.read())
        self.write(f"Score: {self.score} High Score: {self.highscore} ", False, align="center",
                   font=("Courier", 15, "normal"))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore} ", False, align="center",
                   font=("Courier", 15, "normal"))

    def high_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('data.txt','w') as data:
                data.write(f"{self.highscore}")

        self.score = -1
        self.update_score()
