import turtle

tom = turtle.Turtle()
canvas = turtle.Screen()

canvas.bgcolor("black")

tom.penup()
tom.goto(-50, 50)
tom.pendown()

tom.color("cyan")
tom.fillcolor("teal")

tom.begin_fill()
for i in range(4):
    tom.forward(100)
    tom.right(90)

tom.penup()
tom.goto(0, 0)
tom.pendown()

for i in range(4):
    tom.forward(100)
    tom.right(90)

tom.left(135)
tom.forward(70)

tom.penup()
tom.goto(50, 50)
tom.pendown()

tom.right(180)
tom.forward(70)

tom.penup()
tom.goto(50, -50)
tom.pendown()

tom.forward(70)
tom.end_fill()

tom.begin_fill()

tom.penup()
tom.goto(-50, -50)
tom.pendown()

tom.forward(70)
tom.end_fill()
tom.left(135)
tom.forward(50)
tom.left(90)
tom.forward(50)
tom.left(135)
tom.forward(70)

tom.end_fill()

tom.penup()
tom.goto(200, 200)

canvas.exitonclick()
