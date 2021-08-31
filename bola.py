from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.penup()
        self.color("pink")
        self.reinicia()

    def reinicia(self):
        angulos = [45, 135, 225, 315]
        self.goto(0, 0)
        self.setheading(random.choice(angulos))

    def bateu_margem(self):
        if self.ycor() > 360 or self.ycor() < -360:
            direcao = self.heading()
            if 0 < direcao < 90:
                self.setheading(-direcao)
            elif 90 <= direcao < 180:
                self.setheading(180 + (180 - direcao))
            elif 180 <= direcao < 270:
                self.setheading(180 - (direcao - 180))
            else:
                self.setheading(360 - direcao)

    def bateu_jogador(self):
        direcao = self.heading()
        if 0 < direcao < 90:
            self.setheading((90 - direcao) + 90)
        elif 90 <= direcao < 180:
            self.setheading(90 - (direcao - 90))
        elif 180 <= direcao < 270:
            self.setheading((270 - direcao) + 270)
        else:
            self.setheading(270 - (direcao - 270))
