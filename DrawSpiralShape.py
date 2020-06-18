import turtle
import time

tom = turtle.Turtle()
tom.speed(100)
canvas = turtle.Screen()
canvas.bgcolor("black")

tom.color("orange")
tom.fillcolor("yellow")
tom.begin_fill()
tom.penup()
tom.goto(-250,250)
tom.pendown()
for i in range(40):
    tom.forward(500)
    tom.right(115)
    tom.left(15)
tom.end_fill()

tom.penup()
tom.goto(-135,-125)
tom.pendown()
tom.color("black")
tom.begin_fill()
tom.circle(210)
tom.end_fill()




canvas.exitonclick()
