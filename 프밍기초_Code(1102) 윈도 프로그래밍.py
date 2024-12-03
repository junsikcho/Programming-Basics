'''
11장 02 윈도 프로그래밍
-키보드와 마우스 이벤트 처리
1) 키보드 입력과 마우스 클릭 이벤트의 동작 원리를 이해하고,
이를 처리하는 프로그램 코드를 작성할 수 있다.
2) 키보드와 마우스 이벤트 핸들러를 구현하여 특정 입력 동작에 따라
프로그램이 반응하도록 설계할 수 있다. 
'''

'''
# 마우스 이벤트 기본 처리 ( 마우스 이벤트가 처리 형식 )
def 이벤트처리함수(event) :
    # 이부분에 마우스 이벤트가 발생할 때 작동할 내용 작성
    
위젯.bind("마우스이벤트", 이벤트처리함수)
'''

# 마우스 왼쪽 버튼을 클릭했ㅇ르 때 처리하는 방법
#Code10-13.py
from tkinter import *
from tkinter import messagebox

## 함수 선언 부분 ##
def clickLeft(event) :
    messagebox.showinfo("마우스", "마우스 왼쪽 버튼이 클릭됨")
    
## 메인 코드 부분 ##
window = Tk()

window.bind("<Button-1>", clickLeft)

window.mainloop()

#------------------------------------------------------------

# 지정된 위젯을 클릭했을 때 다른 함수 호출
#Code10-14.py
from tkinter import *
from tkinter import messagebox

## 함수 선언 부분 ##
def clickImage(event) :
    messagebox.showinfo("마우스", "토끼에서 마우스가 클릭됨")

## 메인 코드 부분 ##
window = Tk()
window.geometry("400 x 400")

photo = PhotoImage(file = "gif/rabbit.gif")
label1 = Label(window, image = photo)

label1.bind("<Button>", clickImage)

label1.pack(expand = 1, anchor = CENTER)
window.mainloop()

#-----------------------------------------------------------

# event 매개변수를 활용한 마우스 이벤트 처리
# 마우스를 클릭할 때마다 어떤 마우스가 클릭되었는지 보여주고
# 클릭한 좌표 출력
#Code10-15.py
from tkinter import *

## 함수 선언 부분 ##
def clickMouse( event ) : # ~76행 : 마우스 클릭할때 실행될 이벤트 함수 선언
    txt = ""
    if event.num == 1 :
        txt += "마우스 왼쪽 버튼이 ("
    elif event.num == 3 :
        txt += "마우스 오른쪽 버튼이 ("
    # 68 ~71행 : event.num값은 마우스 왼쪽 버튼 클릭했을때 1값,
    # 마우스 오른쪽 버튼 클릭했을 때 2값을 가짐
        
    txt += str( event.y ) + "," + str( event.x ) + ")에서 클릭됨"
    label1.configure(text = txt)
    
## 메인 코드 부분 ##
window = Tk()
window.geometry("400 x 400 ")

label1 = Label(window, text = "이곳이 바뀜")

window.bind("<Button>", clickMouse) # 마우스 클릭하면 함수 호출

label1.pack(expand = 1, anchor = CENTER)
window.mainloop()

#------------------------------------------------------------

# 키보드 이벤트는 위젯에서 키보드가 눌리면 발생
#Code.10-16.py
from tkinter import *
from tkinter import messagebox

## 함수 선언 부분 ##
def keyEvent(event) :
    messagebox.showinfo("키보드 이벤트", "눌린 키 : " + chr( event.keycode))
    
## 메인 코드 부분 ##
window = Tk()

window.bind("<Key>" , keyEvent)

window.mainloop()