from turtle import *
from colorsys import *

speed(0)
bgcolor('blue')
pensize(2)
colormode(1.0)

n = 100
h = 0

scale = 0.5

penup()
setposition (0,0)
pendown()

for j in range (120):
 for i in range(4):
     color(hsv_to_rgb(h , 1 , 1))
     h +=0.003
     circle((40 + i * 5) * scale , 90)
     forward(250 * scale )
     left(90)
     
     right(10)

hideturtle()
done()
 