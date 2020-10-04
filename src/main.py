import re

main_menu_list = ["프로그램 종료", "일지 작성", "일지 불러오기", "일지 분석", "유해식품 검색"]
search_menu_list = ["메인 메뉴로 이동", "제품명으로 검색", "바코드 번호로 검색"]

foods = [
    [1, "열무김치", 110],
    [2, "배추김치", 220],
    [3, "파김치", 330],
    [4, "고등어구이", 440],
    [5, "갈치구이", 550]
]
food_name_index = 1

products = [
    ["가나다라", "12321"],
    ["마바사아", "45654"],
    ["가나AB", "78987"],
    ["ABCD", "01010"]
]
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


def foodInfo(foodname):
    for food in foods:
        if food[food_name_index] == foodname:
            return food


def inputFoodName():
    while True:
        input_text = input('입력 > ')
        return_text = ''
        find_text = re.findall(r'[가-힣\?\*]+', input_text)
        korean = re.findall(r'[가-힣]+', input_text)
        two_star = re.findall(r'\*{2,}', input_text)
        for temp in find_text:
            return_text += temp
        if input_text == return_text and len(return_text) <= 20 and korean and not two_star:
            return return_text
        elif input_text != return_text:
            print("입력 가능한 문자는 완전한 한글, 와일드카드 문자(?, *) 입니다.")
        else:
            if len(return_text) > 20:
                print("20글자 이하로 입력해주세요.")
            if not korean:
                print("완전한 한글 문자가 최소 1글자 이상 포함되어야 합니다.")
            if two_star:
                print("* 기호는 2개 이상 연속하여 입력할 수 없습니다.")


def inputProduct():
    while True:
        input_text = input('입력 > ')
        return_text = ''
        find_text = re.findall(r'[가-힣a-zA-Z\s\?\*]+', input_text)
        korean_english = re.findall(r'[가-힣a-zA-Z]+', input_text)
        two_star = re.findall(r'\*{2,}', input_text)
        for temp in find_text:
            return_text += temp
        if input_text == return_text and len(return_text) <= 20 and korean_english and not two_star:
            return return_text
        elif input_text != return_text:
            print("입력 가능한 문자는 완전한 한글, 영문자, 와일드카드 문자(?, *) 입니다.")
        else:
            if len(return_text) > 20:
                print("20글자 이하로 입력해주세요.")
            if not korean_english:
                print("완전한 한글 문자 또는 영문자가 최소 1글자 이상 포함되어야 합니다.")
            if two_star:
                print("* 기호는 2개 이상 연속하여 입력할 수 없습니다.")


def inputBarcode():
    while True:
        input_text = input('입력 > ')
        barcode_text = ''
        return_text = ''
        find_text = re.findall(r'[0-9\s\-]+', input_text)
        number = re.findall(r'[0-9]+', input_text)
        for temp in find_text:
            barcode_text += temp
        for temp in number:
            return_text += temp
        if input_text == barcode_text and 5 <= len(return_text) <= 30:
            return return_text
        elif len(return_text) < 5 or len(return_text) > 30:
            print("숫자를 5개 이상 30개 이하로 입력해주세요.")
        else:
            print("입력 가능한 문자는 숫자, 공백, - 기호 입니다.")


def inputNumber(start, end):
    while True:
        try:
            number = int(input('입력 > '))
            if start <= number <= end:
                return number
            else:
                print(str(start) + "이상 " + str(end) + "이하의 숫자로 입력해 주세요.")
        except ValueError:
            print("숫자만 입력 가능합니다.")


def inputUser(type=''):
    if type == 'foodname':
        return inputFoodName()
    elif type == 'product':
        return inputProduct()
    elif type == 'barcode':
        return inputBarcode()
    else:
        return input()


def selectMenu(title, menu_list):
    index = 0
    print(title)
    for item in menu_list:
        print(str(index) + ". " + item)
        index += 1
    menu = inputNumber(0, len(menu_list) - 1)
    return menu


def showBadProducts(product_list=[]):
    if product_list:
        print("[검색된 유해식품]")
        for product in product_list:
            print(product[product_name_index] + "  " + product[product_barcode_index])
    else:
        print("검색된 유해식품이 없습니다.")


def badProductSearch():
    menu = selectMenu("[유해식품 검색 메뉴]", search_menu_list)
    if menu == 0:
        return
    if menu == 1:
        showBadProducts(searchProductName(inputUser("product")))
    if menu == 2:
        showBadProducts(searchBarcode(inputUser("barcode")))


if __name__ == "__main__":
    while True:
        menu = selectMenu("[메인 메뉴]", main_menu_list)
        if menu == 0:
            break
        if menu == 1:
            print(searchFood(inputUser("foodname")))
        if menu == 4:
            badProductSearch()
