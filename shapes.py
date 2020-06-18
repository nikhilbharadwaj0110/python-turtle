import turtle

tom = turtle.Turtle()
canvas = turtle.Screen()
canvas.bgcolor("black")

tom.speed(100)
tom.screen.colormode(255)

size = 20

# for i in range(251):
#     tom.color("yellow")
#     tom.forward(size)
#     tom.left(147)
#     size = size + 3


# for i in range(300):
#     tom.color("black")
#     tom.forward(size)
#     tom.left(147)
#     size = size - 2
tom.color("yellow")
for _ in range(4):
    tom.forward(150)
    tom.right(90)

tom.right(45)
tom.forward(212)
canvas.exitonclick()
