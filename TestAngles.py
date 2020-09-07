import turtle
import time

canvas = turtle.Screen()

# tom = turtle.Turtle()
#
#
# turtle.speed(1)
#
# def funnyfunction(x, y):
#     tom.penup()
#     tom.goto(30,y)
#     tom.pendown()
#
# x = 10
# y = 20
# v = x + y
#
# tom.goto(100,100)
#
# funnyfunction(v)
#
#
# nikhil = turtle.Turtle()
#
# nikhil.penup()
# nikhil.goto(-400, 200)
# nikhil.hideturtle()
# rules = "RULES: This game is known as \"Catch the Ball\", game.  This is a two player Game. \nPlayer 1 is the blue turtle and Player 2 is the red turtle.  \nThe players have to use \"left\" and \"right\" arrow (blue turtle) and keys \"a\" & \"d\" (red turtle) \nto move their turtles to catch and eat the red balls that are falling from sky.  \nThe game score will be shown in green and red color respectively at the top of the screen. \nThe players will have 300 sec to catch as much balls as they can to get higher score.  \nThe player with most score at the end of the game wins."
#
# nikhil.write(rules, font=("Lucida Console", 12))
#
# time.sleep(5)

tom = turtle.Turtle()
tom.shape("square")
tom.shapesize(6,0.75)

while True:
    tom.penup()
    tom.forward(2)
    if tom.xcor() > 300:
        tom.hideturtle()
        tom.goto(-200,0)
        tom.showturtle()
canvas.exitonclick()
