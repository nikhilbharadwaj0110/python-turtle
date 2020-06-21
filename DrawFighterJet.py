import turtle

tom = turtle.Turtle()
tom.speed(10)
tom.hideturtle()
canvas = turtle.Screen()

canvas.screensize()
canvas.setup(width=1.0, height=1.0)
canvas.bgcolor("dodgerblue")


def gotoPos(x, y):
    tom.penup()
    tom.goto(x, y)
    tom.pendown()


# Draw main body
tom.begin_fill()
for _ in range(2):
    tom.forward(80)
    tom.right(90)
    tom.forward(300)
    tom.right(90)
tom.end_fill()

# Draw front tip
tom.begin_fill()
tom.left(60)
tom.forward(80)
tom.right(120)
tom.forward(80)
tom.end_fill()

# Draw right wing
tom.begin_fill()
tom.right(30)
gotoPos(80, -100)
tom.left(45)
tom.forward(200)
tom.right(90)
tom.forward(80)
tom.right(90)
tom.forward(120)
tom.end_fill()

# Draw left wing
gotoPos(0, -100)
tom.begin_fill()
tom.left(90)
tom.forward(200)
tom.left(90)
tom.forward(80)
tom.left(90)
tom.forward(120)
tom.end_fill()

# Right Engine
gotoPos(115, -110)
tom.begin_fill()
tom.left(45)
tom.left(270)
for _ in range(2):
    tom.forward(35)
    tom.right(90)
    tom.forward(100)
    tom.right(90)

tom.left(60)
tom.forward(35)
tom.right(120)
tom.forward(35)
tom.end_fill()

# Left Engine
gotoPos(-65, -110)
tom.begin_fill()
tom.left(285)
tom.left(180)
tom.right(45)
for _ in range(2):
    tom.forward(35)
    tom.right(90)
    tom.forward(100)
    tom.right(90)

tom.left(60)
tom.forward(35)
tom.right(120)
tom.forward(35)

tom.end_fill()

# Draw frond tip
gotoPos(40, 69)
tom.right(30)
tom.pensize(2)
tom.backward(15)

# Draw cockpit
gotoPos(50, -10)
tom.color("gray")
tom.begin_fill()

for _ in range(2):
    tom.forward(50)
    tom.right(90)
    tom.forward(20)
    tom.right(90)
tom.left(180)
tom.circle(10, 180)

tom.end_fill()

# title
tom.color("black")
gotoPos(-75, 200)
tom.write("SR-71 BlackBird\n  The spy plane", font=("Arial", 20, "bold"))


canvas.exitonclick()
