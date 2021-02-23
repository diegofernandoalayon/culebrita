import turtle
import time
import random
import tkinter as tk

# tiempo para animación
posponer = 0.11

# marcadordf
score = 0
high_score = 0

score2 = 0
high_score2 = 0

# configuracion ventana
ventana = turtle.Screen()
ventana.title("Juego de Snake")
ventana.bgcolor("#7c9696")
ventana.setup(width=800, height=600)
ventana.tracer(0)


# Crear cabeza serpiente 1
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("circle")
cabeza.color("white")
cabeza.penup()
cabeza.goto(-60, 0)
cabeza.direction = "stop"
# crear cabeza serpiente 2
cabeza2 = turtle.Turtle()
cabeza2.speed(0)
cabeza2.shape("circle")
cabeza2.color("blue")
cabeza2.penup()
cabeza2.goto(60, 0)
cabeza2.direction = "stop"
# comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0, 110)
# cuerpo serpiente
segmentos = []
segmentos2 = []

# texto
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(-340, 270)
texto.write("Score: 0  High Score: 0",
            align="left", font=("Courier", 16, "bold"))

texto2 = turtle.Turtle()
texto2.speed(0)
texto2.color("blue")
texto2.penup()
texto2.hideturtle()
texto2.goto(40, 270)
texto2.write("Score: 0  High Score: 0",
             align="left", font=("Courier", 16, "bold"))

texto_ini = turtle.Turtle()

textoperdio = turtle.Turtle()
textoperdio.hideturtle()

texto_paus = turtle.Turtle()
texto_paus.hideturtle()


texto_resume = turtle.Turtle()
texto_resume.hideturtle()

# Funciones


def borde():
    ancho = 785
    alto = 585
    # recuadro para borde
    recuadro = turtle.Turtle()
    recuadro.speed(0)
    recuadro.shape("square")
    recuadro.color("#7c9606")
    # recuadro.goto(-390, -280)
    recuadro.penup()
    recuadro.setx(-395)
    recuadro.sety(-290)
    recuadro.direction = "stop"
    recuadro.pendown()
    recuadro.width(5)
    recuadro.forward(ancho)
    recuadro.left(90)
    recuadro.forward(alto)
    recuadro.left(90)
    recuadro.forward(ancho)
    recuadro.left(90)
    recuadro.forward(alto)
    recuadro.left(90)
    recuadro.hideturtle()

    # recuadro.hideturtle()


def texto_inicio(indicador):

    indi = indicador
    if indi == 0:

        texto_ini.speed(0)
        texto_ini.color("white")
        texto_ini.penup()
        texto_ini.hideturtle()
        texto_ini.goto(0, 0)
        texto_ini.write("INICIO",
                        align="center", font=("Courier", 56, "bold"))
        #print("no se borro")

    if indi == 1:
        texto_ini.clear()


def texto_perdio_fun(indi):
    textoperdio.speed(0)
    textoperdio.color("white")
    textoperdio.penup()

    textoperdio.goto(0, 0)
    if indi == 0:
        textoperdio.hideturtle()
        textoperdio.clear()
    if indi == 1:

        textoperdio.write("PERDIO BLANCO", align="center",
                          font=("courier", 56, "bold"))
    if indi == 2:
        textoperdio.color("blue")
        textoperdio.write("PERDIO AZUL", align="center",
                          font=("courier", 56, "bold"))


def arriba():
    cabeza.direction = "up"


def abajo():
    cabeza.direction = "down"


def derecha():
    cabeza.direction = "right"


def izquierda():
    cabeza.direction = "left"


def arriba2():
    cabeza2.direction = "up"


def abajo2():
    cabeza2.direction = "down"


def derecha2():
    cabeza2.direction = "right"


def izquierda2():
    cabeza2.direction = "left"


def mov():

    velocidad = 20

    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + velocidad)

    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - velocidad)

    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + velocidad)

    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - velocidad)


