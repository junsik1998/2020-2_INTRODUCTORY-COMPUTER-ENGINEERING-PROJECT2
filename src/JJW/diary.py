import os
from datetime import date
from check import *

def showDiaryList(user, YYYYMM):
    directory ="./Users/"+user+"/diary/"

    for i in os.listdir(directory):
        if i.startswith(YYYYMM):
            print(i)

def showDiary(user, YYYYMMDD):
    diaryFile = "./Users/"+user+"/diary/"+YYYYMMDD+".txt"
    f = open(diaryFile, 'r')
    lines = f.readlines()
    for line in lines:
        print(line.replace('\n',''))
    f.close()

def writeDiary(user):
    today = date.today().strftime('%Y%m%d')
    diaryDir ="./Users/"+user+"/diary/"
    foodDir ="./Users/"+user+"/food/"
    diaryFile = diaryDir+str(today)+".txt"
    foodFile = foodDir+str(today)+".txt"

    # 식품명 입력
    if existFile(foodFile) == True:
        f = open(foodFile, "a")
    else:
        f = open(foodFile, "w")

    print("오늘 섭취한 식품들을 하나씩 Enter키로 구분하여 입력해주세요. 입력을 완료했으면 빈 문자열인 상태로 한번 더 Enter키를 누르세요.")
    while True: 
        diary = input()
        if diary == '':
            break
        else:
            # 여기서 준식이 함수 거침
            f.write(diary+"\n")
    f.close()
    print("식품명 입력이 완료되었습니다.")

    # 제품명 입력
    if existFile(diaryFile) == True:
        f = open(diaryFile, "a")
    else:
        f = open(diaryFile, "w")

    print("오늘 섭취한 제품명들을 하나씩 Enter키로 구분하여 입력해주세요. 입력을 완료했으면 빈 문자열인 상태로 한번 더 Enter키를 누르세요.")
    while True: 
        food = input()
        if food == '':
            break
        else:
            # 중복되는지 확인
            f.write(food+"\n")
    f.close()
    print("제품명 입력이 완료되었습니다.")

def loadDiary(user):
    directory ="./Users/"+user+"/diary/"

    # 년도 월 입력받기
    while True:
        YYYYMM = input("불러오실 일지의 년도와 월을 입력해주세요.")
        if YYYYMM == '0':
            return 
        else:
            if checkYYYYMM(YYYYMM):
                break

    # 날짜 입력받기
    # 기획서 수정 : 0입력하면 메인으로
    while True:
        showDiaryList(user, YYYYMM)
        DD = input("불러오실 일지의 날짜를 입력해주세요.")
        if DD == '0':
            return
        else:
            if checkDD(YYYYMM, DD):
                if existFile(directory+YYYYMM+DD+".txt"):
                    showDiary(user, YYYYMM+DD)
                    return YYYYMM+DD
                else:
                    print("해당 날짜에 일지를 적지 않으셨습니다.")
                    continue

def loadDiaryList(user, YYYYMMDD):
    diaryFile = "./Users/"+user+"/diary/"+YYYYMMDD+".txt"
    foodList = list()
    f = open(diaryFile, 'r')
    lines = f.readlines()
    f.close()
    for line in lines:
        foodList.append(line.replace('\n', ''))
    return foodList

def editDiary(user, YYYYMMDD):
    diaryFile = "./Users/"+user+"/diary/"+YYYYMMDD+".txt"
    foodList = loadDiaryList(user, YYYYMMDD)
    select = None
    change = None

    print("수정할 음식을 선택해주세요.")

    for i in range(len(foodList)):
        print(i, foodList[i])

    while True:
        select = input()
        res = re.search('[0-9]', select)
        if res != None:
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
            print("숫자외에 문자를 입력할 수 없습니다. 다시 입력해주세요.") # 추가
    f = open(diaryFile, 'w')
    for i in foodList:
        f.write(i+'\n')
    f.close()            


    # filename = directory+str(date)+".txt"
    # if existFile(filename) == True:
    #     f = open(filename, "r")
    #     test = f.readline()
    #     print(test.split(','))
    #     print(type(test))
    #     f.close()
    # else:
    #     print("해당 날짜의 일기가 존재하지 않습니다.")

def delDiary(user, YYYYMMDD):
    diaryFile = "./Users/"+user+"/diary/"+YYYYMMDD+".txt"
    os.remove(diaryFile)