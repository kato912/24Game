import random as rd

def Start_game():
    problem_List = create_Problem()
    print(problem_List)
    len(problem_List) > 1:
        problem_List = get_input(problem_List)
        print(problem_List)
    if int(problem_List[0]) == 24:
        print("You win")
    else:
        print("You lost")
def Categorize_input(User_input):#ทำการแบ่งค่าinput ออกป็น3ชุด operator,a,b
    Index_op = 0
    operator = ['+','-','*','/']
    a = ''
    b = ''
    for i in range(len(User_input)):
        if User_input[i] in operator:
            now_op = User_input[i]
            Index_op = i
    for i in range(len(User_input)):
        if i < Index_op:
            a += User_input[i]
        elif i > Index_op:
            b += User_input[i]
    return now_op,int(a),int(b)


def get_input(y): # ทำการรับค่าinputเข้ามาคำนวล
    problem_List = []
    for i in y:
        problem_List.append(i)
    x = input()
    op , a ,b = Categorize_input(x)
    if a in problem_List and b in problem_List:
        result = caculation(op,a,b)
        problem_List.remove(a)
        problem_List.remove(b)
        problem_List.append(result)
    else:
        print("Wrong input number")
    return problem_List

def random_num():#funtion ในการrandom ตัวเลข4ตัวสำหรับโจทย์
    x = [rd.randint(1,9),rd.randint(1,9),rd.randint(1,9),rd.randint(1,9)]
    return x

def caculation(op,a,b):#funtion ในการวกลคูณหารตัวเลข
    if op == '+':
        result = a+b
    elif op=='-':
        result = a-b
    elif op == '*':
        result = a*b
    elif op == '/':
        if b == 0:
            result = 0
        else:result = a/b
    return result

def CheckCanDo():#ตรวจสอบว่าตัวเลขที่สุ่มมานั้นสามารถบวกลบคูหารกันแล้วได้24เป็นไปได้หรือไม่
    NumList = random_num()
    canDOorNot = False
    operator = ['+','-','*','/']
    for i in operator:
        for j in operator:
            for k in operator:
                if caculation(j,caculation(i,NumList[0],NumList[1]),caculation(k,NumList[2],NumList[3])) == 24:
                    canDOorNot = True
                    break
    return canDOorNot,NumList

def create_Problem():#สุ่มโจทย์จนได้เลขที่สามารถทำให้เป็น24ได้
    while (1):
        x,y = CheckCanDo()
        if x == True:
            return y

Start_game()
