import turtle

tom = turtle.Turtle()
canvas = turtle.Screen()
canvas.bgcolor("black")
tom.speed(200)
tom.hideturtle()

size = 20
tom.color("light gray")
for i in range(600):
    tom.forward(size)
    tom.right(219)
    size = size + 1
    if 200 < i <= 450:
        tom.color("cyan")
    elif i > 450:
        tom.color("teal")

canvas.exitonclick()
