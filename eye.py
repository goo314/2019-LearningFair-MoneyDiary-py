import turtle as t
def move(a, b, t):
    t.penup()
    t.goto(a, b)
    t.pendown()

#눈_원
def circle(eye_color):
    t.begin_fill()
    t.color('black', eye_color)
    move(-80, 0, t)
    t.circle(40)
    t.end_fill()
    move(80, 0, t)
    t.begin_fill()
    t.circle(40)
    t.end_fill()
    return

#눈_네모
def square(eye_color):
    t.color('black', eye_color)
    move(-120, 0, t)
    t.begin_fill()
    for i in range(4):
        t.forward(70)
        t.left(90)
    t.end_fill()
    move(50, 0, t)
    t.begin_fill()
    for i in range(4):
        t.forward(70)
        t.left(90)
    t.end_fill()
    return

#눈_세모
def triangle(eye_color):
    t.color('black', eye_color)
    move(-130, 0, t)
    t.begin_fill()
    for i in range(3):
        t.forward(80)
        t.left(120)
    t.end_fill()
    move(50, 0, t)
    t.begin_fill()
    for i in range(3):
        t.forward(80)
        t.left(120)
    t.end_fill()
    return

def eye(x, y):
    if x == 'a':
        circle(y)
    elif x == 'b':
        square(y)
    else:
        triangle(y)
    return
