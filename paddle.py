import time
from turtle import Turtle

class Paddle:

    def __init__(self, coord_x, coord_y):
        self.segmentos = []

        for seg in range(4):
            parte = Turtle("square")
            parte.color("white")
            parte.penup()
            parte.goto(coord_x, coord_y)
            self.segmentos.append(parte)
            coord_y += 20

    def baixo(self):
        curr_y = self.segmentos[0].ycor()
        curr_x = self.segmentos[0].xcor()

        for segmento in range(len(self.segmentos) - 1, 0, -1):
            self.segmentos[segmento].goto(self.segmentos[segmento-1].pos())
            print(segmento)

        self.segmentos[0].goto(curr_x, curr_y - 20)

    def cima(self):
        tamanho = len(self.segmentos)
        curr_y = self.segmentos[tamanho-1].ycor()
        curr_x = self.segmentos[tamanho-1].xcor()

        for segmento in range(0,tamanho - 1):
            self.segmentos[segmento].goto(self.segmentos[segmento+1].pos())
            print(segmento)

        self.segmentos[tamanho - 1].goto(curr_x, curr_y + 20)

    def bateu_bola(self, coordenadas):
        res = False

        for segmento in self.segmentos:
            if segmento.distance(coordenadas) < 20:
                res = True
                print("LOL")
                break

        return res