from turtle import Turtle, Screen
from paddle import Paddle
from score import Score
from bola import Ball
import time


def desenha_linhas():
    linhas = Turtle()
    linhas.color("white")
    linhas.penup()
    linhas.hideturtle()
    linhas.speed("fastest")
    linhas.goto(0, 370)

    linhas.setheading(270)
    linhas.pendown()
    linhas.pensize(5)

    while linhas.ycor() > -370:
        linhas.pendown()
        linhas.forward(20)
        linhas.penup()
        linhas.forward(30)


def inicializa_ecra():
    screen = Screen()
    screen.screensize(800, 600)
    screen.bgcolor("black")
    screen.tracer(0)
    screen.title("PONG")
    screen.listen()

    return screen


def jogo():
    screen = inicializa_ecra()
    bola = Ball()

    desenha_linhas()
    paddle1 = Paddle(-440, -30)
    paddle2 = Paddle(440, -30)
    score1 = Score(-90, 290)
    score2 = Score(90, 290)

    screen.onkeypress(paddle1.cima, "Up")
    screen.onkeypress(paddle1.baixo, "Down")
    screen.onkeypress(paddle2.cima, "w")
    screen.onkeypress(paddle2.baixo, "s")

    jogo_ativo = True
    score1.atualiza_score()
    score2.atualiza_score()

    while jogo_ativo:
        screen.update()
        time.sleep(0.1)

        bola.forward(40)
        bola.bateu_margem()

        if paddle1.bateu_bola(bola.position()) or paddle2.bateu_bola(bola.position()):
            bola.bateu_jogador()

        if bola.xcor() > 480:
            score1.aumenta_pontos()
            bola.reinicia()
            time.sleep(0.5)
        elif bola.xcor() < -480:
            score2.aumenta_pontos()
            bola.reinicia()
            time.sleep(0.5)

    screen.exitonclick()


jogo()
