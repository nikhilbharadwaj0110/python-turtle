import turtle

tom = turtle.Turtle()
canvas = turtle.Screen()

def init():
    tom.speed(5)
    canvas.bgcolor("black")

def drawTriangle():
    for _ in range(3):
        tom.forward(50)
        tom.right(-120)

def drawSquare():
    for _ in range(4):
        tom.forward(50)
        tom.left(90)

def drawPentagon():
    for _ in range(5):
        tom.forward(50)
        tom.left(72)

def drawHexagon():
    for _ in range(6):
        tom.forward(50)
        tom.left(60)

def drawSeptagon():
    for _ in range(7):
        tom.forward(50)
        tom.left(51)

def drawOctagon():
    for _ in range(8):
        tom.forward(50)
        tom.left(45)

def drawNonagon():
    for _ in range(9):
        tom.forward(50)
        tom.left(40)

def drawDecagon():
    for _ in range(10):
        tom.forward(50)
        tom.left(36)

def drawShape(x, y, shape, shapeColor):
    tom.penup()
    tom.goto(x, y)
    tom.fillcolor(shapeColor)
    tom.color(shapeColor)
    tom.begin_fill()
    tom.pendown()

    if shape == "triangle":
        drawTriangle()
    elif shape == "square":
        drawSquare()
    elif shape == "pentagon":
        drawPentagon()
    elif shape == "hexagon":
        drawHexagon()
    elif shape == "septagon":
        drawSeptagon()
    elif shape == "octagon":
        drawOctagon()
    elif shape == "nonagon":
        drawNonagon()
    elif shape == "decagon":
        drawDecagon()

    tom.end_fill()


init()

drawShape(-450,0, "triangle", "turquoise2")
drawShape(-375,0, "square", "teal")
drawShape(-300,0,"pentagon", "yellow")
drawShape(-200,0, "hexagon", "magenta")
drawShape(-90,0, "septagon", "purple")
drawShape(40,0, "octagon", "coral3")
drawShape(180,0, "nonagon", "red")
drawShape(350,0, "decagon", "green")

canvas.exitonclick()