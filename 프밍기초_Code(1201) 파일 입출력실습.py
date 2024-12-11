
'''
텍스트 파일 입출력
'''

## 한 행씩 읽어 들이기

#Code11-01.py
inFp = None  #입력 파일 객체 초기화
inStr = "" # 읽어온 문자열 저장 변수

# 텍스트 파일 열기
inFp = open("C:/Python/CookPython/sample.txt", "r", encoding="utf-8")
# 파일 열기

# 첫 번째 줄 읽기
inStr = inFp.readline() # readline()함수는 inFp로 열린 파일에서 한 행 읽어 inStr에 저장
print(inStr, end = "") # 화면에 출력 
# 위같은 처리를 아래 두번 째, 세번째줄에서도 반복 총 3회 수행

# 두 번째 줄 읽기
inStr = inFp.readline() 
print(inStr, end = "")

# 세 번째 줄 읽기
inStr = inFp.readline()
print(inStr, end = "")

# 파일 닫기
inFp.close()
# 위 코드 중 행이 1~2개만 있으면 오류 발생, 4개 이상이 있어도 3개밖에 읽지 못함

#===========================================================================

# 텍스트 파일에 있는 모든 행을 다 읽기
# Code11-02.py
inFp = None # 입력 파일
inStr = "" # 읽어 온 문자열

inFp = open("C:/Python/CookPython/sample.txt", "r", encoding="utf-8")

while True : # 무한루프문 반복
    inStr=inFp.readline() 
    if inStr =="" :
        break;
    print(inStr, end = "")
'''
위 무한루프문 설명
파일에서 행을 1개 읽음. 
8행에서 읽어 온 것이 없다면 9행 break로 무한 반복에서 빠져나옴
그렇지 않으면 10행에서 읽어 온 내용 출력
'''
inFp.close()

#=============================================================================

# SELF STUDY
#Cody11-02.py를 수정해서 다음과 같이 앞에 각 행 번호를 출력해보자.

inFp = None # 입력 파일
inStr = "" # 읽어 온 문자열
lineNum = 1
inFp = open("C:/Python/CookPython/sample.txt", "r", encoding="utf-8")

while True : # 무한루프문 반복
    inStr=inFp.readline() 
    if inStr =="" :
        break;
    print("%d : %s" %(lineNum, inStr), end = "")
    lineNum += 1

inFp.close()

#===============================================================================

# 한 번에 모두 읽어 들이기
# 1) readlines()함수 : 파일의 내용을 통째로 읽어서 리스트에 저장
#Code11-03.py
inFp = None
inList = ""

inFp = open("C:/Python/CookPython/sample.txt", "r", encoding="utf-8")

inList = inFp.readlines() # 한 번에 읽어서 inList에 저장
print(inList)

inFp.close()
'''
(plus)
with ~ as 문
프로그램을 만들다 보면 close()함수를 호출하지 않고 프로그램을 종료해서 종종 문제가 발생.
아예 close()함수를 사용하지 않으려면 아래와 같이 with~as문으로 파일을 엶.
with open("C:/Python/CookPython/sample.txt", "r", encoding="utf-8") as inFp :
    inList = inFp.readlines()
    print(inList)
'''
#=================================================================================

# 한번에 모두 읽어 들이기
#Code11-03.py에서 파일의 내용을 한 행씩 출력.
#Code11-04.py
inFp = None
inList = []
inStr = ""

inFp = open("C:/Python/CookPython/sample.txt", "r", encoding="utf-8")

inList = inFp.readlines()
for inStr in inList :
    print(inStr, end = "")
    
inFp.close()

#==================================================================================

#SELF STUDY (Cody11-04.py를 수정해서 다음과 같이 앞에 각 행 번호를 출력해보자.)
inFp = None
inList = []
inStr = ""
lineNum = 1

inFp = open("C:/Python/CookPython/sample.txt", "r", encoding="utf-8")

inList = inFp.readlines()
for inStr in inList :
    print("%d : %s" %(lineNum, inStr), end = "")
    lineNum += 1
    
inFp.close()

#====================================================================================

# 도스 명령어 type의 구현
# 1) 지정한 파일의 내용을 화면에 출력 ->  type 파일명

# 출력 프로그램
#Code11-05.py
inFp = None
fName, inList, inStr = "", [], ""

fName = input("파일명을 입력하세요 : ") #C:/Windows/win.ini
inFp = open(fName, "r")

inList = inFp.readlines()
for inStr in inList :
    print(inStr, end = "")
    
inFp.close()

#=====================================================================================

# 파일이 없을 때 오류가 발생하지 않게 하려면 os.path.exists(파일명) 형식 사용
#Code11-06.py
import os # os 모듈 임포트

inFp = None
fName, inList, inStr = "", [], ""

fName = input("파일명을 입력하세요 : ")

if os.path.exists(fName) :
    inFp = open(fName, "r")
    
    inList = inFp.readlines()
    for inStr in inList :
        print(inStr, end = "")
        
    inFp.close()
else :
    print("%s 파일이 없습니다." % fName)

