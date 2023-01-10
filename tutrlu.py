from turtle import *
from colorsys import *
bgcolor("Black")
tracer(50)
pensize(7)
goto(-40,-300)
c = ["red", "yellow"]
rt(4)
for i in range(300):
    color(c[i%2])
    up()
    circle(300-i,-92)
    down()
    circle(300-i,-92)
done()