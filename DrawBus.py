import turtle

tom = turtle.Turtle()
canvas = turtle.Screen()
tom.speed(10)
tom.penup()
tom.goto(-400,100)
tom.pendown()

tom.fillcolor("yellow")
tom.begin_fill()


tom.right(90)
tom.forward(300)
tom.left(90)
tom.forward(800)
tom.left(90)
tom.forward(150)
tom.left(90)
tom.forward(200)
tom.right(90)
tom.forward(150)
tom.left(90)
tom.forward(600)

tom.end_fill()

tom.penup()
tom.goto(-235,40)
tom.pendown()

# Drawing windows
tom.fillcolor("light gray")
xpos = -305
for _ in range(4):
    tom.penup()
    tom.goto(xpos, 5) 
    tom.begin_fill()
    tom.pendown()
    for g in range (4):
        tom.forward(80)
        tom.right(90)
    tom.end_fill()
    xpos = xpos + 100


# Drawing Door
tom.penup()
tom.goto(190,90)
tom.pendown()

tom.fillcolor("light gray")
tom.begin_fill()

tom.forward(100)
tom.left(90)
tom.forward(290)
tom.left(90)
tom.forward(100)
tom.left(90)
tom.forward(290)

tom.end_fill()

tom.penup()
tom.goto(140,90)
tom.pendown()

tom.left(180)
tom.forward(290)



# Draw horizontal band
tom.penup()
tom.goto(-400,-50)
tom.left(90)
tom.pendown()
tom.forward(490)

tom.penup()
tom.goto(-400,-60)
tom.fillcolor("black")
tom.pendown()
tom.begin_fill()
for _ in range(2):
    tom.forward(490)
    tom.right(90)
    tom.forward(30)
    tom.right(90)

tom.end_fill()

# Draw wheels
tom.fillcolor("black")

xpos = -200

for _ in range(2):
    tom.penup()
    tom.goto(xpos,-260)
    tom.pendown()
    tom.begin_fill()
    tom.circle(60)
    tom.end_fill()
    xpos = xpos + 500


# Print "School Bus"
tom.penup()
tom.goto(-200,-85)

tom.color("white")
tom.pendown()
tom.write("School Bus", font=("Arial", 14, "bold"))

# Move tom away
tom.penup()
tom.goto(400,400)



# exit canvas on click
canvas.exitonclick()
