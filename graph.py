import turtle as t

def title(month, flow):
    t.color('black')
    t.penup()
    t.goto(0, 180)
    t.pendown()
    graph_name = '%s월 %s 내역'%(month, flow)
    t.write(graph_name, False, 'center',('돋움',40,'bold'))
    t.hideturtle()

def pieplt(total, data, colors):
    if total == 0:
        print('기록이 없습니다.')
        return
    else:
        categories = list(data.keys())
        expences = list(data.values())

        percentages = []
        for i in range(len(data)):
            percentages.append(expences[i]/total)

        t.hideturtle()
        t.penup()
        t.goto(0, -30)
        t.pendown()

        t.left(90)
        for j in range(len(percentages)):
            angle = percentages[j]*360
            if angle == 0:
                continue
            t.color('white', colors[j])
            t.pensize(2)
            t.speed(10)
            t.begin_fill() # 도형 그리기
            t.forward(180)
            t.left(90)
            t.circle(180, angle)
            t.left(90)
            t.forward(180)
            t.end_fill()
        
            t.penup()
            t.right(180 + angle/2)
            t.forward(90)
            t.pendown()

            text = '%s(%d%%)'%(categories[j],percentages[j]*100)
            t.write(text, False, 'center',('함초롬바탕',15,'bold')) # 항목 작성
            t.penup()
            t.right(180)
            t.forward(90)
            t.right(180-angle/2)
            t.pendown()
        t.speed(4)
 
