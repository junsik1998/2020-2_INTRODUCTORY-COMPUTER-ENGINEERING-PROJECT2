import os
from datetime import date

from login import *
from menu import *
from check import *
from diary import *
    
user = None
task = None
loadDiaryTask = None

os.system("clear")

while user==None:
    showMenu(startMenu)
    task = input("번호를 선택해주세요.")

    if task=='1':
        signUp()
    elif task=='2':
        user = login()
    elif task=='0':
        break
    else :
        print("존재하지 않는 메뉴를 선택했습니다. 다시 입력해주세요.")


while user!=None and task!="0":
    YYYYMMDD = None
    
    showMenu(mainMenu)
    task=input("메뉴를 선택해주세요")

    if task == '1':
        writeDiary(user)
    elif task == "2":
        YYYYMMDD = loadDiary(user)
        if YYYYMMDD != None:
            # 일지 불러오기 프롬프트
            showMenu(loadDairyMenu)
            loadDiaryTask = input()
            if loadDiaryTask =='1':
                editDiary(user, YYYYMMDD)
                pass
            elif loadDiaryTask == '2':
                delDiary(user,YYYYMMDD)
                pass
            elif loadDiaryTask == '0':
                continue
            else:
                print("존재하지 않는 메뉴를 선택했습니다. 다시 입력해주세요.")

    elif task == '3':
        pass
    elif task == '4':
        pass
    elif task == '0':
        break
    else:
        os.system('clear')
        print("잘못 선택했습니다. 다시 선택해주세요.")
        
print("프로그램을 종료합니다.")

# DD를 해서 4는 안되고 04만 된다고 해놓기0
