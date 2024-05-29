import turtle
from random import *


turtle.tracer(10)

number_of_turtles = 50
steps_of_time_number = 10000


pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.speed(50)
    unit.goto(randint(-200, 200), randint(-200, 200))


for i in range(steps_of_time_number):
    for unit in pool:
        unit.forward(randint(-100,100))
        unit.right(randint(-100,100))


turtle.getscreen()._root.mainloop()