#============================================================================================

'''
파일을 이용한 출력
1) 출력 결과를 파일에 저장하는 방식(파일에 내용 쓸 때 write()나 writelines()함수 사용)
입력 관련 : input() , 파일 출력 관련 : write(), writelines()
'''

# 한 행씩 파일에 쓰기
# 1) 키보드에서 입력한 내용을 한 행씩 파일에 쓰는 코드(input()함수 반복 사용)
#Code11-07.py
outFp = None
outStr = ""

outFp = open("C:/Python/CookPython/data2.txt", "w", encoding="utf-8")

while True :
    outStr = input("내용 입력 :")
    if outStr != "" :
        outFp.writelines(outStr + "\n")
    else :
        break
    
outFp.close()
print("---정상적으로 파일에 씀---")

#==============================================================================================

# SELF STUDY(11-07.py를 수정해서 파일명도 입력받아 보자.)
outFp = None
outStr = ""
fName = ""

fName = input("파일명을 입력하세요 : ") #C:/Windows/win.ini
outFp = open(fName, "w")

while True :
    outStr = input("내용 입력 :")
    if outStr != "" :
        outFp.writelines(outStr + "\n")
    else :
        break
    
outFp.close()
print("---정상적으로 파일에 씀---")

#============================================================================================

'''
파일을 이용한 출력
2) 도스 copy 명령어의 구현
copy 소스파일 타깃파일
파일 -> 파일입력관련(read(),readline(),readlines()
파일 출력 관련(write(),writelines())
'''

#Code11-08.py
inFp, outFp = None, None
inStr = ""

inFp = open("C:/Windows/win.ini", "r")
outFp = open("C:/Python/CookPython/data2.txt", "w", encoding="utf-8")
# 232 ~ 233 행 : 읽기 모드 및 쓰기 모드로 파일 열기
inList = inFp.readlines() # 파일의 내용 통째로 읽기
for inStr in inList : # 내용을 쓰기 파일에 쓰기
    outFp.writelines(inStr)
    
inFp.close()
outFp.close()
print("---파일이 정상적으로 복사되었음----")

#=====================================================================================================

# 암호화(ord()와 chr()함수 사용)
ord('파')
chr(54028)

# '파'를 암호화하려고 54028('파')+100 =54123('')으로 저장
num = ord('퍰')
chr(num - 100)

#========================================================================================================

'''
이진 파일 입출력
1) 이진 파일의 복사
'''

# 1) Code11-08.py를 수정해서 이진 파일 복사
#Code11-10.py
inFp, outPf = None, None
inStr = ""

inFp = open("C:/Windows/notepad.exe", "rb")
outFp = open("C:/Temp/notepad.exe", "wb")

while True :
    inStr = inFp.read(1)
    if not inStr :
        break
    outFp.write(inStr)
    
inFp.close()
outFp.close()
print("--- 이진 파일이 정상적으로 복사되었음---")

#=======================================================================================

## [프로그램 2]의 완성

# 윈도창의 작성
# 1) 기본적인 윈도창 표시하는 간단한 코드
#Code11-11.py
from tkinter import *

## 변수 선언 부분 ##
window = None

canvas = None
XSIZE, YSIZE = 256, 256

## 메인 코드 부분 ##
window = Tk()
canvas = Canvas(window, height = XSIZE, width = YSIZE)

canvas.pack()
window.mainloop()

#==========================================================================================

## [프로그램 2]의 완성
# RAW 이미지 출력
from tkinter import *

## 변수 선언 부분 ##
window = None

canvas = None
XSIZE, YSIZE = 256, 256

## 메인 코드 부분 ##
window = Tk()
canvas = Canvas(window, height = XSIZE, width = YSIZE)
paper = PhotoImage(width=XSIZE, height=YSIZE)
canvas.create_image((XSIZE/2, YSIZE/2), image = paper, state = "normal")
canvas.pack()
window.mainloop() 

#==================================================================

## [프로그램2]의 완성
# RAW사진 파일의 화면 출력
# 1) 디스크에 저장된 RAW파일을 메모리(inImage)로 불러옴
for i in range(0, XSIZE) :
    tmpList = [] # tmpList를 비움
    for k in range(0, YSIZE) : # 327~329행 : 1바이트씩 256번 읽어 tmpList에 저장
        data = int(ord(fp.read(1)))
        tmpList.append(data)
    inImage.append(tmpList) # inImage에 256크기의 1차 리스트를 inImage에 저장
    
#=============================================================================

## [프로그램2]의 완성
# RAW 사진 파일의 화면 출력
# 2) 메모리(inImage)를 윈도창에 출력하는 기능은 displayImage()함수에 구현
rgbString = ""
for i in range(0, XSIZE) :
    tmpString = ""
    for k in range(0, YSIZE) :
        data = image[i][k]
        tmpString += "#%02x%02x%02x " % (data, data, data) # x 뒤에 한 칸 공백
    rgbString += "{" + tmpString + "} " # } 뒤에 한 칸 공백
paper.put(rgbString)


#==================================================================================
