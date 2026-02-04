import turtle

arrow = turtle.Turtle()

screen = turtle.Screen()
screen.bgcolor("blue")

arrow.color("purple")

for i in range (3):
    arrow.forward(200)
    arrow.left(120)

arrow.penup()
arrow.goto(-250,200)
arrow.pendown()

for i in range (3):
    arrow.forward(100)
    arrow.left(120)

arrow.penup()
arrow.goto(-250,-200)
arrow.pendown()

for i in range (3):
    arrow.forward(100)
    arrow.left(120)

arrow.penup()
arrow.goto(250,-200)
arrow.pendown()

for i in range (3):
    arrow.forward(100)
    arrow.left(120)

turtle.done()