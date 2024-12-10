# 윈도프로그래밍 1103

'''
메뉴와 대화상자
1) 메뉴바와 메뉴 항목을 생성하고, 이를 프로그램에 통합하는 방법을 설명할 수 있다.
2) 대화상자를 통해 사용자 입력을 처리하고, 프로그램의 동작을 제어할 수 있는 기능을 구현할 수 있다.


## 메뉴의 생성

# 메뉴의 구성 개념과 형식
메뉴자체 = Menu(부모윈도)
부모윈도.config(menu = 메뉴자체)

상위메뉴 = Menu(메뉴자체)
메뉴자체.add_cascade(label = "상위메뉴텍스트", menu = 상위메뉴)
상위메뉴.add_command(label = "하위메뉴1", command = 함수1)
상위메뉴.add_command(label = "하위메뉴2", command = 함수2)
'''

# [파일] 메뉴 아래에 [열기]와 [종료] 하위 메뉴가 있는 코드
#Code10-17.py
from tkinter import *

window = Tk()

mainMenu = Menu(window)
# 27행 : Menu(부모윈도)로 mainMenu 변수 생성
# 27행 : mainMenu : '메뉴 자체'를 나타내는 변수
window.config(menu = mainMenu)
# 30행 : 생성한 메뉴 자체를 윈도창의 메뉴로 지정
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = fileMenu)
# 32~33행 : 상위 메뉴인 [파일]생성, 메뉴 자체에 부착.
# 32~33행 : [파일]메뉴는 선택하고 끝나는 것이 아니라, 그 아래에 다른 메뉴가 확장
# 32~33행 : 되어야 하므로 add_cascade() 함수 사용
fileMenu.add_command(label = "열기")
# 37행 : [파일]메뉴의 하위에 [열기] 메뉴 준비
# 37행 : [열기]메뉴 : 선택할 때 어떤 작동을 해야하므로 add_command()함수 사용
fileMenu.add_separator() # 메뉴 사이에 구분선 넣음
fileMenu.add_command(label = "종료")
# 41행 : 메뉴 사이에 구분선 넣음
window.mainloop()

#====================================================================================

#메뉴를 선택하면 작동할 수 있도록 코드 추가
#Code10-18.py
from tkinter import *
from tkinter import messagebox

## 함수 선언 부분 ##
def func_open() : # [열기]메뉴 선택하면 간단한 메시지창 열림
    messagebox.showinfo("메뉴선택", "열기 메뉴를 선택함")
    
def func_exit() : # [종료]메뉴를 선택하면 프로그램이 종료
    window.quit()
    window.destroy()
    
## 메인 코드 부분 ##
window = Tk()

mainMenu = Menu(window)
window.config(menu = mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="파일", menu=fileMenu)
fileMenu.add_command(label="열기", command=func_open)
# 68행 : [열기]메뉴 선택하면 무언가 작동해야 하므로 add_command()함수 사용
# 68행 : 즉,[파일]메뉴 선택하면 하위 메뉴가 확장.[열기]메뉴를 선택하면 53행의
# 68행 : func_open()함수가 실행
fileMenu.add_separator()
fileMenu.add_command(label ="종료", command=func_exit)
# 73행 : 68행과 같은 방식으로 하위 메뉴를 생성한다.
window.mainloop()

#==========================================================================

## 대화상자의 생성과 사용

# tkinter.simpledialog 모듈을 임포트한 후 askinteger() 및 askstring()등을 사용
#Code10-19.py
from tkinter import *
from tkinter.simpledialog import *

## 함수 선언 부분 ##
window = Tk()
window.geometry("400x100")

label1 = Label(window, text = "입력된 값")
label1.pack()

value = askinteger("확대배수", "주사위 숫자(1~6)을 입력하세요", minvalue = 1, maxvalue=6)

label1.configure(text = str(value))
window.mainloop()

#============================================================================

## 그림 파일인 GIF 파일을 선택하는 코드

#Code10-20.py는 Code10-19.py의 2행과 11행만 변경
from tkinter import *
from tkinter.filedialog import *

## 함수 선언 부분 ##
window = Tk()
window.geometry("400x100")

label1 = Label(window, text = "선택된 파일 이름")
label1.pack()

filename = askopenfilename(parent = window, filetypes =(("GIF파일", "*.gif"),
                                                        ("모든 파일", "*.*")))

label1.configure(text = str(filename))

window.mainloop()

#================================================================================

## 그림 파일인 GIF 파일을 선택하는 코드

#Code10-20.py의 113~116행만 변경하고 실행

from tkinter import *
from tkinter.filedialog import *

## 함수 선언 부분 ##
window = Tk()
window.geometry("400x100")

label1 = Label(window, text = "선택된 파일 이름")
label1.pack()

saveFp = asksaveasfile(parent = window, mode = "w", defaultextension = ".jpg",
                       filetypes = (("JPG파일", "*.jpg;*.jpeg"), ("모든 파일", "*.*")))
label1.configure(text = saveFp)
saveFp.close()

window.mainloop()

#==================================================================================

## [프로그램2]의 완성

# 메뉴 처리와 파일 처리가 핵심
#Code10-22.py
from tkinter import*
from tkinter.filedialog import *

## 함수 선언 부분 ##
def func_open() :
    filename = askopenfilename(parent = window, filetypes = (("GIF 파일", "*.gif"),
                                                             ("모든 파일", "*.*")))
    photo = PhotoImage(file = filename)
    pLabel.configure(image = photo)
    pLabel.image = photo
    
def func_exit() :
    window.quit()
    window.destroy()
    
## 메인 코드 부분 ##
window = Tk()
window.geometry("400x400")
window.title("명화 감상하기")

photo = PhotoImage()
pLabel = Label(window, image = photo)
pLabel.pack(expand=1, anchor=CENTER)

mainMenu = Menu(window)
window.config(menu = mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = fileMenu)
fileMenu.add_command(label = "파일 열기", command = func_open)
fileMenu.add_separator()
fileMenu.add_command(label = "프로그램 종료", command = func_exit)

window.mainloop()