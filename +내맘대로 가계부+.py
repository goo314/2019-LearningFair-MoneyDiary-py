print('+내맘대로 가계부+')
print('"환영합니다! +내맘대로 가계부+는 데이터 백업, 계산기, 통계 기능뿐만 아니라')
print('최소 잔액과 자신만의 캐릭터를 설정해 돈을 현명하게 관리할 수 있습니다."')
print()
choice1 = input('새로 만들려면 A, 불러오려면 B: ')
if choice1 == 'A':
    file_name = input('가계부 이름을 입력하세요: ')
    f=open(file_name+'.txt', 'w')
    f.write(file_name+'\n')
    money = input('잔액을 입력하세요: ')
    f.write(money+'\n')
    minimum = input('살아남기 위한 최소 잔액을 입력하세요: ')
    f.write(minimum+'\n')
    for i in range(6):
        f.write('\n')
    f.close()
    print()
    print('자신만의 캐릭터를 만들어봅시다')
    import emoji
    emoji.making_emoji(file_name)
    print('당신의 캐릭터가 완성되었습니다!')

if choice1 == 'B':
    file_name = input('불러올 가계부 이름을 입력하세요: ')
    f=open(file_name+'.txt', 'r')
    items = f.read().split('\n')
    print('잔액은',items[1], '입니다')
    f.close()

#메뉴선택
menu={1:'가계부 이름 변경',2:'잔액 변경',3:'최소 기준 변경',4:'이모지 설정',5:'수입 기록',6:'지출 기록',7:'월말결산',8:'나가기'}
while True:
    print('-'*80)
    print('메뉴 =',menu)
    m_choice = int(input('메뉴를 선택하세요: '))

#가계부 이름 변경
    if m_choice == 1:
        print()
        print('<1:가계부 이름 변경>을 선택하셨습니다.')
        f = open(file_name+'.txt', 'r')
        items = f.read().split('\n')
        f.close()
        print('기존 이름은',items[0],'입니다.')
        c_name = input('이름을 변경하시겠습니까 (Y/N): ')
        
        if c_name == 'Y':
            name = input('변경할 이름을 입력하세요: ')
            items[0] = name
            file_name = name
            f = open(file_name+'.txt', 'w')
            for i in items:
                f.write(i+'\n')
            f.close()
        else:
            continue

#잔액 변경   
    if m_choice == 2:
        print()
        print('<2:잔액 변경>을 선택하셨습니다.')
        f = open(file_name+'.txt', 'r')
        items = f.read().split('\n')
        f.close()
        print('기존 잔액은',items[1],'입니다.')
        c_money = input('잔액을 변경하시겠습니까? (Y/N): ')
        
        if c_money == 'Y':
            money = input('변경할 잔액을 입력하세요: ')
            items[1] = money
            f = open(file_name+'.txt', 'w')
            for i in items:
                f.write(i+'\n')
            f.close()

#기준설정    
    if m_choice == 3:
        print()
        print('<3:최소 기준 변경>을 선택하셨습니다.')
        f = open(file_name+'.txt', 'r')
        items = f.read().split('\n')
        f.close()
        print('기존 살아남기 위한 최소 잔액은',items[2],'입니다.')
        c_minimum = input('살아남기 위한 최소 잔액을 변경하시겠습니까? (Y/N): ')
        if c_minimum == 'Y':
            minimum = input('변경할 최소 잔액을 입력하세요: ')
            items[2] = minimum
            f = open(file_name+'.txt', 'w')
            for i in items:
                f.write(i+'\n')
            f.close()

#이모지 설정
    if m_choice == 4:
        print()
        print('<4:이모지 설정>을 선택하셨습니다.')
        import emoji
        emoji.clear()
        emoji.making_emoji(file_name)
        print('당신의 새로운 캐릭터입니다!')
    

# 수입기록
    if m_choice == 5:
        print()
        print('<5:수입 기록>을 선택하셨습니다.')
        month, date = input('오늘의 날짜는 무엇입니까? (월/일): ').split('/')
        income_dic = {'a':'알바비', 'b':'용돈', 'c':'기타'}
        print(income_dic)
        part = input('분류를 선택하세요: ')
        income = input('금액은 얼마인가요?: ')
        income_record = '수입 %s %s %s %s\n'%(month, date, income_dic[part], income)
        f = open(file_name+'.txt', 'r')
        items = f.read().split('\n')
        f.close()
        items.append(income_record)
        money = int(items[1])+int(income)
        items[1] = str(money)
        minimum = int(items[2])
        f = open(file_name+'.txt', 'w')
        for i in items:
            f.write(i+'\n')
        f.close()
        print('살아남기 위한 최소 잔액:',items[2]+'원')
        print('잔액은', str(money)+'원 입니다')
        minimum = int(items[2])
        import emoji
        emoji.clear()
        emoji.drawing_emoji(items, int(money), int(minimum))
        emoji.condition(int(money), int(minimum))

