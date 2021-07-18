def drawing_emoji(items, money, minimum):
    import head as h
    import eye as e
    import nose as n
    import mood as m
    h.head(items[3], items[4])
    e.eye(items[5], items[6])
    n.nose(items[7], items[8])
    m.mood(money, minimum)
 
def making_emoji(file_name):
    f = open(file_name+'.txt', 'r')
    items = f.read().split('\n')
    f.close()

    head_dic = {'a':'원', 'b':'네모', 'c':'세모','d':'별', 'e':'하트'}
    print('얼굴 모양 =', head_dic)
    head_shape = input('얼굴 모양을 선택하세요: ')
    h_color = input('얼굴 색깔을 입력하세요(영어로): ')
    print()

    eye_dic = {'a':'원', 'b':'네모'}
    print('눈 모양 =', eye_dic)
    eye_shape = input('눈 모양을 선택하세요: ')
    e_color = input('눈 색깔을 입력하세요(영어로): ')
    print()

    nose_dic = {'a':'원', 'b':'세모'}
    print('코 모양 =', nose_dic)
    nose_shape = input('코 모양을 선택하세요: ')
    n_color = input('코 색깔을 입력하세요(영어로): ')
    print()

    f = open(file_name+'.txt', 'r')
    items = f.read().split('\n')
    f.close()

    items[3] = head_shape
    items[4] = h_color
    items[5] = eye_shape
    items[6] = e_color
    items[7] = nose_shape
    items[8] = n_color
    
    f = open(file_name+'.txt', 'w')
    for i in range(len(items)-1):
        record = items[i]+'\n'
        f.write(record)
    f.close()
    drawing_emoji(items, 1, 0)


def clear():
    import turtle as t
    t.clear()
    t.penup()
    t.home()
    t.pendown()

def condition(x, minimum):
    import turtle as t
    t.penup()
    t.goto(0, 220)
    t.pendown()
    if x > minimum:
        t.write('여유롭네요! 잘하고 있어요~', False, 'center', ('함초롬바탕', 30, 'normal'))
    elif x == minimum:
        t.write('간당간당하네요, 조금만 아껴써요!', False, 'center', ('함초롬바탕', 30, 'normal'))
    else:
        t.write('돈이 많이 부족해요! 밥은 먹고 다니는 거죠?', False, 'center', ('함초롬바탕',20,'normal'))
    t.hideturtle()
        
