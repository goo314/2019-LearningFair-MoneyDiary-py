import turtle as t
def move(a, b, t):
    t.penup()
    t.goto(a, b)
    t.pendown()
    return

#코_원
def circle(nose_color):
    t.color('black', nose_color)
    move(0, -60, t)
    t.begin_fill()
    t.circle(20)
    t.end_fill()
    return

#코_세모
def triangle(nose_color):
    t.color('black', nose_color)
    move(-20, -50, t)
    t.begin_fill()
    for i in range(3):
        t.forward(40)
        t.left(120)
    t.end_fill()
    return

def nose(x, y):
    if x == 'a':
        circle(y)
    else:
        triangle(y)
    return
