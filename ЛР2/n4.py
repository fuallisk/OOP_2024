import turtle
x, y = 0, 0
vx, vy = 5, 60
a = -9.81
turtle.tracer(2)
for t in range(6000):
    if y <= 0:
        vy = abs(vy)*0.95
    x += vx * 0.1
    y += vy * 0.1 + a * 0.1 ** 2 / 2
    vy += a * 0.1
    turtle.goto(x, y)
