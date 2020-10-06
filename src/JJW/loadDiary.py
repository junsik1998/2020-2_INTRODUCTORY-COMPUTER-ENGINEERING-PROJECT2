from menu import *
from diary import *

def loadDiaryPrompt(user, YYYYMMDD):
    loadDiaryTask = showMenu("일지 불러오기 메뉴")
    if loadDiaryTask =='1':
        editDiary(user, YYYYMMDD)
    elif loadDiaryTask == '2':
        delDiary(user,YYYYMMDD)
    elif loadDiaryTask == '0':
        return
    else:
        print("존재하지 않는 메뉴를 선택했습니다. 다시 입력해주세요.")