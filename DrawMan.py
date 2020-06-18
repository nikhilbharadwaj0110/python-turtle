import turtle

tom = turtle.Turtle()
canvas = turtle.Screen()

def init():
    tom.speed(5)
    tom.screen.colormode(255)

def gotoPos(x,y):
    tom.penup()
    tom.goto(x,y)

init()

gotoPos(-75,90)

tom.color("sky blue")
tom.pendown()
tom.fillcolor("sky blue")
tom.begin_fill()

for _ in range(2):
    tom.forward(150)
    tom.right(90)
    tom.forward(180)
    tom.right(90)

tom.end_fill()

gotoPos(-75,90)
tom.left(180)

tom.pendown()
tom.begin_fill()

for _ in range(2):
    tom.forward(120)
    tom.left(90)
    tom.forward(40)
    tom.left(90)

tom.end_fill()

gotoPos(75,90)
tom.left(180)

tom.pendown()
tom.begin_fill()

for _ in range(2):
    tom.forward(120)
    tom.right(90)
    tom.forward(40)
    tom.right(90)

tom.end_fill()

gotoPos(-75,-90)
tom.right(90)

tom.pendown()
tom.fillcolor("black")
tom.color("black")
tom.begin_fill()

for _ in range(2):
    tom.forward(180)
    tom.left(90)
    tom.forward(40)
    tom.left(90)

tom.end_fill()

gotoPos(75,-90)
tom.begin_fill()
tom.pendown()
for _ in range(2):
    tom.forward(180)
    tom.right(90)
    tom.forward(40)
    tom.right(90)
tom.end_fill()


gotoPos(15,90)

tom.fillcolor("salmon3")
tom.color("salmon3")
tom.begin_fill()
tom.pendown()
tom.left(180)
for _ in range(4):
    tom.forward(30)
    tom.left(90)

tom.end_fill()

gotoPos(0,100)
tom.right(90)
tom.begin_fill()
tom.pendown()

tom.circle(50)
tom.end_fill()

gotoPos(-20,150)
tom.fillcolor("white")
tom.color("white")
tom.begin_fill()
tom.pendown()
tom.circle(5)
tom.end_fill()

gotoPos(20,150)
tom.fillcolor("white")
tom.color("white")
tom.begin_fill()
tom.pendown()
tom.circle(5)
tom.end_fill()

gotoPos(-15,125)
tom.right(90)
tom.fillcolor("white")
tom.color("white")
tom.begin_fill()
tom.pendown()
tom.circle(15,180)
tom.end_fill()

gotoPos(0,90)
tom.color("black")
tom.pendown()
tom.pensize(3)
tom.right(180)
tom.forward(180)

posY = 70
for _ in range(6):
    gotoPos(5,posY)
    tom.pendown()
    tom.circle(2)
    posY = posY - 30


gotoPos(-80,170)
tom.left(90)
tom.pendown()
tom.forward(160)

tom.fillcolor("black")
gotoPos(50,170)
tom.right(270)
tom.pendown()
tom.begin_fill()
tom.circle(50,180)
tom.end_fill()

tom.penup()
gotoPos(250,250)


canvas.exitonclick()