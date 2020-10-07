from menu import *
import os
from diary import loadDiaryList
import re
from check import * 

def editDiary(user, YYYYMMDD):
    diaryFile = "./Users/"+user+"/diary/"+YYYYMMDD+".txt"
    foodList = loadDiaryList(user, YYYYMMDD)
    select = None
    change = None

    print("수정할 음식을 선택해주세요.")

    for i in range(len(foodList)):
        print(i, foodList[i])

    while True:
        select = input( "입력 > ")
        res = justNumber(select) # 숫자 이외의 것들이 있는지 확인
        if res == True:
            if int(select)>=0 and int(select)<len(foodList):
                change = input()
                if len(change)==0:
                    del foodList[int(select)]
                    break
                else:
                    print(int(select), change)
                    foodList[int(select)] = change
                    break
            else:
                print("존재하지 않는 인덱스를 선택했습니다. 다시 입력해주세요.")
        else:
            print("숫자 외에 문자를 입력할 수 없습니다. 다시 입력해주세요.")
    f = open(diaryFile, 'w')
    for i in foodList:
        f.write(i+'\n')
    f.close()            

def delDiary(user, YYYYMMDD):
    diaryFile = "./Users/"+user+"/diary/"+YYYYMMDD+".txt"
    os.remove(diaryFile)

def loadDiaryPrompt(user, YYYYMMDD):
    loadDiaryTask = showMenu("일지 불러오기 메뉴")
    if loadDiaryTask == 1:
        editDiary(user, YYYYMMDD)
    elif loadDiaryTask == 2:
        delDiary(user,YYYYMMDD)
    elif loadDiaryTask == 0:
        return