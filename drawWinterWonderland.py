import turtle
import random

tom = turtle.Turtle()
canvas = turtle.Screen()

tom.speed("fastest")


def drawSnowflake(numBranches, branchLength, sideBranchLength):
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)

    for j in range(numBranches):
        tom.penup()
        tom.goto(x, y)
        tom.pendown()
        tom.right(360 / numBranches)
        for i in range(branchLength):
            tom.forward(10)
            tom.right(45)
            tom.forward(sideBranchLength)
            tom.backward(sideBranchLength)
            tom.left(90)
            tom.forward(sideBranchLength)
            tom.backward(sideBranchLength)
            tom.right(45)


drawSnowflake(19, 8, 20)

# for j in range(10):
#   nb = random.randint(3, 20)
#   bl = random.randint(3, 10)
#   sbl = random.randint(3, 30)
#   drawSnowflake(nb, bl, sbl)

tom.hideturtle()

canvas.exitonclick()