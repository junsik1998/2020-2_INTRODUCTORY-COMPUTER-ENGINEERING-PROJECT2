import os
from datetime import date
from check import *
from input import inputFoodName, inputProduct
from search import searchFood


def showDiaryList(user, YYYYMM):
    directory ="./Users/"+user+"/diary/"

    for i in os.listdir(directory):
        if i.startswith(YYYYMM):
            print(i.replace('.txt',''))

def showDiary(user, YYYYMMDD):
    diaryFile = "./Users/"+user+"/diary/"+YYYYMMDD+".txt"
    f = open(diaryFile, 'r', encoding='utf-8')
    lines = f.readlines()
    for line in lines:
        print(line.replace('\n',''))
    f.close()

def writeDiary(user):
    today = date.today().strftime('%Y%m%d')
    diaryDir ="./Users/"+user+"/diary/"
    productDir ="./Users/"+user+"/product/"
    diaryFile = diaryDir+str(today)+".txt"
    productFile = productDir+str(today)+".txt"

    # 식품명 입력
    if existFile(diaryFile) == True:
        f = open(diaryFile, "a", encoding='utf-8')
    else:
        f = open(diaryFile, "w", encoding='utf-8')

    print("오늘 섭취한 식품들을 하나씩 Enter키로 구분하여 입력해주세요. 입력을 완료했으면 빈 문자열인 상태로 한번 더 Enter키를 누르세요.")
    while True: 
        diary = inputFoodName()
        if diary == '':
            break
        else:
            diary = searchFood(diary)
            if diary != "-1":
                f.write(diary+"\n")
    f.close()
    print("식품명 입력이 완료되었습니다.")

    # 제품명 입력
    if existFile(productFile) == True:
        productList = loadProductList(user, today)
        f = open(productFile, "a", encoding='utf-8')
    else:
        f = open(productFile, "w", encoding='utf-8')

    print("오늘 섭취한 제품명들을 하나씩 Enter키로 구분하여 입력해주세요. 입력을 완료했으면 빈 문자열인 상태로 한번 더 Enter키를 누르세요.")
    while True:
        # 제품명 문법 규칙 검사하여 입력
        product = inputProduct()
        if product == '':
            break
        else:
            if product in productList:
                print("제품명은 동일 일에 중복으로 입력할 수 없습니다.")
            else:
                productList.append(product)
                f.write(product+"\n")
    f.close()
    print("제품명 입력이 완료되었습니다.")

def loadDiary(user):
    directory ="./Users/"+user+"/diary/"

    # 년도 월 입력받기
    while True:
        YYYYMM = input("불러오실 일지의 년도와 월을 입력해주세요.\n입력 > ")
        if YYYYMM == '0':
            return 
        else:
            if checkYYYYMM(YYYYMM):
                break

    # 날짜 입력받기
    while True:
        showDiaryList(user, YYYYMM)
        DD = input("불러오실 일지의 일을 입력해주세요.\n입력 > ")
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
    f = open(diaryFile, 'r', encoding='utf-8')
    lines = f.readlines()
    f.close()
    for line in lines:
        foodList.append(line.replace('\n', ''))
    return foodList

def loadProductList(user, YYYYMMDD):
    productFile = "./Users/"+user+"/product/"+YYYYMMDD+".txt"
    productList = list()
    f = open(productFile, 'r', encoding='utf-8')
    lines = f.readlines()
    f.close()
    for line in lines:
        productList.append(line.replace('\n', ''))
    return productList