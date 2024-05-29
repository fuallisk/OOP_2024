import turtle
turtle.shape('turtle')
w0 = ((20, 0), (20, -40), (0, -40), (0, 0))
w1 = ((20, 0), (20, -40))
w2 = ((20, 0), (20, -20), (0, -40), (20, -40))
w3 = ((20, 0), (0, -20), (20, -20), (0, -40))
w4 = ((0, -20), (20, -20), (20, -40), (20, 0))
w5 = ((20, 0), (0, 0), (0, -20), (20, -20), (20, -40), (0, -40))
w6 = ((-20, -20), (-20, -40), (0, -40), (0, -20), (-20, -20))
w7 = ((20, 0), (0, -20), (0, -40))
w8 = ((0, -40), (20, -40), (20, 0), (0, 0), (0, -20), (20, -20))
w9 = ((20, 0), (20, -20), (0, -40), (20, -20), (0, -20), (0, 0))
writer = (w0, w1, w2, w3, w4, w5, w6, w7, w8, w9)
print('Введите индекс')
ind = int(input())
ind = str(ind)
print(ind)
mind = [0]*len(ind)
for i in range(len(ind)):
    mind[i] = int(ind[i])
print(mind)
x = 0
y = 0
xend = 0
for i in range(len(ind)):
    xend = x+30
    if mind[i]==1:
        y -= 20
    elif mind[i]==6:
        x += 20
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    for j in range(len(writer[mind[i]])):
        turtle.goto(x+writer[mind[i]][j][0], writer[mind[i]][j][1])
    turtle.penup()
    y = 0
    x = xend
