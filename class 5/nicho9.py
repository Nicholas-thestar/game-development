import turtle 
import random


arrow = turtle.Turtle()

screen = turtle.Screen()
screen.bgcolor("#0d0d30")

arrow.color("white")
arrow.penup()
arrow.goto(200,180)
arrow.speed(0)

arrow.pendown()
arrow.fillcolor("white")
arrow.begin_fill()
arrow.circle(50)
arrow.end_fill()


for j in range(100):
    arrow.penup()
# arriw.got(x,y)
    arrow.goto(random.randint(-380,380),random.randint(-380,380))
    arrow.pendown()

    for i in range(5):
        arrow.forward(10)
        arrow.left(144)


turtle.done()