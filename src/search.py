import re

from input import inputNumber, inputUser
from menu import showMenu

foods = []
food_name_index = 1

products = []
product_name_index = 0
product_reason_index = 1
product_company_index = 2
product_tel_index = 4
product_barcode_index = 5


def searchFood(input_text):
    if input_text.find('?') < 0 and input_text.find('*') < 0:
        for food in foods:
            if food[food_name_index] == input_text:
                return food[food_name_index]
        food_list = []
        for food in foods:
            if food[food_name_index] in input_text or input_text in food[food_name_index]:
                food_list.append(food[food_name_index])
        # if =food_list:
        print("다음 항목 중에서 원하는 항목을 선택하세요.")
        print("0. 선택 안함")
        index = 1
        for food in food_list:
            print(str(index) + ". " + food)
            index += 1
        select = inputNumber(0, len(food_list))
        if select == 0:
            print("선택 안함")
            return "-1"
        else:
            print(food_list[select - 1])
            return food_list[select - 1]
        '''
        else:
            print("검색된 식품명이 없습니다.")
            return "-1"
        '''
    else:
        food_list = []
        pattern = input_text.replace('?', '.')
        pattern = pattern.replace('*', '.*')
        for food in foods:
            if re.fullmatch(pattern, food[food_name_index]):
                food_list.append(food[food_name_index])
        # if =food_list:
        print("다음 항목 중에서 원하는 항목을 선택하세요.")
        print("0. 선택 안함")
        index = 1
        for food in food_list:
            print(str(index) + ". " + food)
            index += 1
        select = inputNumber(0, len(food_list))
        if select == 0:
            print("선택 안함")
            return "-1"
        else:
            print(food_list[select - 1])
            return food_list[select - 1]
        '''
        else:
            print("검색된 식품명이 없습니다.")
            return "-1"
        '''


def searchProductName(input_text):
    product_list = []
    while input_text == '':
        print("입력하신 값이 문법 형식에 맞지 않습니다.")
        input_text = inputUser("product")
    if input_text.find('?') < 0 and input_text.find('*') < 0:
        for product in products:
            if product[product_name_index] == input_text:
                product_list.append(product)
        if product_list:
            return product_list
        else:
            for product in products:
                if input_text in product[product_name_index]:
                    product_list.append(product)
            return product_list
    else:
        pattern = input_text.replace('?', '.')
        pattern = pattern.replace('*', '.*')
        for product in products:
            if re.fullmatch(pattern, product[food_name_index]):
                product_list.append(product)
        return product_list


def searchBarcode(input_text):
    product_list = []
    for product in products:
        if product[product_barcode_index] == input_text:
            product_list.append(product)
            return product_list


def showBadProducts(product_list=[], type=""):
    if product_list:
        # print("[검색된 유해식품]")
        for product in product_list:
            print("제품명 : " + product[product_name_index])
            print("사유 : " + product[product_reason_index])
            if product[product_company_index]: print("업체명 : " + product[product_company_index])
            if product[product_tel_index]: print("전화번호 : " + product[product_tel_index])
            if product[product_barcode_index]: print("바코드 번호 : " + product[product_barcode_index])
            print("")
    else:
        if type == "product": print("입력하신 제품명에 대한 검색 결과가 없습니다.")
        if type == "barcode": print("입력하신 바코드 번호는 유해식품정보에 등록되어 있지 않은 바코드 번호입니다.")


def badProductSearch():
    menu = showMenu("유해식품 검색 메뉴")
    if menu == 0:
        return
    if menu == 1:
        print("제품명을 입력해주세요.")
        showBadProducts(searchProductName(inputUser("product")), "product")
    if menu == 2:
        print("바코드 번호를 입력하세요.")
        showBadProducts(searchBarcode(inputUser("barcode")), "barcode")


def foodInfo(foodname):
    for food in foods:
        if food[food_name_index] == foodname:
            return food


def searchInit(main_foods, main_products):
    global foods, products
    foods = main_foods
    products = main_products
