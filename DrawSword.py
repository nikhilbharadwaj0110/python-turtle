import turtle

tom=turtle.Turtle()
tom.speed(200)
canvas = turtle.Screen()
canvas.bgcolor("black")

def gotoPos(x, y):
    tom.penup()
    tom.goto(x, y)
    tom.pendown()


#sword body
gotoPos(0,-200)
tom.color("yellow")
tom.begin_fill()
for _ in range(3):
    tom.forward(45)
    tom.left(90)
    tom.forward(350)
    tom.left(90)


tom.right(60)
tom.forward(45)
tom.left(120)
tom.forward(45)
tom.end_fill()

gotoPos(125,-105)
tom.color("yellow")
tom.begin_fill()
tom.right(55)
tom.right(90)
tom.right(180)
tom.right(3)
for _ in range(2):
    tom.forward(35)
    tom.right(90)
    tom.forward(100)
    tom.right(90)

tom.left(60)
tom.forward(35)
tom.right(120)
tom.forward(35)
tom.end_fill()

gotoPos(-80,-140)
tom.color("yellow")
tom.begin_fill()
tom.right(5)
tom.right(270)
tom.right(180)
tom.right(45)
tom.left(18)
for _ in range(2):
    tom.forward(35)
    tom.right(90)
    tom.forward(100)
    tom.right(90)

tom.left(60)
tom.forward(35)
tom.right(120)
tom.forward(35)
tom.end_fill()


gotoPos(-200,-85)

tom.color("yellow")
tom.begin_fill()
tom.circle(75)
tom.end_fill()

gotoPos(-305,-28)
tom.color("gray")
tom.begin_fill()
for i in range(5):
    tom.forward(130)
    tom.right(144)

tom.end_fill()



















canvas.exitonclick()

