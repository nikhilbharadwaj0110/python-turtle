import turtle
import random

tom = turtle.Turtle()
canvas = turtle.Screen()

tom.screen.colormode(255)

rand = random.randint(5, 15)

for _ in range(rand):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    x = random.randint(-350, 350)
    y = random.randint(-350, 350)
    sides = random.randint(3, 10)
    size = random.randint(20, 80)
    direction = random.randint(0, 360)
    tom.penup()
    tom.goto(x, y)
    tom.right(direction)
    tom.color(r, g, b)
    tom.pendown()
    tom.begin_fill()

    for i in range(sides):
        tom.forward(size)
        tom.right(360 / sides)

    tom.end_fill()

canvas.exitonclick()
