from turtle import Turtle

class Score(Turtle):
    def __init__(self, coord_x, coord_y):
        super().__init__()
        self.pontuacao = 0
        self.penup()
        self.hideturtle()
        self.goto(coord_x, coord_y)
        self.color("white")

    def aumenta_pontos(self):
        self.pontuacao += 1
        self.atualiza_score()

    def atualiza_score(self):
        self.clear()
        self.write(self.pontuacao, False, "center", ("Courier", 80, "bold"))
