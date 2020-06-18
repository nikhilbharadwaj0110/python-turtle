import turtle

tom=turtle.Turtle()
tom.speed(300)
canvas = turtle.Screen()

canvas.bgcolor("black")
tom.penup()
tom.goto(0,0)
tom.pendown()
tom.color("yellow")
tom.fillcolor("teal")
tom.begin_fill()
for i in range(201):
    tom.forward(i*3)
    tom.left(117)
tom.end_fill()


canvas.exitonclick()