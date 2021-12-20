from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.score = 0
        with open("data.txt", mode='r') as h_s_n:
            h_s_n = int(h_s.read())
        self.high_score = h_s_n
        self.hideturtle()
        self.penup()
        self.goto(0, 267)

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align="center", font=("Courier", 24, "normal"))


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode='w') as h_s_w:
                h_s_w.write(str(self.high_score))
        self.score = 0
        self.write_score()

    def update_score(self):
        self.score += 1
        self.write_score()


    # def game_over(self):
    #     self.home()
    #     self.write(f"GAME OVER!", align="center", font=("Courier", 24, "underline bold"))

