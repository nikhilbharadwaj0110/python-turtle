import turtle

tom = turtle.Turtle()
canvas = turtle.Screen()

tom.speed(1000)

# for _ in range(4):
#     tom.color("black")
#     posy = -400
#     circleSize = 400
#     for _ in range(80):
#         tom.penup()
#         tom.goto(0,posy)
#         tom.pendown()
#         tom.circle(circleSize)
#         posy = posy + 5
#         circleSize = circleSize -5
#
#     colorRed = "red"
#     colorBlue = "blue"
#     colorGreen = "green"
#     initColor =  "red"
#
#     posy = -5
#     circleSize = 5
#     for _ in range(80):
#         if initColor == "red":
#             tom.color(colorBlue)
#             initColor = colorBlue
#         elif initColor == "blue":
#             tom.color(colorGreen)
#             initColor = colorGreen
#         elif initColor == "green":
#             tom.color(colorRed)
#             initColor = "red"
#         tom.penup()
#         tom.goto(0,posy)
#         tom.pendown()
#         tom.circle(circleSize)
#         posy = posy - 5
#         circleSize = circleSize + 5



canvas.bgcolor("black")

tom.color("orange")
tom.fillcolor("teal")
tom.begin_fill()
for i in range(100):
    tom.forward(i*3)
    tom.left(115)
tom.end_fill()
canvas.exitonclick()
