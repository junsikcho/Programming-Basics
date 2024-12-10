'''
키보드와 마우스 이벤트 처리

-마우스 이벤트 기본 처리

1) 마우스 이벤트가 처리 형식
def  이벤트처리함수(event) :
     # 이 부분에 마우스 이벤트가 발생할 때 작동할 내용 작성
     
위젯.bind("마우스이벤트", 이벤트처리함수)
'''

#==============================================================

# 마우스 왼쪽 버튼을 클릭했을 때 처리하는 방법
#Code10-13.py
from tkinter import *
from tkinter import messagebox

## 함수 선언 부분 ##
def clickLeft(event) : # 마우스 이벤트가 발생할 때 작동할 함수 정의
    messagebox.showinfo("마우스", "마우스 왼쪽 버튼이 클릭됨")
    
## 메인 코드 부분 ##
window = Tk()

window.bind("<Button-1>", clickLeft) 
#window.bind()함수에는 마우스 왼쪽 버튼 클릭할 때 발생하는 이벤트인 <Button-1>설정하고
# 19행의 clickLeft함수명을 지정.
window.mainloop()

#==============================================================

# 지정된 위젯을 클릭했을 때 다른 함수 호출
#Code10-14.py
from tkinter import *
from tkinter import messagebox

## 함수 선언 부분 ##
def clickImage(event) :
    messagebox.showinfo("마우스", "펭귄에서 마우스가 클릭됨")

## 메인 코드 부분 ##
window = Tk()
window.geometry("400x400")

photo = PhotoImage(file = "gif/penguin.gif") # 공백 넣으면 안됨
label1 = Label(window, image = photo)

label1.bind("<Button>", clickImage)

label1.pack(expand = 1, anchor = CENTER)
window.mainloop()

#==================================================================

## event 매개변수를 활용한 마우스 이벤트 처리

# 마우스를 클릭할 때마다 어떤 마우스가 클릭되었는지 보여 주고 클릭한 좌표 출력
#Code10-15.py
from tkinter import *

## 함수 선언 부분 ##
def clickMouse(event): # 이 함수 : 마우스 클릭할 때 실행될 이벤트함수 선언
    txt=""
    if event.num ==1 : # 66~69행 : event.num값은 마우스 왼쪽 버튼 클릭했을때 1값, 오른쪽버튼->2값
        txt += "마우스 왼쪽 버튼이 ("
    elif event.num ==3 :
        txt += "마우스 오른쪽 버튼이 ("
        
    txt += str(event.y) + "," + str(event.x) + ")에서 클릭됨" 
    # 71행 : event.x와 event.y는 클릭한 위치의 좌표를 가짐/
    label1.configure(text = txt)
    
## 메인 코드 부분 ##
window = Tk()
window.geometry("400x400")

label1 = Label(window, text = "이곳이 바뀜")
# 79행에서 화면에 표시한 레이블의 글자 변경
window.bind("<Button>", clickMouse)

label1.pack(expand = 1, anchor = CENTER)
window.mainloop()

#======================================================================

# 키보드 이벤트는 위젯에서 키보드가 눌리면 발생
#Code10-16.py
from tkinter import *
from tkinter import messagebox

## 함수 선언 부분 ##
def keyEvent(event) :
    messagebox.showinfo("키보드 이벤트", "눌린 키 : " + chr(event.keycode))
    
## 메인 코드 부분 ##
window = Tk()

window.bind("<Key>", keyEvent)

window.mainloop()

#======================================================================

#SELF STUDY (위 코드를 수정해서 Shift+화살표키를 누르면 화살표 키가 출력되도록 해보자)
from tkinter import *
from tkinter import messagebox

## 함수 선언 부분 ##
def keyEvent(event):
    # Shift 키와 화살표 키를 조합했을 때 처리
    if event.state & 0x0001:  # Shift 키가 눌려 있는 상태를 확인
        if event.keycode == 37:  # 왼쪽 화살표
            messagebox.showinfo("키보드 이벤트", "눌린 키 : Shift + 왼쪽 화살표")
        elif event.keycode == 38:  # 위쪽 화살표
            messagebox.showinfo("키보드 이벤트", "눌린 키 : Shift + 위쪽 화살표")
        elif event.keycode == 39:  # 오른쪽 화살표
            messagebox.showinfo("키보드 이벤트", "눌린 키 : Shift + 오른쪽 화살표")
        elif event.keycode == 40:  # 아래쪽 화살표
            messagebox.showinfo("키보드 이벤트", "눌린 키 : Shift + 아래쪽 화살표")

## 메인 코드 부분 ##
window = Tk()
window.geometry("400x200")

# 키보드 이벤트 바인딩
window.bind("<Key>", keyEvent)

window.mainloop()
