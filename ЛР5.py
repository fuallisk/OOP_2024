import pygame
from pygame.draw import *
from random import randint,choice


pygame.init()
pygame.font.init()

FPS = 30
WIDTH = 1200
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Цвета
RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
GREEN = (0,255,0)
MAGENTA = (255,0,255)
CYAN = (0,255,255)
BLACK = (0,0,0)
COLORS = [RED,BLUE,YELLOW,GREEN,MAGENTA,CYAN]

NUM_BALLS = 15
balls = []

score = 1

def new_ball():
    '''Создает новый шарик со случайными параметрами.'''
    x = randint(100,1100)
    y = randint(100,600)
    r = randint(10,100)
    color = [randint(0, 255), randint(0, 255), randint(0, 255)]
    dx,dy = randint(-5,5),randint(-5,5)
    return [x,y,r,color,dx,dy]

def draw_ball(ball):
    '''Рисует шарик на экране.'''
    circle(screen,ball[3],(ball[0],ball[1]),ball[2])

def move_ball(ball):
    '''Обновляет положение шарика, учитывая столкновения со стенами.'''
    ball[0] += ball[4]
    ball[1] += ball[5]
    ball[3] = choice(COLORS)
    if ball[0] - ball[2] < 0 or ball[0] + ball[2] > WIDTH:
        ball[4] = -ball[4]
    if ball[1] - ball[2] < 0 or ball[1] + ball[2] > HEIGHT:
        ball[5] = -ball[5]

def check_click(event,ball):
    '''Проверяет, попал ли клик в шарик.'''
    distance = ((event.pos[0] - ball[0])**2 + (event.pos[1] - ball[1])**2)**0.5
    return distance < ball[2]


for _ in range(NUM_BALLS):
    balls.append(new_ball())

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for ball in balls:
                if check_click(event,ball):
                    score += 1
                    print("Score:", score)
                    balls.remove(ball)
                    balls.append(new_ball())

    screen.fill(BLACK)
    x, y = pygame.mouse.get_pos()
    x-=30
    y-=30
    clicker = pygame.font.Font(None, 64)
    click = clicker.render(str(score), True, choice(COLORS))
    screen.blit(click, (x, y))
    for ball in balls:
        draw_ball(ball)
        move_ball(ball)
        pygame.font.init()
    pygame.display.update()

pygame.quit()
