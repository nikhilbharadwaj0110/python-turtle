import turtle

tom=turtle.Turtle()
canvas = turtle.Screen()
canvas.bgcolor("black")
tom.speed(5)

tom.penup()
tom.goto(0,-270)

tom.fillcolor("red")
tom.color("red")
tom.begin_fill()
tom.pendown()
for _ in range(3):
    tom.forward(50)
    tom.right(-120)

tom.end_fill()

tom.penup()
tom.goto(-200,200)

tom.fillcolor("magenta")
tom.color("magenta")
tom.begin_fill()
tom.pendown()
for _ in range(6):
    tom.forward(100)
    tom.right(60)

tom.end_fill()

tom.penup()
tom.goto(200,100)

tom.fillcolor("purple")
tom.color("purple")
tom.begin_fill()
tom.pendown()
for _ in range(10):
    tom.forward(100)
    tom.right(36)

tom.end_fill()

tom.penup()
tom.goto(-300,-100)

tom.fillcolor("teal")
tom.color("teal")
tom.begin_fill()
tom.pendown()
for _ in range(5):
    tom.forward(150)
    tom.right(144)

tom.end_fill()

canvas.exitonclick()