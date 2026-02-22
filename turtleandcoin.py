import turtle,random

screen = turtle.Screen()
screen.bgcolor("skyblue")

coin = turtle.Turtle()
coin.shape("circle")
coin.color("gold")
coin.penup()
coin.goto(random.randint(-250,250),random.randint(-250,250))


tort = turtle.Turtle()
tort.shape("turtle")
tort.color("red")
tort.penup()


def move_up():
    tort.sety(tort.ycor()+10)

def move_down():
    tort.sety(tort.ycor()-10)

def move_left():
    tort.setx(tort.xcor()-10)

def move_right():
    tort.setx(tort.xcor()+10)
screen.listen()
screen.onkey(move_up,"Up")
screen.onkey(move_down,"Down")
screen.onkey(move_left,"Left")
screen.onkey(move_right,"Right")

# def check_coll()
def check_coll(tur,coin):
    # it will check the distance bet the coid and the tur
    # if the dis is less tha 25 then we will consider that they have collided
    if tur.distance(coin)<25:
        return True
    else:
        return False
score = 0
pen = turtle.Turtle()
pen.pendown()

pen.penup()
pen.goto(-200,200)
pen.hideturtle()
pen.write("score :"+str(score),font=("Arial",20,"bold"))
score = 0
def game_loop():
    global score
    # keep check for the coll
    if check_coll(tort,coin):
        coin.goto(random.randint(-300,300),random.randint(-300,300))
        score +=10
        pen.clear()
        pen.write("score :"+str(score),font=("Arial",20,"bold"))

        print(score)
    screen.ontimer(game_loop,50) #it will call the game loop for coll, after each 50 milli sec
    
    


game_loop()
turtle.done()