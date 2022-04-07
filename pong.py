import turtle

ww = turtle.Screen()
ww.title("pong ping by peter")
ww.bgcolor("black")
ww.setup(width=800,height=600)
ww.tracer(0)

#Score 
score_1=0
score_2=0

#Raquete 1

raquete1 = turtle.Turtle()
raquete1.speed(0)
raquete1.shape('square')
raquete1.color('red')
raquete1.shapesize(stretch_wid=5,stretch_len=1)
raquete1.penup()
raquete1.goto(-350,0)

#Raquete 2
raquete2 = turtle.Turtle()
raquete2.speed(0)
raquete2.shape('square')
raquete2.color('red')
raquete2.shapesize(stretch_wid=5,stretch_len=1)
raquete2.penup()
raquete2.goto(350,0)

#Bolinha 
bola = turtle.Turtle()
bola.speed(0)
bola.shape('circle')
bola.color('white')
bola.penup()
bola.goto(0,0)


#Score - Texto 
lap = turtle.Turtle()
lap.speed(0)
lap.color('white')
lap.penup()
lap.hideturtle()
lap.goto(0,260)
lap.write("Jogador A: 0   Jogador B: 0", align="center",font=("Courier",24,'normal'))

#Movimentação em x
bola.dx = 0.2
#Movimentação em y
bola.dy = 0.2

#Funções (Movimentação,contato,etc)
def raquete1_cima():
    y = raquete1.ycor()
    y += 40
    raquete1.sety(y)

def raquete1_baixo():
    y = raquete1.ycor()
    y -= 40
    raquete1.sety(y)

def raquete2_cima():
    y = raquete2.ycor()
    y += 40
    raquete2.sety(y)

def raquete2_baixo():
    y = raquete2.ycor()
    y -= 40
    raquete2.sety(y)

#Teclas
ww.listen()
ww.onkeypress(raquete1_cima,"w")
ww.onkeypress(raquete1_baixo,"s")
ww.onkeypress(raquete2_cima,"Up")
ww.onkeypress(raquete2_baixo,"Down")

#main game loop

while True:
    ww.update()

    #mover a bolinha
    bola.setx(bola.xcor()+ bola.dx)
    bola.sety(bola.ycor()+ bola.dy)

    #adicionando bordas
    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy *= -1
    
    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1
    
    if bola.xcor() > 390:
        bola.goto(0,0)
        bola.dx *= -1
        score_1 += 1
        lap.clear()
        lap.write("Jogador A: {}   Jogador B: {}".format(score_1,score_2), align="center",font=("Courier",24,'normal'))
    
    if bola.xcor() < -390:
        bola.goto(0,0)
        bola.dx *= -1
        score_2 += 1
        lap.clear()
        lap.write("Jogador A: {}   Jogador B: {}".format(score_1,score_2), align="center",font=("Courier",24,'normal'))
    
    
    #Colisões
    if (bola.xcor() > 340 and bola.xcor() < 350) and (bola.ycor() < raquete2.ycor()+40 and bola.ycor() > raquete2.ycor() -40):
        bola.setx(340)
        bola.dx *= -1 

    if (bola.xcor() < -340 and bola.xcor() > -350) and (bola.ycor() < raquete1.ycor()+ 40 and bola.ycor() > raquete1.ycor() -40):
        bola.setx(-340)
        bola.dx *= -1 