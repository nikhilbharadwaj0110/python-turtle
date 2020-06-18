import turtle

canvas = turtle.Screen()

tom = turtle.Turtle()
tom.speed(100)

# body of the jet
tom.penup()
tom.goto(50, -200)
tom.pendown()
tom.left(90)
tom.forward(250)
tom.left(90)
tom.forward(50)
tom.left(90)
tom.forward(250)
tom.left(90)
tom.forward(50)
tom.left(90)
tom.forward(250)
tom.left(45)
tom.forward(50)
tom.left(110)
tom.forward(40)
tom.left(25)

# wing1

tom.penup()
tom.forward(100)
tom.pendown()
tom.right(90)
tom.forward(200)
tom.left(90)
tom.forward(25)
tom.left(90)
tom.forward(200)

# wing2

tom.penup()
tom.forward(50)
tom.pendown()

tom.forward(200)
tom.left(90)
tom.forward(25)
tom.left(90)
tom.forward(200)

# rudder1

tom.left(90)

tom.penup()
tom.forward(80)
tom.pendown()
for u in range(3):
    tom.forward(65)
    tom.left(120)

# ruder2

tom.right(90)
tom.penup()
tom.forward(50)
tom.pendown()

tom.left(90)
for u in range(3):
    tom.forward(65)
    tom.right(120)

# missile1

tom.penup()
tom.goto(200, -100)
tom.pendown()

tom.left(180)
tom.forward(100)
tom.left(90)
tom.forward(30)
tom.left(90)
tom.forward(100)
tom.left(90)
tom.forward(30)
tom.left(90)
tom.forward(100)
tom.left(60)
tom.forward(30)
tom.left(120)
tom.forward(30)
tom.left(25)

# missile2

tom.penup()
tom.goto(-100, -100)
tom.pendown()
tom.left(205)
tom.forward(100)
tom.left(90)
tom.forward(30)
tom.left(90)
tom.forward(100)
tom.left(90)
tom.forward(30)
tom.left(90)
tom.forward(100)
tom.left(45)
tom.forward(30)
tom.left(105)
tom.forward(30)
tom.left(25)

canvas.exitonclick()
