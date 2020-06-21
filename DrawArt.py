import turtle

window = turtle.Screen()
window.bgcolor("black")

tom = turtle.Turtle()
tom.screen.colormode(255)
tom.hideturtle()
tom.speed(100)

tom.color("yellow")
for _ in range(6):
    circleSize = 8
    for _ in range(10):
        tom.circle(circleSize)
        circleSize = circleSize + 5

    tom.left(60)

tom.color("cyan")
for _ in range(6):
    circleSize = 15
    for _ in range(10):
        tom.circle(circleSize)
        circleSize = circleSize + 5

    tom.left(60)

tom.color("blue")
for _ in range(6):
    circleSize = 21
    for _ in range(10):
        tom.circle(circleSize)
        circleSize = circleSize + 5

    tom.left(60)

tom.color("green")
for _ in range(6):
    circleSize = 27
    for _ in range(10):
        tom.circle(circleSize)
        circleSize = circleSize + 5

    tom.left(60)

window.exitonclick()
