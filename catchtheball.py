import turtle
import random

canvas = turtle.Screen()

tom = turtle.Turtle()
tom.color("blue")
jim = turtle.Turtle()
jim.color("blue")
kim = turtle.Turtle()
kim.color("red")
result = turtle.Turtle()
result.hideturtle()

scorekeeper = turtle.Turtle()
scorekeeper.color("red")
border = turtle.Turtle()
timekeeper = turtle.Turtle()
border.speed(200)
border.hideturtle()
border.penup()
border.goto(-450, 300)
border.pendown()

for _ in range(2):
    border.forward(900)
    border.right(90)
    border.forward(600)
    border.right(90)

tom.shape("turtle")
tom.setheading(90)
tom.penup()
tom.goto(-50, -280)
tom.pendown()

kim.shape("turtle")
kim.setheading(90)
kim.penup()
kim.goto(50, -280)
kim.pendown()


def moveLeft():
    posX = tom.xcor()
    tom.penup()
    tom.goto(posX - 10, -280)


def moveRight():
    posX = tom.xcor()
    tom.penup()
    tom.goto(posX + 10, -280)


def moveLefti():
    posX = kim.xcor()
    kim.penup()
    kim.goto(posX - 10, -280)


def moveRighti():
    posX = kim.xcor()
    kim.penup()
    kim.goto(posX + 10, -280)


canvas.onkey(moveLeft, "left")
canvas.onkey(moveRight, "right")
canvas.onkey(moveRighti, "d")
canvas.onkey(moveLefti, "a")
canvas.listen()

turtles = []

for i in range(10):
    x = random.randint(-355, 375)

    tim = turtle.Turtle()
    tim.speed(200)

    tim.color("red")
    tim.shape("circle")
    tim.setheading(270)
    tim.hideturtle()
    tim.penup()
    tim.goto(x, 290)
    tim.pendown()
    tim.showturtle()

    turtles.append(tim)

nikhil = []

for i in range(5):
    x = random.randint(-355, 375)

    t = turtle.Turtle()
    t.speed(200)

    t.color("black")
    t.shape("circle")
    t.setheading(270)
    t.hideturtle()
    t.penup()
    t.goto(x, 290)
    t.pendown()
    t.showturtle()

    nikhil.append(t)

jim.hideturtle()
jim.speed(100)
jim.penup()
jim.goto(-420, 320)
jim.pendown

scorekeeper.hideturtle()
scorekeeper.speed(100)
scorekeeper.penup()
scorekeeper.goto(-300, 320)
scorekeeper.pendown

timekeeper.hideturtle()
timekeeper.speed(100)
timekeeper.penup()
timekeeper.goto(-180, 320)
timekeeper.pendown

Score1 = 0
Score2 = 0
timeLimit = 300
endGame = False

while True:
    jim.clear()
    jim.write("Score1 : " + str(Score1), font=("Arial", 12, "bold"))

    scorekeeper.clear()
    scorekeeper.write("Score2 : " + str(Score2), font=("Arial", 12, "bold"))
    timeLimit = timeLimit - 1
    timekeeper.clear()
    timekeeper.write("Time Left : " + str(timeLimit), font=("Arial", 12, "bold"))

    for oneturtle in turtles:
        x = random.randint(-355, 375)
        oneturtle.speed(200)
        speed = random.randint(5, 20)

        oneturtle.penup()
        oneturtle.forward(speed)

        if oneturtle.ycor() <= -300:
            oneturtle.goto(x, 290)

        if abs(oneturtle.xcor() - tom.xcor()) < 20 and abs(oneturtle.ycor() - tom.ycor()) < 20:
            Score1 = Score1 + 1
            oneturtle.goto(x, 290)

        if abs(oneturtle.xcor() - kim.xcor()) < 20 and abs(oneturtle.ycor() - kim.ycor()) < 20:
            Score2 = Score2 + 1
            oneturtle.goto(x, 290)

    for oneturtles in nikhil:
        x = random.randint(-355, 375)
        oneturtles.speed(200)
        speed = random.randint(5, 20)

        oneturtles.penup()
        oneturtles.forward(speed)

        if oneturtles.ycor() <= -300:
            oneturtles.goto(x, 290)

        if abs(oneturtles.xcor() - tom.xcor()) < 20 and abs(oneturtles.ycor() - tom.ycor()) < 20:
            Score1 = Score1 - 3
            oneturtle.goto(x, 290)

        if abs(oneturtles.xcor() - kim.xcor()) < 20 and abs(oneturtles.ycor() - kim.ycor()) < 20:
            Score2 = Score2 - 3
            oneturtle.goto(x, 290)

        if timeLimit <= 0:
            endGame = True
            break

    if endGame:
        break

if Score1 > Score2:
    res = "Game over! Blue turtle won."
    result.color("blue")
elif Score2 > Score1:
    res = "Game over! Red turtle won."
    result.color("red")
else:
    res = "Game over! It's a tie."
    result.color("green")

result.penup()
result.goto(-100, 0)

result.write(res, font=("Arial", 20, "bold"))

canvas.onkey(None, "left")
canvas.onkey(None, "right")
canvas.onkey(None, "d")
canvas.onkey(None, "a")



