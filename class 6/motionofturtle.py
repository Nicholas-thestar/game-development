import turtle, time

square = turtle.Turtle()
square.shape("square")

square.penup()


x = 100
y = 100

speedX = 5
speedY = 4
while True:
    y += speedY
    x += speedX
    if x > 330 or x < -330:
        speedX = -speedX
    if y > 330 or y < -330:
        speedY = - speedY
    time.sleep(0.01)
    square.goto(x,y)


turtle.done()