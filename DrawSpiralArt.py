import turtle
tom = turtle.Turtle()
tom.speed(300)
canvas = turtle.Screen()
canvas.bgcolor("black")

tom.color("orange")
tom.fillcolor("teal")
tom.begin_fill()
for i in range(100):
    tom.circle(i*3)
    tom.left(10)
tom.end_fill()
canvas.exitonclick()