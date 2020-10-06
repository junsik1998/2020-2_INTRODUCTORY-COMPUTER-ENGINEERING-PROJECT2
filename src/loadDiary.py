from menu import *
from diary import *

def loadDiaryPrompt(user, YYYYMMDD):
    loadDiaryTask = showMenu("일지 불러오기 메뉴")
    if loadDiaryTask == 1:
        editDiary(user, YYYYMMDD)
    elif loadDiaryTask == 2:
        delDiary(user,YYYYMMDD)
    elif loadDiaryTask == 0:
        return