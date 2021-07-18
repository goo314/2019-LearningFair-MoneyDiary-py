import turtle as t
def move(a, b, t):
    t.penup()
    t.goto(a, b)
    t.pendown()
    return

def notbad():
    t.pensize(10)
    # 눈썹
    move(-125, 80, t)
    t.forward(80)

    move(40, 80, t)
    t.forward(80)
 
    # 입
    move(0, -160, t)
    t.circle(25)
    return

def good():
    t.pensize(10)
    # 눈썹
    move(-125, 80, t)
    for i in range(2):
        t.left(30)
        t.forward(50)
        t.right(60)
        t.forward(50)
        t.left(30)
        move(40, 80, t)
    # 입
    move(85, -80, t)
    t.fillcolor('red')
    t.right(180)
    t.begin_fill()
    t.forward(170)
    t.left(90)
    t.circle(85, 180)
    t.end_fill()
    return

def bad():
    t.pensize(10)
    # 눈썹
    move(-125, 110, t)
    t.pensize(10)
    t.right(28)
    t.forward(100)
    t.left(28)

    move(125, 110, t)
    t.left(28)
    t.backward(100)
    t.right(28)
    # 입
    move(75, -140, t)
    t.left(125)
    t.circle(85, 110)
    return

def mood(x, minimum):
    if x > minimum:
        good()
    elif x == minimum:
        notbad()
    else:
        bad()
    return