# 지출기록
    if m_choice == 6:
        print()
        print('<6:지출 기록>을 선택하셨습니다.')
        month, date = input('오늘의 날짜는 무엇입니까? (월/일):').split('/')
        spending_dic = {'a':'생활비','b':'식비','c':'패션/미용비','d':'여가비','e':'교통비','f':'기타'}
        print(spending_dic)
        part = input('분류를 선택하세요: ')
        spending = input('금액은 얼마입니까?: ')
        spending_record = '지출 %s %s %s %s\n'%(month, date, spending_dic[part],spending)
        f = open(file_name+'.txt', 'r')
        items = f.read().split('\n')
        f.close()
        items.append(spending_record)
        money = int(items[1])-int(spending)
        items[1] = str(money)
        f = open(file_name+'.txt', 'w')
        for i in items:
            f.write(i+'\n')
        f.close()
        print('살아남기 위한 최소 잔액:',items[2]+'원')
        print('잔액은', str(money)+'원 입니다')
        minimum = int(items[2])
        import emoji
        emoji.clear()
        emoji.drawing_emoji(items, int(money), int(minimum))
        emoji.condition(int(money), int(minimum))

# 결산
    if m_choice == 7:
        print()
        print('<7:월말결산>을 선택하셨습니다.')
        f = open(file_name+'.txt', 'r')
        items = f.read().split('\n')
        f.close()
        for i in range(9, len(items)):
            lst = items[i].split(' ')
            items[i] = lst
        print('현재 잔액은',items[1]+'원 입니다.')
        check_month = input('결산을 원하는 Month를 입력하세요: ')        
        flow = input('어떤 것을 보시겠습니까? (수입/지출): ' )

        if flow == '수입':
            total_income = 0
            wage = 0
            cash = 0
            etc = 0
            for i in range(9, len(items)):
                if items[i][0] == '수입' and items[i][1] == check_month:
                    total_income = total_income+int(items[i][4])
                    if items[i][3] == '알바비':
                        wage += int(items[i][4])
                    if items[i][3] == '용돈':
                        cash += int(items[i][4])
                    if items[i][3] == '기타':
                        etc += int(items[i][4])
            print()
            print(check_month+'월의 총 수입은 %d원입니다.'%total_income)
            print('알바비: %d원'%wage)
            print('용돈: %d원'%cash)
            print('기타: %d원'%etc)
            
            income_data = {'알바비':wage, '용돈':cash, '기타':etc}
            colors = ['gold', 'royal blue', 'tomato']
            import emoji
            emoji.clear()
            import graph
            graph.title(str(check_month), flow)
            graph.pieplt(total_income, income_data, colors)

        else:
            total_spending = 0
            living = 0
            food = 0
            beauty = 0
            leisure = 0
            transportation = 0
            etc = 0
            for i in range(9, len(items)):
                if items[i][0] == '지출' and items[i][1] == check_month:
                    total_spending = total_spending+int(items[i][4])
                    if items[i][3] == '생활비':
                        living += int(items[i][4])
                    elif items[i][3] == '식비':
                        food += int(items[i][4])
                    elif items[i][3] == '패션/미용비':
                        beauty += int(items[i][4])
                    elif items[i][3] == '여가비':
                        leisure += int(items[i][4])
                    elif items[i][3] == '교통비':
                        transportation += int(items[i][4])
                    elif items[i][3] == '기타':
                        etc += int(items[i][4])
            print()
            print(check_month+'월의 총 지출은 %d원입니다.'%total_spending)
            print('생활비: %d원'%living)
            print('식비: %d원'%food)
            print('패션/미용비: %d원'%beauty)
            print('여가비: %d원'%leisure)
            print('교통비: %d원'%transportation)
            print('기타: %d원'%etc)
            
            spending_data = {'생활비':living, '식비':food, '패션/미용비':beauty, '여가비':leisure, '교통비':transportation, '기타':etc}
            colors = ['gold', 'royal blue', 'tomato', 'lightblue', 'lightgreen', 'gray']
            import emoji
            emoji.clear()
            import graph
            graph.title(str(check_month), flow)
            graph.pieplt(total_spending, spending_data, colors)
            
    if m_choice == 8:
        print('+내맘대로 가계부+를 종료합니다.')
        break
