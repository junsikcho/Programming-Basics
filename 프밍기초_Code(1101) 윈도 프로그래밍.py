# Code10-01.py
from tkinter import * # tkinter는 파이썬에서 GUI 관련 모듈을 제공해주는 표준 윈도 라이브러리

window = Tk() # Tk()는 기본이 되는 윈도를 반환, 이를 루트 윈도 또는 베이스 윈도라고 함.
# 3행을 실행하면 윈도창 화면에 출력 ( 베이스 윈도를 window 변수에 넣음)

## 이 부분에서 화면을 구성하고 처리 ##

window.mainloop() # window.mainloop() 함수 실행

'''
tkinter는 TK Interface의 약어. Tk는 Tcl/Tk 라는 전통적인 GUI인터페이스 윈도, 리눅스, 맥 등에서 
모두 동일한 코드로 사용 가능
'''

#Code 10-02 py (윈도창 조절)
from tkinter import *

window = Tk()
window.title("윈도창 연습") # 윈도창에 제목 표시
window.geometry("400x100") # 윈도창의 초기 크기를 400 X 100으로 지정
window.resizable(width = FALSE, height = FALSE ) # 가로와 세로의 크기가 변경되지 않도록 지정

window.mainloop()


#Code10-03.py (레이블(Label): 문자를 표현할 수 있는 위젯)
from tkinter import *

# 최상위 창 생성
window = Tk()

# Label 위젯 생성
label1 = Label(window, text="COOKBOOK~~ Python을")  # 첫 번째 레이블
label2 = Label(window, text="열심히", font=("궁서체", 30), fg="blue")  # 두 번째 레이블
label3 = Label(window, text="공부합시다!", bg="yellow", width=20, height=2, anchor=SE)  # 세 번째 레이블

# 레이블 화면에 표시 pack()함수로 해당 레이블을 화면에 표시
label1.pack()
label2.pack()
label3.pack()

# Tkinter 이벤트 루프 실행
window.mainloop()
'''
Font : 글꼴과 크기 지정
Fg : 'foreground'의 약어, 글자색 지정
Bg : 'background'의 약어, 배경색 지정
width와 height : 위젯의 폭과 높이 지정
Anchor : 위젯이 어느 위치에 자리 잡을지 결정
'''

#-----------------------------------------------------------------------------
#Code10-04.py (레이블에 글자 대신 이미지 넣기)
from tkinter import *
window = Tk()

photo = PhotoImage(file = "gif/dog.gif") #PhotoImage()에서 이미지 파일을 준비
label1 = Label(window, image = photo) # Label()의 옵션 image에서 속성 지정

label1.pack()

window.mainloop()

#----------------------------------------------------------------
# 레이블 SELF STUDY (Code 10-04.py를 수정해서 이미지를 2개 출력해보자.)
# 힌트 : 위젯을 가로로 나타내려면 pack(side = LEFT)를 사용한다.
from tkinter import *
window = Tk()

photo1 = PhotoImage(file="GIF/dog.gif")
photo2 = PhotoImage(file="GIF/cat.gif")
label1= Label(master = window, image=photo1)
label2= Label(master = window, image=photo2)

label1.pack(side=LEFT)
label2.pack(side=LEFT)

window.mainloop()

#----------------------------------------------------------------
'''
버튼(Button) : 마우스로 클릭하면 눌리는 효과와 함께 지정한 작업 실행
예 : 버튼을 누르면 파이썬 IDLE이 종료되는 코드
'''
#Code10-05.py
from tkinter import *
window = Tk()

button1 = Button(window, text = "파이썬 종료", fg = "red", command = quit)
# 90행 : command 옵션에 quit 명령
button1.pack()

window.mainloop()

#------------------------------------------------------------------
'''
예 : 이미지 버튼을 누르면 간단한 메시지창이 나오는 코드
'''
#Code10-06.py
from tkinter import *
from tkinter import messagebox # messagebox 모듈 사용 임포트

## 함수 선언 부분 ##
def myFunc() : # myFunc()함수 정의
    messagebox.showinfo("강아지 버튼", "강아지가 귀엽죠?^^")
    # 이 함수는 messagebox.showinfo(제목, 내용) 형식으로 화면에 메시지 상자 출력
## 메인 코드 부분 ##
window = Tk()

photo = PhotoImage(file = "gif/dog2.gif") # 이미지 준비하고 버튼에 글자 대신 이미지 표현
button1 = Button(window, image = photo, command = myFunc)

button1.pack()

window.mainloop()

#-----------------------------------------------------------------
'''
체크 버튼(Checkbutton) : 켜고 끄는 데 사용하는 위젯
예 : 체크버튼을 켜거나 끄면 메시지창이 열리게 하는 코드
'''
# Code10-07.py (체크버튼)
from tkinter import *
from tkinter import messagebox
window = Tk()

## 함수 선언 부분 ##
def myFunc() : # myFunc() 함수는 chk.get()함수, 체크버튼에 설정된 값을 가져와서 메시지 출력
    if chk.get() == 0 :
        messagebox.showinfo("", "체크버튼이 꺼졌어요.")
    else :
        messagebox.showinfo("", "체크버튼이 켜졌어요.")
        
