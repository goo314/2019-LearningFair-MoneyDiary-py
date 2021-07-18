import turtle as t
def move(a, b, t):
    t.penup()
    t.goto(a, b)
    t.pendown()
    return

#얼굴_원
def circle(head_color):
    t.pensize(1)
    t.color('black', head_color)
    move(0, -200, t)
    t.begin_fill()
    t.circle(200)
    t.end_fill()
    return

#얼굴_네모
def square(head_color):
    t.pensize(1)
    t.color('black', head_color)
    move(-200, -200, t)
    t.begin_fill()
    for i in range(4):
        t.forward(400)
        t.left(90)
    t.end_fill()
    return

#얼굴_세모
def triangle(head_color):
    t.pensize(1)
    t.color('black', head_color)
    move(-270, -250, t)
    t.begin_fill()
    for i in range(3):
        t.forward(540)
        t.left(120)
    t.end_fill()
    return

#얼굴_별
def star(head_color):
    t.pensize(1)
    t.color(head_color)
    move(280, 60, t)
    t.left(36)
    t.begin_fill()
    for i in range(5):
        t.left(144)
        t.forward(550)
    t.end_fill()
    t.right(36)
    return

# 얼굴_하트
def heart(head_color):
    t.pensize(1)
    import math as m
    t.color(head_color)
    t.begin_fill()
    for x in range(100):
        h = m.pi*x/50
        x = 160*m.sin(h)**3
        y = 130*m.cos(h)-50*m.cos(2*h)-20*m.cos(3*h)-10*m.cos(4*h)
        t.goto(1.5*x, 1.5*y)
    t.end_fill()
    return

def head(x, y):
    if x == 'a':
        circle(y)
    elif x == 'b':
        square(y)
    elif x == 'c':
        triangle(y)
    elif x == 'd':
        star(y)
    elif x == 'e':
        heart(y)
