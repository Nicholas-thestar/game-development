import turtle 


arrow = turtle.Turtle()
arrow.shape("turtle")
arrow.color("green")
arrow.penup()
arrow.goto(50,50)
arrow.pendown()
for i in range(3):
    arrow.forward(100)
    arrow.left(120)




arrow2 = turtle.Turtle()
arrow2.shape("turtle")
arrow2.color("red")
arrow2.penup()
arrow2.goto(20,30)
arrow2.pendown()
for i in range(4):
    arrow2.forward(100)
    arrow2.left(90)
arrow3 = turtle.Turtle()
arrow3.shape("turtle")
arrow3.color("red")
arrow3.penup()
arrow3.goto(30,40)




arrow4 = turtle.Turtle()
arrow4.shape("turtle")
arrow4.color("red")
arrow4.penup()
arrow4.goto(150,140)
arrow4.pendown()
name = input("Enter your name")
arrow4.write(name)


turtle.done()