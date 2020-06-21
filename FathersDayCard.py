import turtle

tom = turtle.Turtle()
tom2 = turtle.Turtle()
tom2.hideturtle()
canvas = turtle.Screen()
canvas.screensize()
canvas.setup(width=1.0, height=1.0)
canvas.bgcolor("teal")

tom.hideturtle()


def init():
    tom.speed(5)
    tom.screen.colormode(255)


def gotoPos(x, y):
    tom.penup()
    tom.goto(x, y)
    tom.pendown()


init()

gotoPos(-75, 90)

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

gotoPos(-75, 90)
tom.left(180)

tom.pendown()
tom.begin_fill()

for _ in range(2):
    tom.forward(120)
    tom.left(90)
    tom.forward(40)
    tom.left(90)

tom.end_fill()

gotoPos(75, 90)
tom.left(180)

tom.pendown()
tom.begin_fill()

for _ in range(2):
    tom.forward(120)
    tom.right(90)
    tom.forward(40)
    tom.right(90)

tom.end_fill()

gotoPos(-75, -90)
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

gotoPos(75, -90)
tom.begin_fill()
tom.pendown()
for _ in range(2):
    tom.forward(180)
    tom.right(90)
    tom.forward(40)
    tom.right(90)
tom.end_fill()

gotoPos(15, 90)

tom.fillcolor("salmon3")
tom.color("salmon3")
tom.begin_fill()
tom.pendown()
tom.left(180)
for _ in range(4):
    tom.forward(30)
    tom.left(90)

tom.end_fill()

gotoPos(0, 100)
tom.right(90)
tom.begin_fill()
tom.pendown()

tom.circle(50)
tom.end_fill()

gotoPos(-20, 150)
tom.fillcolor("white")
tom.color("white")
tom.begin_fill()
tom.pendown()
tom.circle(5)
tom.end_fill()

gotoPos(20, 150)
tom.fillcolor("white")
tom.color("white")
tom.begin_fill()
tom.pendown()
tom.circle(5)
tom.end_fill()

gotoPos(-15, 125)
tom.right(90)
tom.fillcolor("white")
tom.color("white")
tom.begin_fill()
tom.pendown()
tom.circle(15, 180)
tom.end_fill()

gotoPos(0, 90)
tom.color("black")
tom.pendown()
tom.pensize(3)
tom.right(180)
tom.forward(180)

posY = 70
for _ in range(6):
    gotoPos(5, posY)
    tom.pendown()
    tom.circle(2)
    posY = posY - 30

tom.penup()
tom.goto(-950, 350)
tom.pendown()

tom.write(
    "Dear Daddy, Happy father's day, thank you for being a great dad. I also want to thank you for always helping me when I am having tough time \nand thank you for entertaining me when you get the time. You are the best dad I could ever wish for. Once again Happy Father's Day.\nI love you a lot.",
    font=("Arial", 20, "bold"))

tom.penup()
tom.goto(-65, 60)
tom.pendown()
tom.write("Nikhil's", font=("Arial", 10, "bold"))

tom.penup()
tom.goto(-65, 50)
tom.pendown()
tom.write("dad is", font=("Arial", 10, "bold"))

tom.penup()
tom.goto(-65, 40)
tom.pendown()
tom.write("the best", font=("Arial", 10, "bold"))

tom.penup()
tom.goto(-65, 30)
tom.pendown()
tom.write("dad in", font=("Arial", 10, "bold"))

tom.penup()
tom.goto(-65, 20)
tom.pendown()
tom.write("the world", font=("Arial", 10, "bold"))
tom2.penup()
tom2.goto(205, 210)
tom2.pendown()

tom2.showturtle()
tom2.shape("circle")
tom2.shapesize(5, 6.5, 1)
tom2.fillcolor("white")
tom.showturtle()
tom.penup()
tom.goto(150, 210)
tom.pendown()
tom.write("Happy father's day best ")
tom.penup()
tom.goto(150, 200)
tom.pendown()
tom.write("dad in the world")

tom.color("white")
gotoPos(105, 175)
tom.circle(5)
gotoPos(80, 165)
tom.circle(5)
gotoPos(135, 185)
tom.circle(5)
tom.hideturtle()

canvas.exitonclick()
