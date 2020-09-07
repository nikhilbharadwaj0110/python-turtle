import turtle
import random

window = turtle.Screen()

tom = turtle.Turtle()
tom.speed(1)
tom.hideturtle()

tom.penup()
tom.goto(-200, 200)
tom.pendown()

for _ in range(4):
    tom.write(tom.pos())
    tom.forward(400)
    tom.right(90)

oneTurtle = turtle.Turtle()
oneTurtle.speed(10)

oneTurtle.color("red")
oneTurtle.shape("circle")

while True:
    distance = 20  # random.randint(10, )
    oneTurtle.setheading(random.randint(0, 360))

    print(oneTurtle.pos())

    if oneTurtle.xcor() <= -200:
        oneTurtle.right(180)

    if oneTurtle.xcor() >= 200:
        oneTurtle.right(180)

    if oneTurtle.ycor() <= -200:
        oneTurtle.right(180)

    if oneTurtle.ycor() >= 200:
        oneTurtle.right(180)

    oneTurtle.penup()
    oneTurtle.forward(distance)


window.exitonclick()

#oneTurtle.setheading(heading)