def mov2():

    velocidad = 20
    if cabeza2.direction == "up":
        y = cabeza2.ycor()
        cabeza2.sety(y + velocidad)

    if cabeza2.direction == "down":
        y = cabeza2.ycor()
        cabeza2.sety(y - velocidad)

    if cabeza2.direction == "right":
        x = cabeza2.xcor()
        cabeza2.setx(x + velocidad)

    if cabeza2.direction == "left":
        x = cabeza2.xcor()
        cabeza2.setx(x - velocidad)


def texto_pausa(indica_pausa):

    if(indica_pausa == 1):
        texto_paus.speed(0)
        texto_paus.hideturtle()
        texto_paus.color("white")
        texto_paus.penup()
        texto_paus.goto(0, 0)
        texto_paus.write("PAUSA", align="center", font=("courier", 56, "bold"))
    elif (indica_pausa == 0):
        texto_paus.clear()


def pausar():
    global estado
    if (estado == "play"):
        estado = "pause"
        indi_pau = 1
        texto_pausa(indi_pau)
    elif (estado == "pause"):
        estado = "play"
        indi_pau = 0
        texto_pausa(indi_pau)


ventana.listen()  # estar pendiente de la ventana


estado = "play"
aux = 0
texto_inicio(aux)

borde()


# LEER TECLADO jugador 1

ventana.onkeypress(arriba, "w")
ventana.onkeypress(abajo, "s")
ventana.onkeypress(derecha, "d")
ventana.onkeypress(izquierda, "a")

ventana.onkeypress(arriba, "W")
ventana.onkeypress(abajo, "S")
ventana.onkeypress(derecha, "D")
ventana.onkeypress(izquierda, "A")

# leer teclado jugador 2

ventana.onkeypress(arriba2, "Up")
ventana.onkeypress(abajo2, "Down")
ventana.onkeypress(derecha2, "Right")
ventana.onkeypress(izquierda2, "Left")

ventana.onkeypress(pausar, "space")


'''CUERPO DEL JUEGO'''

