import turtle

tom=turtle.Turtle()
canvas = turtle.Screen()

tom.right(90)
tom.penup()
tom.goto(-40,45)
tom.pendown()
tom.speed(3)


for z in range (4):
  tom.forward(100)
  tom.left(90)
  
  tom.end_fill()
  
tom.forward(60)
tom.right(90)
tom.forward(135)
tom.right(90)
tom.forward(35)
tom.right(90)
tom.forward(135)

tom.penup()
tom.goto(60,20)
tom.pendown()
tom.forward(135)
tom.right(90)
tom.forward(35)
tom.right(90)
tom.forward(135)

tom.left(90)
tom.forward(40)
tom.right(90)
tom.forward(70)
tom.left(90)
tom.forward(135)
tom.right(90)
tom.forward(30)
tom.right(90)
tom.forward(135)
tom.right(90)
tom.forward(100)
tom.right(90)
tom.forward(135)
tom.right(90)
tom.forward(35)
tom.right(90)
tom.forward(135)

tom.penup()
tom.goto(45,80)
tom.pendown()
tom.circle(35)


tom.penup()
tom.goto(30,80)
tom.pendown()
tom.circle(5)


tom.penup()
tom.goto(0,80)
tom.pendown()
tom.circle(5)


tom.penup()
tom.goto(0,60)
tom.pendown()
tom.right(180)
tom.circle(10,180)

tom.right(180)
tom.penup()
tom.goto(10,50)
tom.pendown()
tom.forward(110)


canvas.exitonclick()