## 메인 코드 부분 ##
chk = IntVar() # chk 변수를 준비, intVar()함수 사용
cb1 = Checkbutton(window, text = "클릭하세요", variable = chk, command = myFunc)
# 137행 : Checkbutton()의 옵션 중 variable에 chk변수 사용
cb1.pack()

window.mainloop()

#---------------------------------------------------------------------
'''
라디오버튼(Radiobutton) : 여러 개 중에서 하나를 선택하는 데 사용하는 위젯
'''
#Code10-08.py
from tkinter import *
window = Tk()

## 함수 선언 부분 ##
def myFunc() : # myFunc()함수는 var 변수값으로 맨 아래 쪽 레이블의 텍스트를 변경
    if var.get() == 1 :
        label1.configure(text = "파이썬")
    elif var.get() == 2 :
        label1.configure(text = "C++")
    else :
        label1.configure(text = "Java")
        
## 메인 코드 부분 ##
var = IntVar() # 정수형 변수 var 준비
rb1 = Radiobutton(window, text = "파이썬", variable = var, value = 1, command = myFunc)
rb2 = Radiobutton(window, text = "C++", variable = var, value = 2, command = myFunc)
rb3 = Radiobutton(window, text = "Java", variable = var, value = 3, command = myFunc)
#rb 1 ~ 3 라디오 버튼 3개 준비
label1 = Label(window, text = "선택한 언어 : ", fg = "red")

rb1.pack()
rb2.pack()
rb3.pack()
label1.pack()

window.mainloop()
# --------------------------------------------------------------------------
'''
수평 정렬
수평으로 정렬하는 방법 : pack()함수의 옵션 중 side = LEFT, RIGHT
'''
#Code10-09.py
from tkinter import *
window = Tk()

button1 = Button(window, text = "버튼1")
button2 = Button(window, text = "버튼2")
button3 = Button(window, text = "버튼3")

# side = LEFT옵션은 왼쪽부터 채우라는 의미
button1.pack( side = LEFT )
button2.pack( side = LEFT )
button3.pack( side = LEFT )

window.mainloop()

# Code10-10.py (리스트와 for문 활용)
from tkinter import *
window = Tk()

btnList = [None] * 3 # 비어 있는 리스트를 3개 준비

for i in range(0, 3) : # 3회 반복하면서 버튼 생성
    btnList[i] = Button(window, text = "버튼" + str(i + 1))
    
for btn in btnList : # 준비한 버튼 리스트를 화면에 출력
    btn.pack( side = RIGHT )
    
window.mainloop()

# -------------------------------------------------
'''
수직 정렬
pack() 함수의 옵션 중 수직으로 정렬하는 방법 : side=TOP, BOTTOM
1)Code10-10.py의 10행을 다음과 같이 변경하고 실행
btn.pack(side = TOP)
btn.pack(side = BOTTOM)
'''

'''
폭 조정
pack()함수의 옵션 중+에서 윈도창 폭에 맞추는 방법 : fill=X
1) Code10-10.py의 10행을 다음과 같이 변경하고 실행
btn.pack(side = TOP, fill = X)
'''

'''
위젯 사이의 여백 조절
pack()함수의 옵션 중에서 위젯 사이에 여백 주는 방법:
1.padx=픽셀값 또는 pady=픽셀값
1) Code10-10.py의 10행을 다음과 같이 변경하고 실행
btn.pack(side = TOP, fill = X, padx = 10, pady = 10)

2. ipadx=픽셀값 또는 ipady = 픽셀값
2) btn.pack(side = TOP, fill = X, ipadx = 10, ipady = 10)

3. 위젯 내부와 외부에 모두 여백
3) btn.pack(side = TOP, fill = X, ipadx = 10, ipady = 10,
padx = 10, pady = 10)
'''

'''
고정 위치에 배치
1. 위젯을 고정 위치에 배치하려면 pack()대신 place()함수 사용
2. 그림 9개를 2차원으로 배치하는 코드
'''
#Code10-11.py
from tkinter import *

## 전역 변수 선언 부분 ##
btnList = [None] * 9
fnameList = ["froyo.gif", "gingerbread.gif", "honeycomb.gif", "icecream.gif",
             "jellybean.gif", "kitkat.gif", "lollipop.gif", "marshmallow.gif", "nougat.gif"]
photoList = [None] * 9
i, k = 0, 0
xPos, yPos = 0, 0
num = 0

## 메인 코드 부분 ##
window = Tk()
window.geometry("210x210")

for i in range(0,9) :
    photoList[i] = PhotoImage(file = "gif/" + fnameList[i])
    btnList[i] = Button(window, image = photoList[i])
    
for i in range(0, 3) :
    for k in range(0, 3) :
        btnList[num].place(x = xPos, y = yPos)
        num += 1
        xPos += 70
    xPos = 0
    yPos += 70
    
window.mainloop()

# ----------------------------------------------
# 프로그램 1 코드 생략