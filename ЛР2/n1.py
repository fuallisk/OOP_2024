import turtle
from random import *

turtle.shape('turtle')
turtle.tracer(2)
turtle.width(2)
a = randint(100, 1000)
for i in range(a):
    turtle.right(randint(0, 360))
    turtle.forward(randint(0, 100))
    