while True:
    ventana.update()

    if (estado == "pause"):
        pass
    elif (estado == "play"):
        if cabeza.xcor() > 380 or cabeza.xcor() < -380 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
            indi_per = 1
            texto_perdio_fun(indi_per)
            time.sleep(1)
            cabeza.goto(-60, 0)
            cabeza.direction = "stop"
            # esconder segmentosz
            for segmento in segmentos:
                segmento.goto(1000, 1000)
            segmentos.clear()
            # resetear marcador
            score = 0
            indi_per = 0
            texto_perdio_fun(indi_per)
            texto.clear()
            texto.write("Score: {}  High Score: {}".format(score, high_score),
                        align="left", font=("Courier", 16, "bold"))

        if cabeza2.xcor() > 380 or cabeza2.xcor() < -380 or cabeza2.ycor() > 280 or cabeza2.ycor() < -280:
            indi_per = 2
            texto_perdio_fun(indi_per)
            time.sleep(1)
            cabeza2.goto(60, 0)
            cabeza2.direction = "stop"
            for segmento in segmentos2:
                segmento.goto(1000, 1000)
            segmentos2.clear()
            # resetear marcador
            score2 = 0
            indi_per = 0
            texto_perdio_fun(indi_per)
            texto2.clear()
            texto2.write("Score: {}  High Score: {}".format(score2, high_score2),
                         align="left", font=("Courier", 16, "bold"))

        # colisiones comida
        if cabeza.distance(comida) < 20:
            x = random.randint(-380, 380)
            y = random.randint(-280, 280)
            comida.goto(x, y)

            nuevo_segmento = turtle.Turtle()
            nuevo_segmento.speed(0)
            nuevo_segmento.shape("circle")
            nuevo_segmento.color("gray")
            nuevo_segmento.penup()
            segmentos.append(nuevo_segmento)

            # aumentar marcador
            score += 10
            if score > high_score:
                high_score = score
            texto.clear()
            texto.write("Score: {}  High Score: {}".format(score, high_score),
                        align="left", font=("Courier", 16, "bold"))

        if cabeza2.distance(comida) < 20:
            x = random.randint(-380, 380)
            y = random.randint(-280, 280)
            comida.goto(x, y)

            nuevo_segmento2 = turtle.Turtle()
            nuevo_segmento2.speed(0)
            nuevo_segmento2.shape("circle")
            nuevo_segmento2.color("light blue")
            nuevo_segmento2.penup()
            segmentos2.append(nuevo_segmento2)

            # aumentar el marcador 2
            score2 += 10
            if score2 > high_score2:
                high_score2 = score2
            texto2.clear()
            texto2.write("Score: {}  High Score: {}".format(score2, high_score2),
                         align="left", font=("Courier", 16, "bold"))

        # mover el cuerpo de la serpiente
        totalseg = len(segmentos)
        for index in range(totalseg - 1, 0, -1):
            x = segmentos[index - 1].xcor()
            y = segmentos[index - 1].ycor()
            segmentos[index].goto(x, y)
        if totalseg > 0:
            x = cabeza.xcor()
            y = cabeza.ycor()
            segmentos[0].goto(x, y)
        # mover el cuerpo de la serpiente 2
        totalseg2 = len(segmentos2)
        for index in range(totalseg2 - 1, 0, -1):
            x = segmentos2[index - 1].xcor()
            y = segmentos2[index - 1].ycor()
            segmentos2[index].goto(x, y)
        if totalseg2 > 0:
            x = cabeza2.xcor()
            y = cabeza2.ycor()
            segmentos2[0].goto(x, y)

        mov()
        # colisiones con el cuerpo
        for segmento in segmentos:
            if segmento.distance(cabeza) < 20:
                indi_per = 1
                texto_perdio_fun(indi_per)
                time.sleep(1)
                cabeza.goto(-60, 0)
                cabeza.direction = "stop"

                # esconder los segmentos
                for segmento in segmentos:
                    segmento.goto(1000, 1000)
                segmentos.clear()
                # resetear marcador
                score = 0
                indi_per = 0
                texto_perdio_fun(indi_per)
                texto.clear()
                texto.write("Score: {}  High Score: {}".format(score, high_score),
                            align="left", font=("Courier", 16, "bold"))
        mov2()

        # colisiones con el cuerpo 2
        for segmento in segmentos2:
            if segmento.distance(cabeza2) < 20:
                indi_per = 2
                texto_perdio_fun(indi_per)
                time.sleep(1)
                cabeza2.goto(60, 0)
                cabeza2.direction = "stop"

                # esconder los segmentos
                for segmento in segmentos2:
                    segmento.goto(1000, 1000)
                segmentos2.clear()
                # resetear marcador 2
                score2 = 0
                indi_per = 0
                texto_perdio_fun(indi_per)
                texto2.clear()
                texto2.write("Score: {}  High Score: {}".format(score2, high_score2),
                             align="left", font=("Courier", 16, "bold"))
        time.sleep(posponer)

        # para borrar el texto de inicio
        if ((cabeza.direction == "up") and (cabeza.pos() == (-60.00, 20.00))) or ((cabeza.direction == "down") and (cabeza.pos() == (-60.00, -20.00))) or ((cabeza.direction == "right") and (cabeza.pos() == (-40.00, 0))) or ((cabeza.direction == "left") and (cabeza.pos() == (-80.00, 0))):
            aux = 1
            texto_inicio(aux)
        if ((cabeza2.direction == "up") and (cabeza2.pos() == (60.00, 20.00))) or ((cabeza2.direction == "down") and (cabeza2.pos() == (60.00, -20.00))) or ((cabeza2.direction == "right") and (cabeza2.pos() == (80.00, 0))) or ((cabeza2.direction == "left") and (cabeza2.pos() == (40.00, 0))):
            aux = 1
            texto_inicio(aux)
