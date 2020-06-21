import turtle

tom = turtle.Turtle()
canvas = turtle.Screen()

turtle.speed(1)

def funnyfunction(x, y):
    tom.penup()
    tom.goto(30,y)
    tom.pendown()

x = 10
y = 20
v = x + y

tom.goto(100,100)

funnyfunction(v)


canvas.exitonclick()