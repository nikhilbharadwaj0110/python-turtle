import  turtle
import  random

tom=turtle.Turtle()
tom.speed(200)
tom.pensize(5)
size=20

tom.screen.colormode(255)

for i in range(150):
  tom.forward(size)
  tom.right(135)
  tom.forward(10)
  tom.backward(10)
  tom.right(90)
  tom.forward(10)
  tom.backward(10)
  size=size+5
  r=random.randint(0,255)
  g=random.randint(0,255)
  b=random.randint(0,255)
  tom.color(r,b,g)

