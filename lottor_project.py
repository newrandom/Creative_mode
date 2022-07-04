# 로또 번호 생성기
from ast import Global
from optparse import Values
from tkinter import *
from random import sample
from tkinter.ttk import Combobox

# =========  함수  ======== #
def create_lot_num():       # entry > button > message

    except_string = entry.get()
    
    if except_string == '':
        lotto_num = sample(range(1,46),6)

    elif except_string != '':     # 빈칸이 아닌경우
        except_string = except_string.split()

        except_num = []
        for str in except_string:
            except_num.append(int(str))
        
        # 로또번호 제외 라인
        a = True
        while a:
            lotto_num = sample(range(1,46),6)       # list

            for num in except_num:
                if num in lotto_num:
                    break
                elif num == except_num[-1]:
                    if num not in lotto_num:
                        a = False

    # message widget에 넣기
    message['text']=lotto_num

# =========  상단  frame  ========= #

# 탑레벨 위젯
window = Tk()
window.geometry('500x400')
window.title('로또번호 조회기')
window.resizable(0,0)

# main_label
main_label = Label(text='본 프로그램은 당첨을 확정해주는 프로그램이 아닙니다.', width = 490, justify='center', font=("Helvetica", 14, 'bold'))
main_label.place(relx=0.15, y = 5, relwidth=0.7, height=30)

# title_label
title_label = Label(text='제외할 숫자를 쓰세요 (예 : 1 25 33)', width=490,justify='center', )# borderwidth=1, relief='ridge')
title_label.place(relx=0.3, y = 35, relwidth=0.4, height=20)

# Entry     # 입력을 받아서 출력으로 넘길 때 사용하는 툴
entry = Entry(background='lightsteelblue', justify='center', borderwidth=2, relief='ridge')
entry.place(relx = 0.1, y = 60, relwidth=0.8, height = 50, )#width = 490, height = 80)
# entry.pack(fill=BOTH, expand=1)
entry.focus()

# button
button = Button(text='🎡', command=create_lot_num,  foreground='black',) # borderwidth = 2, relief='sunken')
button.place(relx=0.1, y=110, relwidth = 0.8, height = 50)
# button.pack(fill=BOTH,expand=1)

# message
message = Message(text='특정 숫자를 제외한 나머지 숫자가 무작위로 나옵니다',width=145, background='pink', foreground='green')
message.place(relx=0, y = 165, relwidth = 1, height = 50)
# message.pack(fill=Y,expand=1)

# ================== 하단 frame ===================== #

# button - 최근 10회 가장 많이 나온 번호 조회
top_10_button = Button(text='최근 TOP 10',background='lightyellow', command=None)
top_10_button.place(relx=0.01, y=220, relwidth=0.2, height=50)

# button - 최근 25회 번호 조회
top_25_button = Button(text='최근 TOP 25', command=None)
top_25_button.place(relx=0.26, y = 220, relwidth=0.2, height=50)

# button - 최근 50회 번호 조회
top_50_button = Button(text='최근 TOP 50', command=None)
top_50_button.place(relx = 0.51, y = 220, relwidth=0.2, height=50)

# button - 전체 번호 조회
all_num_button = Button(text='전체 번호 조회', command=None)
all_num_button.place(relx=0.76, y = 220, relwidth=0.2, height=50)


# message - 번호 조회 창
print_nums_message = Message(text='🤔', background='white', foreground='black', width=145)
print_nums_message.place(relx=0, y = 275, relwidth=1, height=50)

# combobox_start - 조회 시작 칸
combobox_start = Combobox(window, values=[i for i in range(1, 1001)])
combobox_start.place(relx=0.01, y = 330, relwidth=0.2, height=25, )
combobox_start.set('시작')
a = combobox_start.get()

# combobox_end - 조회 종료 칸
combobox_end = Combobox(window, values=[i for i in range(1, 1001)])
combobox_end.place(relx=0.01, y = 360, relwidth=0.2, height=25, )
combobox_end.set('종료')
b = combobox_end.get()

# search_button - combobox 조회버튼
search_button = Button(text='{} 부터 {} 까지 조회'.format(a,b), command=None)
search_button.place(relx=0.25, y = 330, relwidth=0.3, height=55, )


# window.Looping
window.mainloop()