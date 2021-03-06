import turtle

tom = turtle.Turtle()
tom.speed(5)
canvas = turtle.Screen()
tom2 = turtle.Turtle()
tom2.hideturtle()
tom3 = turtle.Turtle()
tom3.hideturtle()
tom4 = turtle.Turtle()
tom4.hideturtle()


def gotoPos(x, y):
    tom.penup()
    tom.goto(x, y)
    tom.pendown()


# tyre1
gotoPos(-175, -225)
tom.fillcolor("black")
tom.begin_fill()
tom.circle(80)
tom.end_fill()

gotoPos(-175, -190)
tom.fillcolor("white")
tom.begin_fill()
tom.circle(45)
tom.end_fill()

gotoPos(-85, -160)
tom.pensize(10)
tom.setheading(80)
tom.circle(90, 130)
tom.pensize(1)

# tyre2
gotoPos(175, -225)
tom.setheading(0)
tom.fillcolor("black")
tom.begin_fill()
tom.circle(80)
tom.end_fill()

gotoPos(175, -190)
tom.fillcolor("white")
tom.begin_fill()
tom.circle(45)
tom.end_fill()

gotoPos(260, -110)
tom.pensize(10)
tom.setheading(110)
tom.circle(90, 150)
tom.pensize(1)

# body frame

gotoPos(-50, -145)
tom.setheading(120)
tom.pensize(15)
tom.forward(150)
gotoPos(-50, -145)
tom.setheading(0)
tom.pensize(15)
tom.forward(100)
tom.left(60)
tom.forward(150)

gotoPos(25, 0)
tom.right(60)
tom.fillcolor("black")
tom.begin_fill()
for i in range(2):
    tom.forward(185)
    tom.left(90)
    tom.forward(50)
    tom.left(90)
tom.end_fill()

tom2.penup()
tom2.goto(-35, 35)
tom2.pendown()
tom2.showturtle()
tom2.right(90)
tom2.shape("circle")
tom2.shapesize(5, 3.5, 10)
tom2.fillcolor("light gray")
tom3.showturtle()
tom3.penup()
tom3.goto(-110, 30)
tom3.pendown()
tom3.shape("circle")
tom3.shapesize(4, 3.5, 10)
tom3.fillcolor("white")

gotoPos(155, 0)

tom.right(80)
tom.forward(140)

gotoPos(-130, -15)
tom.right(30)

tom.forward(140)

gotoPos(-60, 20)
tom.write("Yezdi", font=("Arial", 16,))

gotoPos(-95, 55)
tom.right(185)
tom.forward(55)
tom.right(90)
tom.forward(10)

# Draw engine
gotoPos(-70, -30)
tom.pensize(2)
tom.setheading(0)
for _ in range(2):
    tom.forward(70)
    tom.right(90)
    tom.forward(40)
    tom.right(90)

ypos = -33
tom.pensize(1)
for _ in range(8):
    gotoPos(-75, ypos)
    tom.forward(80)
    ypos = ypos - 5

# Draw decorator - side
gotoPos(12, -30)
tom.pensize(3)
tom.forward(78)
tom.right(120)
tom.forward(50)
tom.right(60)
tom.forward(40)
tom.right(70)
tom.forward(45)

tom4.showturtle()
tom4.penup()
tom4.goto(-10, -110)
tom4.color("gray")
tom4.pendown()
tom4.setheading(90)
tom4.shape("circle")
tom4.shapesize(4,2,1)

tom.hideturtle()
canvas.exitonclick()
