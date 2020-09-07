import turtle
import random

canvas = turtle.Screen()
tom = turtle.Turtle()
tom.shape("turtle")
tom.setheading(90)
tom.penup()
tom.goto(0, -280)
tom.pendown()


def moveLeft():
    posX = tom.xcor()
    tom.penup()
    tom.goto(posX - 50, -280)


def moveRight():
    posX = tom.xcor()
    tom.penup()
    tom.goto(posX + 50, -280)


canvas.onkey(moveLeft, "left")

canvas.onkey(moveRight, "right")

canvas.listen()
tom.mainloop()
