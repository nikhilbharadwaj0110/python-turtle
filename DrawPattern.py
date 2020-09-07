import turtle
import random

window = turtle.Screen()

tom = turtle.Turtle()
tom.speed(200)
tom.pensize(5)
size = 20

tom.screen.colormode(255)

for i in range(150):
    tom.forward(size)
    tom.right(135)
    tom.forward(10)
    tom.backward(10)
    tom.right(90)
    tom.forward(10)
    tom.backward(10)
    size = size + 5
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tom.color(r, b, g)

# turtles=[]
#
# for i in range(10):
#     tom = turtle.Turtle()
#     tom.hideturtle()
#     turtles.append(tom)
#
# y = 0
# i = 1
# for oneTurtle in turtles:
#     oneTurtle.penup()
#     oneTurtle.goto(0,y)
#     oneTurtle.pendown()
#     oneTurtle.write("Hello, I am turtle #" + str(i), font=("Verdana", 12, "bold"))
#     y = y - 35
#     i = i + 1


window.exitonclick()
