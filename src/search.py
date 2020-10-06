import re

from input import inputNumber, inputUser
from menu import showMenu

foods = []
food_name_index = 1

products = []
product_name_index = 0
product_barcode_index = 1

def searchFood(input_text):
    if input_text.find('?') < 0 and input_text.find('*') < 0:
        for food in foods:
            if food[food_name_index] == input_text:
                return food[food_name_index]
        food_list = []
        for food in foods:
            if food[food_name_index] in input_text or input_text in food[food_name_index]:
                food_list.append(food[food_name_index])
        if food_list:
            print("[유사 식품명 중 선택]")
            print("0. 선택 안함")
            index = 1
            for food in food_list:
                print(str(index) + ". " + food)
                index += 1
            select = inputNumber(0, len(food_list))
            if select == 0:
                return "-1"
            else:
                return food_list[select - 1]
        else:
            print("검색된 식품명이 없습니다.")
            return "-1"
    else:
        food_list = []
        pattern = input_text.replace('?', '.')
        pattern = pattern.replace('*', '.*')
        for food in foods:
            if re.fullmatch(pattern, food[food_name_index]):
                food_list.append(food[food_name_index])
        if food_list:
            print("[유사 식품명 중 선택]")
            print("0. 선택 안함")
            index = 1
            for food in food_list:
                print(str(index) + ". " + food)
                index += 1
            select = inputNumber(0, len(food_list))
            if select == 0:
                return "-1"
            else:
                return food_list[select - 1]
        else:
            print("검색된 식품명이 없습니다.")
            return "-1"


def searchProductName(input_text):
    product_list = []
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


def showBadProducts(product_list=[]):
    if product_list:
        print("[검색된 유해식품]")
        for product in product_list:
            print(product[product_name_index] + "  " + product[product_barcode_index])
    else:
        print("검색된 유해식품이 없습니다.")


def badProductSearch():
    menu = showMenu("유해식품 검색 메뉴")
    if menu == 0:
        return
    if menu == 1:
        showBadProducts(searchProductName(inputUser("product")))
    if menu == 2:
        showBadProducts(searchBarcode(inputUser("barcode")))


def foodInfo(foodname):
    for food in foods:
        if food[food_name_index] == foodname:
            return food


def searchInit(main_foods, main_products):
    global foods, products
    foods = main_foods
    products = main_products