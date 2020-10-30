from diary import *
from input import *
from loadDiary import loadDiaryPrompt
from login import *
from nutrient_analysis import *
from menu import *
from search import badProductSearch, searchInit
from food_info import *
from badfood_info import *

user = None
task = None
loadDiaryTask = None


foods = []
food_name_index = 1

products = []
product_name_index = 0
product_barcode_index = 1


def loadFood():
    food_file = open("./식품영양정보.txt", "r", encoding="utf-8")
    lines = food_file.readlines()
    lines = lines[1:]
    for line in lines:
        temp = line.split(',')
        temp[-1] = temp[-1].replace("\n", "")
        foods.append(temp)


def loadBadProducts():
    bad_file = open("./유해식품정보.txt", "r", encoding="utf-8")
    lines = bad_file.readlines()
    lines = lines[1:]
    for line in lines:
        temp = line.split(',')
        temp[-1] = temp[-1].replace("\n", "")
        products.append(temp)


if __name__ == "__main__":
    check_network = mk_food()
    if check_network == 1:
        mk_badfood()
        loadFood()
        loadBadProducts()
        searchInit(foods, products)

        while user==None:
            task = MenuSelect("시작 메뉴")
            if task == "1":
                signUp()
            elif task == "2":
                user = login()
            elif task == "0":
                break
            else:
                print("존재하지 않는 메뉴를 선택했습니다. 다시 입력해주세요.")

        while user!=None:
            menu = MenuSelect("메인 메뉴")
            if menu == "0":
                print("프로그램을 종료합니다.")
                break
            elif menu == "1":
                writeDiary(user)
            elif menu == "2":
                YYYYMMDD = loadDiary(user)
                if YYYYMMDD is not None:
                    # 일지 불러오기 프롬프트
                    loadDiaryPrompt(user, YYYYMMDD)
            elif menu == "3":
                diary_analysis(user)
            elif menu == "4":
                badProductSearch()
            else:
                print("잘못 입력하셨습니다.")
    else:
        pass
