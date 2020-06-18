import turtle
import random

tom = turtle.Turtle()
canvas = turtle.Screen()
tom.screen.colormode(255)

tom.speed(5)

for a in range(4):
    size = 20
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tom.color(r, g, b)
    tom.left(90)
    for i in range(3):
        size = size + 20
        for x in range(4):
            tom.forward(size)
            tom.left(90)


canvas.exitonclick()
