import turtle

tom = turtle.Turtle()
tom2 = turtle.Turtle()
tom3 = turtle.Turtle()
tom4 = turtle.Turtle()

canvas = turtle.Screen()

tom2.hideturtle()
tom3.hideturtle()
tom4.hideturtle()

tom.speed(10)


def gotoPos(x, y):
    tom.penup()
    tom.goto(x, y)
    tom.pendown()


for _ in range(2):
    tom.forward(50)
    tom.right(90)
    tom.forward(300)
    tom.right(90)

gotoPos(0, 0)

for _ in range(2):
    tom.penup()
    tom.forward(50)
    tom.pendown()
    tom.left(90)
    tom.forward(300)
    tom.left(90)

tom2.st()
tom2.penup()
tom2.goto(25, 300)
tom2.pendown()
tom2.shape("circle")
tom2.shapesize(5, 2.5, 1)
tom2.fillcolor("white")
gotoPos(0, 0)

tom3.st()
tom3.penup()
tom3.goto(-25, 30)
tom3.pendown()
tom3.shape("circle")
tom3.shapesize(5, 2.5, 1)
tom3.fillcolor("white")

tom4.st()
tom4.penup()
tom4.goto(75, 30)
tom4.pendown()
tom4.shape("circle")
tom4.shapesize(5, 2.5, 1)
tom4.fillcolor("white")

tom.fillcolor("white")
tom.begin_fill()
tom.right(180)
for _ in range(2):
    tom.forward(45)
    tom.left(90)
    tom.forward(300)
    tom.left(90)
gotoPos(50, 0)
tom.right(180)

for _ in range(2):
    tom.forward(45)
    tom.right(90)
    tom.forward(300)
    tom.right(90)

tom.end_fill()

gotoPos(80, -300)

# tom.right(90)
tom.fillcolor("black")
tom.begin_fill()
for i in range(6):
    for j in range(2):
        tom.forward(15)
        tom.right(90)
        tom.forward(10)
        tom.right(90)
    tom.penup()
    tom.backward(25)
    tom.pendown()
tom.end_fill()

tom.left(45)

gotoPos(-30, -280)
tom.write("N", font=("Arial", 20, "bold"))
gotoPos(18, -280)
tom.write("S", font=("Arial", 20, "bold"))
gotoPos(65, -280)
tom.write("F", font=("Arial", 20, "bold"))


canvas.exitonclick()
